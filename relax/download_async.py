import os
from asyncio import Semaphore, as_completed, get_event_loop

import aiofiles
from aiohttp import ClientSession, TCPConnector
from tqdm import tqdm

from relax.utils import bar_print


async def req(sem: Semaphore, delete_212: bool, index: str, url: str, ts_folder_path: str, file_name: str,  headers: dict, session: ClientSession):
    try:
        async with sem:
            async with session.get(url, headers=headers) as resp:
                async with aiofiles.open(os.path.join(ts_folder_path, file_name), mode='wb') as f:
                    res = await resp.read()
                    if delete_212:
                        res = res[212:]
                    await f.write(res)
            return index
    except Exception as e:
        bar_print(f'请求异常 {ts_folder_path} {url}  错误 {e}', 'red')
        return '-1'


async def download_ts(sem: Semaphore, raw_url: str, folder_name: str, file_name: str, ts_list: list, headers: dict):
    exp_set = set()
    act_set = set()
    ts_folder_path = os.path.join(folder_name, file_name)
    tasks = []
    pre_url_ts = raw_url.rsplit('/', 1)[0]
    async with ClientSession(connector=TCPConnector(limit=40)) as session:
        for i in ts_list:
            index = i['index']
            url = i['url']
            delete_212 = False
            if not url.startswith('http'):
                url = f'{pre_url_ts}/{url}'
            elif '.ts' not in url:
                delete_212 = True
            exp_set.add(index)
            tasks.append(req(sem, delete_212, index, url, ts_folder_path,
                         f'{index}.ts', headers, session))
        for i in tqdm(as_completed(tasks), desc=file_name, total=len(ts_list), leave=False, bar_format='{l_bar}{bar:10}{r_bar}', colour='yellow'):
            act_set.add(await i)
    if exp_set != act_set:
        diff_set = exp_set - act_set
        retry_list = [i for i in ts_list if i['index'] in diff_set]
        return retry_list
    return []


def download_start(sem: Semaphore, url: str, folder_name: str, file_name: str, ts_list: list, headers: dict):

    retry_list = get_event_loop().run_until_complete(
        download_ts(sem, url, folder_name, file_name, ts_list, headers))
    if retry_list:
        get_event_loop().run_until_complete(
            download_ts(sem, url, folder_name, file_name, retry_list, headers))
    return retry_list
