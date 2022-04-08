import os
import re
import time
import uuid
from copy import deepcopy
from urllib.parse import quote

from relax.utils import safe_str, session_r


def get_qq(url: str, headers: dict) -> str:
    resp = session_r.get(url, headers=headers)
    resp.encoding = 'utf8'
    txt = resp.text
    with open('step/qq.html', mode='w', encoding='utf8') as f:
        f.write(txt)
    matched = re.search(r'"title":"(.*?)"', txt, re.S)
    return matched.group(1)


def get_qiyi(url: str, headers: dict) -> str:
    resp = session_r.get(url, headers=headers)
    resp.encoding = 'utf8'
    txt = resp.text
    with open('step/yiqi.html', mode='w', encoding='utf8') as f:
        f.write(txt)
    matched = re.search(r'"tvName":"(.*?)"', txt, re.S)
    return matched.group(1)


def get_mgtv(url: str, headers: dict) -> str:
    resp = session_r.get(url, headers=headers)
    resp.encoding = 'utf8'
    txt = resp.text
    with open('step/mgtv.html', mode='w', encoding='utf8') as f:
        f.write(txt)
    matched = re.search(r'<title>(.*?) - ', txt, re.S)
    return matched.group(1)


def get_bili(url: str, headers: dict) -> str:
    resp = session_r.get(url, headers=headers)
    resp.encoding = 'utf8'
    txt = resp.text
    with open('step/bili.html', mode='w', encoding='utf8') as f:
        f.write(txt)
    matched = re.search(r'"title":"(.*?)"', txt, re.S)
    return matched.group(1)


def youku_cna(headers: dict):

    def url_quote(val):
        if '%' in val:
            return val
        return quote(val)

    url = 'http://log.mmstat.com/eg.js'
    resp = session_r.get(url, headers=headers)
    resp_headers = resp.headers
    for i, v in resp_headers.items():
        if i == 'set-cookie':
            s1 = v.split('; ')
            for j in s1:
                key, val = j.split('=')
                if key == 'cna':
                    return url_quote(val)
    return url_quote('DOG4EdW4qzsCAbZyXbU+t7Jt')


def youku_vid(url: str):
    matched = re.search(r'youku.com/v_show/id_([0-9a-zA-z=]+)', url)
    return matched.group(1)


def get_youku(raw_url: str, headers: dict, list: list):
    vid = youku_vid(raw_url)
    # 来自you-get
    ckey = 'DIl58SLFxFNndSV1GFNnMQVYkx1PP5tKe1siZu/86PR1u/Wh1Ptd+WOZsHHWxysSfAOhNJpdVWsdVJNsfJ8Sxd8WKVvNfAS8aS8fAOzYARzPyPc3JvtnPHjTdKfESTdnuTW6ZPvk2pNDh4uFzotgdMEFkzQ5wZVXl2Pf1/Y6hLK0OnCNxBj3+nb0v72gZ6b0td+WOZsHHWxysSo/0y9D2K42SaB8Y/+aD2K42SaB8Y/+ahU+WOZsHcrxysooUeND'
    headers = deepcopy(headers)
    headers.update({'referer': 'https://v.youku.com'})
    cna = youku_cna(headers)
    params = {
        "vid": vid,
        'ccode': '0532',
        'client_ip': '192.168.1.1',
        'utid': cna,
        'client_ts': str(int(time.time())),
        'ckey': quote(ckey),
    }
    url = 'https://ups.youku.com/ups/get.json'
    resp = session_r.get(url, params=params, headers=headers)
    data = resp.json()
    video = data['data'].get('video')
    retry_count = list[0]
    if not video:
        if retry_count > 0:
            list[0] -= 1
            time.sleep(3)
            return get_youku(raw_url, headers, list)
        else:
            return None
    return video['title']


def get_title(url: str, headers: dict):
    if not os.path.isdir('step'):
        os.makedirs('step')
    title = ''
    if url.find('qq.com') != -1:
        title = get_qq(url, headers)
    elif url.find('qiyi.com') != -1:
        title = get_qiyi(url, headers)
    elif url.find('mgtv.com') != -1:
        title = get_mgtv(url, headers)
    elif url.find('bilibili.com') != -1:
        title = get_bili(url, headers)
    elif url.find('youku.com') != -1:
        list = [2]
        title = get_youku(url, headers, list)
    if not title:
        title = uuid.uuid4().hex
    return safe_str(title)
