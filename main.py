import json
import os
import shutil
import time
from asyncio import Semaphore

from relax.download import download_all
from relax.utils import color_print, get_ua


def main():
    color_print('所有开始 ...', 'yellow')
    t1 = time.time()
    with open('okjx.txt', mode='r', encoding='utf8') as f:
        video_list = json.load(f)
    folder_name = 'temp'
    target_path = 'data'
    headers = {'user-agent': get_ua()}
    sem = Semaphore(10)
    parent_dir = os.path.dirname(__file__)
    suc_list = []
    for i in video_list:
        title = i['title']
        url = i['url']
        f1 = os.path.join(folder_name, title)
        f2 = os.path.join(folder_name, title)
        if not os.path.isdir(f1):
            os.makedirs(f1)
        if not os.path.isdir(f2):
            os.makedirs(f2)
        suc = download_all(sem, parent_dir, url, folder_name, target_path,
                           title, headers)
        suc_list.append(suc)
    if False in suc_list:
        color_print(f'存在失败 {round(time.time()-t1)}s', 'red')
        return

    for i in video_list:
        shutil.rmtree(os.path.join(folder_name, i['title']))
    color_print(f'所有成功 {round(time.time()-t1)}s')

    for i in range(10, 0, -1):
        print(f'\r将在{i}秒后,自动关闭\r', end='')
        time.sleep(1)


if __name__ == '__main__':
    main()
