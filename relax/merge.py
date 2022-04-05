
import os
import platform

from relax.utils import bar_print, merge_video


def merge_ts(content_list: list, parent_dir: str,
             source_path: str, target_file_name: str, target_path: str = ''):
    os_name = platform.system().lower()
    indexs = [f'{i["index"]}.ts' for i in content_list]
    act_indexs = [i for i in os.listdir(source_path)
                  if '.ts' in i
                  and os.path.getsize(os.path.join(source_path, i)) != 0
                  ]
    if indexs != act_indexs:
        bar_print(
            f'合并失败 {target_file_name} 失败列表 {set(indexs)-set(act_indexs)}')
        return -1
    is_long = True if len(act_indexs) > 800 else False
    res = merge_video(os_name, act_indexs, parent_dir,
                      source_path, f'{target_file_name}.mp4', target_path, is_long)
    return res
