import os
import shutil
import time
from asyncio import Semaphore

from relax.download import download_all
from relax.title_ import get_title
from relax.utils import color_print, get_ua, read_json, write_json


def main():
    t1 = time.time()

    config_name = 'okjx.json'
    data = read_json(config_name)
    target_dir = data['target_dir']
    if not target_dir:
        while True:
            target_dir = input('请设置输出目录,只需设置一次:\n')
            if not os.path.isdir(target_dir):
                print('输出目录不合法\n')
                continue
            else:
                break
        data['target_dir'] = target_dir
        write_json(config_name, data)

    exe_path = os.path.join(os.getcwd(), 'okjx.json')
    color_print(f'配置路径 {exe_path} \n输出路径 {target_dir}', 'yellow')

    temp_dir = os.path.join(target_dir, 'temp')
    headers = {'user-agent': get_ua()}
    sem = Semaphore(10)
    s = input('请输入下载地址,多个地址用 | 隔开:\n')
    urls = s.split('|')
    video_list = []
    for i in urls:
        title = get_title(i, headers)
        video_list.append({'title': title.strip(), 'url': i})

    color_print('所有开始...', 'yellow')

    suc_list = []
    for i in video_list:
        title = i['title']
        url = i['url']
        f1 = os.path.join(temp_dir, title)
        if not os.path.isdir(f1):
            os.makedirs(f1)
        suc = False
        try:
            suc = download_all(sem, url, temp_dir, target_dir, title, headers)
            suc_list.append(suc)
        except Exception as e:
            color_print(f'存在异常 {title} {round(time.time()-t1)}s {e}', 'red')
            suc_list.append(suc)
            continue
    for i in video_list:
        shutil.rmtree(os.path.join(temp_dir, i['title']))
    if False in suc_list:
        color_print(f'存在失败 {round(time.time()-t1)}s', 'red')
        s = input('按任何键继续, 退出请输入 1\n')
        if s == '1':
            return
        main()
        return
    color_print(f'温馨提示: 输出目录修改: {exe_path}')
    color_print(f'所有成功 {round(time.time()-t1)}s 小苗祝您看片愉快 请查看: {target_dir}')
    s = input('按任何键继续, 退出请输入 1\n')
    if s == '1':
        return
    main()


if __name__ == '__main__':
    main()
