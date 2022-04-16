import json
import os
import random
import re
import subprocess
from asyncio.subprocess import PIPE

from click import echo, style
from requests import Session
from tqdm import tqdm
from urllib3 import disable_warnings

disable_warnings()
session_r = Session()


def bar_print(content: str, fg: str = 'green'):
    return echo(style(f'\r{content.ljust(100)}\r', fg=fg))


def color_print(content: str, fg: str = 'green'):
    return echo(style(f'{content}', fg=fg))


def extract_ts(content: str):
    res = re.sub(r'#(.*?)\s+', '', content)
    return re.split(r'\s+', res)


def safe_str(raw: str):
    return re.sub(r'[<>:"/\|?*\s]', '', raw)


def read_json(file_path: str):
    with open(file_path, mode='r', encoding='utf8') as f:
        return json.load(f)


def write_json(file_path: str, content: str):
    with open(file_path, mode='w', encoding='utf8') as f:
        json.dump(content, f)


def encoding_to_utf8(os_name):
    if os_name == 'linux' or os_name == 'darwin':
        return
    # 设置编码为utf8, 为了防止windows系统乱码
    subprocess.run(['chcp', '65001'], shell=True, stdout=subprocess.DEVNULL)


def get_ua():
    contents = read_json('relax/ua_fake.json')
    return random.choice(contents)


def get_url_pre(content: str):
    matched = re.search(r'https://(.*?)/', content, re.S)
    return matched.group().rstrip('/')


def get_url_domain(content: str):
    matched = get_url_pre(content)
    return matched.replace('https://', '').split(':')[0]


def get_random_16():
    return ''.join(random.sample('abcdefghijklmnopqrstuvwxyz1234567890', 16))


def req_break(url: str, dst: str, headers: dict, bytes: int = 1024) -> bool:
    # 断点续传下载 https://blog.csdn.net/qq_38534107/article/details/89721345
    response = session_r.get(url, headers=headers, stream=True)
    file_size = int(response.headers['content-length'])
    if os.path.exists(dst):
        first_byte = os.path.getsize(dst)
    else:
        first_byte = 0
    if first_byte >= file_size:
        return True

    headers.update({"Range": f"bytes={first_byte}-{file_size}"})

    size = 0
    desc = dst.rsplit(os.path.sep, 1)[1]
    with tqdm(total=file_size,
              initial=first_byte,
              unit='B',
              unit_scale=True,
              desc=desc,
              leave=True,
              mininterval=1,
              colour='yellow',
              bar_format='{l_bar}{bar:10}{r_bar}') as pbar:
        req = session_r.get(url, headers=headers, stream=True)
        with open(dst, 'ab') as f:
            for chunk in req.iter_content(chunk_size=bytes):
                if chunk:
                    size += len(chunk)
                    f.write(chunk)
                    pbar.update(bytes)
    return size == file_size


def merge_video(os_name: str,
                content_list: list,
                source_path: str,
                target_file_name: str,
                target_dir: str = '',
                is_long: bool = True):
    '''
    is_long: 如果合并的文件太多,会有长度限制, 所以一般超过800个ts文件[如果用数字命名:1.ts,2.t3,3.ts...],我就会使用这个参数
    '''
    target_file_abs = os.path.join(target_dir, target_file_name)
    res = -1
    bash_file_name = 'ts_sh'
    if os_name == 'windows':
        # 拷贝不同磁盘的时候, 完整路径都要加上
        content_list = [f'{os.path.join(source_path,i)}' for i in content_list]
        ts_str = '+'.join(content_list)
        bash_str = f'cd "{source_path}" && copy /b {ts_str} "{target_file_abs}"'
        if is_long:
            bash_file_path = os.path.join(source_path, f'{bash_file_name}.bat')
            with open(bash_file_path, mode='w', encoding='utf8') as f:
                f.write(bash_str)
            bash_str = bash_file_path
    elif os_name == 'linux' or os_name == 'darwin':
        ts_str = ' '.join(content_list)
        bash_str = f'cd "{source_path}" && cat {ts_str} > "{target_file_abs}"'
        if is_long:
            bash_file_path = os.path.join(source_path, f'{bash_file_name}.sh')
            with open(bash_file_path, mode='w', encoding='utf8') as f:
                f.write(bash_str)
            bash_str = f'chmod +x {bash_file_path} && {bash_file_path}'

    try:
        res = subprocess.run(bash_str, shell=True, stdout=PIPE, stderr=PIPE)
        res_code = res.returncode
        if res_code != 0:
            color_print(
                f'合并失败 {target_file_name} 错误 {res.stdout.decode("utf8")}',
                'red')
            return -1
        return 0
    except Exception as e:
        color_print(f'合并失败 {target_file_name} {e}', 'red')
        return -1
