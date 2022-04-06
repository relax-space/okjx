import json
import os
import re
import time
from asyncio import Semaphore
from copy import deepcopy

from relax.crypto_r import CryptoR
from relax.download_async import download_start
from relax.merge import merge_ts
from relax.utils import (bar_print, color_print, extract_ts, get_url_domain,
                         get_url_pre, req_break, session_r)


def get_1(url: str, headers: dict):
    req_url = f'https://okjx.cc?url={url}'
    resp = session_r.get(req_url, headers=headers)
    content = resp.text
    if not content:
        color_print(f'请求失败 get_1 {req_url}', 'red')
        return f'https://api.okjx.cc:3389/jx.php?url={url}'
    matched = re.search(r'src="(.*?)"', content, re.S)
    new_url = matched.group(1)
    return new_url


def get_2(raw_url: str, headers: dict):

    # req: https://api.okjx.cc:3389/jx.php
    url = get_1(raw_url, headers)
    if not url:
        return '', ''
    new_headers = deepcopy(headers)
    new_headers.update({'referer': 'https://okjx.cc/'})
    resp = session_r.get(url, headers=new_headers)
    content = resp.text
    if not content:
        color_print(f'请求失败 get_2 {url}', 'red')
        return '', ''
    url_list = re.findall(r'<a href="javascript:play\(\'(.*?)\'\)">', content,
                          re.S)
    if not url_list:
        color_print(f'请求失败 2 get_2 {url}', 'red')
        return '', ''
    url_pre: str = get_url_pre(url_list[0])
    urls = []
    for i, j in enumerate(url_list):
        if i == 0:
            urls.append(j)
            continue
        urls.append(f'{url_pre}{j}')
    urls = urls[0:-1]
    return urls, url


def get_3(raw_url: str, headers: dict):
    # <iframe src="
    # req: https://m3u8.okjx.cc:3389/3jx.php
    urls, pre_url = get_2(raw_url, headers)
    if not urls:
        return '', '', ''
    url = urls[0]

    new_headers = deepcopy(headers)
    new_headers.update({'referer': f'{get_url_pre(pre_url)}/'})
    resp = session_r.get(url, headers=new_headers)
    content = resp.text
    if not content:
        color_print(f'请求失败 get_3 {url}', 'red')
        return '', '', ''
    matched = re.search(r'<iframe src="(.*?)"', content, re.S)
    new_url = matched.group(1)
    return f'{get_url_pre(url)}/{new_url}', url, urls


def get_4(raw_url: str, headers: dict):

    # req: https://m3u8.okjx.cc:3389/m3.php
    url, referer, urls = get_3(raw_url, headers)
    if not url:
        return '', '', '', '', '', '', ''
    new_headers = deepcopy(headers)
    new_headers.update({'referer': referer})
    resp = session_r.get(url, headers=new_headers)
    content = resp.text
    if not content:
        color_print(f'请求失败 get_4 {url}', 'red')
        return '', '', '', '', '', '', ''
    matched = re.search(
        r'bt_token = "(?P<t>.*?)".*?"id": "(?P<id>.*?)".*?"api":"(?P<api>.*?)".*?"key": "(?P<key>.*?)".*?getVideoInfo\("(?P<url_crypto>.*?)"',
        content, re.S)
    t = matched.group('t')
    id = matched.group('id')
    api = matched.group('api')
    key = matched.group('key')
    url_crypto = matched.group('url_crypto')
    return t, id, api, key, url_crypto, url, urls


def get_5(raw_url: str, headers: dict):
    # 第一步: 创建并授权iv
    # req: https://shouquan.laohutao.com/shouquan.php?t=73cc003d898729c1
    t, id, api, key, url_crypto, pre_url, urls = get_4(raw_url, headers)
    if not url_crypto:
        return '', '', ''
    new_headers = deepcopy(headers)
    referer = get_url_pre(pre_url)
    new_headers.update({'referer': referer})
    shouquan_url = 'https://shouquan.laohutao.com/shouquan.php'

    d = CryptoR('dvyYRQlnPRCMdQSe',
                t).encrypto(f'{get_url_domain(pre_url)}|{t}')
    resp = session_r.post(shouquan_url,
                          params={'t': t},
                          data={'d': d},
                          headers=new_headers)
    content = resp.text
    if not content:
        color_print(f'请求失败 get_5 {url}', 'red')
        return '', '', ''

    # 第二步: 通过iv解密url_crypto
    url = CryptoR('36606EE9A59DDCE2', t).decrypto(url_crypto)
    return url, referer, urls


