import re
import uuid
from copy import deepcopy

from relax.utils import session_r


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


def get_youku(url: str, headers: dict) -> str:
    headers = deepcopy(headers)
    headers.update({'referer': 'https://movie.youku.com'})
    resp = session_r.get(url, headers=headers)
    resp.encoding = 'utf8'
    txt = resp.text
    with open('step/youku.html', mode='w', encoding='utf8') as f:
        f.write(txt)
    matched = re.search(r'"og:title" content\="(.*?)"', txt, re.S)
    return matched.group(1)


def get_title(url: str, headers: dict):
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
        title = get_youku(url, headers)
    if not title:
        title = uuid.uuid4().hex
    return title
