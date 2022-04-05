import os
import shutil
import time
from asyncio import Semaphore

from relax.download import download_all
from relax.utils import color_print, get_ua


def main():
    color_print('所有开始 ...', 'yellow')
    t1 = time.time()
    video_list = [
        # ('test1', 'https://v.youku.com/v_show/id_XNTg1MjY0NjY2OA==.html?spm=a2h0c.8166622.PhoneSokuProgram_1.dtitle&s=babe00f6ce8647778338'),
        ('test3', 'https://www.mgtv.com/b/386365/15380241.html?fpa=se&lastp=so_result'),
    ]
    folder_name = 'temp'
    target_path = 'data'
    headers = {'user-agent': get_ua()}
    sem = Semaphore(40)
    parent_dir = os.path.dirname(__file__)
    suc_list = []
    for i, v in video_list:
        f1 = os.path.join(folder_name, i)
        f2 = os.path.join(folder_name, i)
        if not os.path.isdir(f1):
            os.makedirs(f1)
        if not os.path.isdir(f2):
            os.makedirs(f2)
        suc = download_all(sem, parent_dir, v, folder_name,
                           target_path, i, headers)
        suc_list.append(suc)
    if False in suc_list:
        color_print(f'存在失败 {round(time.time()-t1)}s', 'red')
        return

    for i, _ in video_list:
        shutil.rmtree(os.path.join(folder_name, i))
    color_print(f'所有成功 {round(time.time()-t1)}s')


if __name__ == '__main__':
    main()