def get_6_1(raw_url: str, target_path: str, file_name: str,
            headers: dict) -> bool:
    dst = os.path.join(target_path, f"{file_name}.mp4")
    return req_break(raw_url, dst, headers, session_r, 512)


def get_6_2(retry_count: list, urls: list, pre_url: str, url: str,
            headers: dict):
    headers = deepcopy(headers)
    headers.update({
        'origin': pre_url,
    })

    resp = session_r.get(url, headers=headers)
    content = resp.text
    if not content:
        color_print(f'请求失败 get_6_2 {url}', 'red')
        return []
    if '<html>' in resp.text:
        retry_count[0] = retry_count[0] - 1
        if retry_count[0] > 0:
            color_print(f'请求失败 get_6_2  剩余重试次数 {retry_count[0]} {url}',
                        'yellow')
            time.sleep(5)
            return get_6_2(retry_count, urls, pre_url, url, headers)
        color_print(f'请求失败 get_6_2 重试10次之后依然失败', 'red')
        return []
    ts_list = extract_ts(content)
    return ts_list


def download_all(sem: Semaphore, parent_dir: str, raw_url: str,
                 folder_name: str, target_path: str, file_name: str,
                 headers: dict):
    t1 = time.time()
    url, pre_url, urls = get_5(raw_url, headers)
    if not url:
        return False
    t2 = time.time()
    bar_print(f'参数成功 {file_name} {round(t2-t1)}s')

    if '.mp4' in url:
        res = get_6_1(url, target_path, file_name, headers)
        if not res:
            bar_print(
                f'下载失败 download_all {file_name} {round(time.time()-t2)}s {url}',
                'red')
            return False
        bar_print(f'下载成功 {file_name} {round(time.time()-t2)}s {url}')
        return True
    elif '.m3u8' in url:
        retry_count = [10]
        ts_list = get_6_2(retry_count, urls, pre_url, url, headers)

        ts_list = [{
            'index': f'{i:0>5}',
            'url': v
        } for i, v in enumerate(ts_list)]
        with open(os.path.join(folder_name, file_name, 'params.json'),
                  mode='w',
                  encoding='utf8') as f:
            json.dump(ts_list, f)
        retry_list = download_start(sem, url, folder_name, file_name, ts_list,
                                    headers)
        t3 = time.time()
        if retry_list:
            bar_print(
                f'开始重试 {file_name} {round(t3-t2)}s 重试个数({len(retry_list)})',
                'red')
            with open(os.path.join(folder_name, file_name, 'ts_err.json'),
                      mode='w',
                      encoding='utf8') as f:
                json.dump(retry_list, f)
            retry_list = download_start(sem, url, folder_name, file_name,
                                        retry_list, headers)
            if retry_list:
                bar_print(f'重试失败 {file_name} 失败个数({len(retry_list)})', 'red')
                with open(os.path.join(folder_name, file_name, 'ts_err.json'),
                          mode='w',
                          encoding='utf8') as f:
                    json.dump(retry_list, f)
                return False
        bar_print(f'下载成功 {file_name} {round(t3-t2)}s')

        res = merge_ts(ts_list, parent_dir,
                       os.path.join(folder_name,
                                    file_name), file_name, target_path)
        if res == -1:
            bar_print(
                f'合并失败 download_all {file_name} {round(time.time()-t3)}s',
                'red')
            return False
        bar_print(f'合并成功 {file_name} {round(time.time()-t3)}s')
        return True
    else:
        bar_print(f'格式无效 {file_name} {url}', 'red')
        return False
