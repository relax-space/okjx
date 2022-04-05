import os
import platform

from relax.utils import bar_print, encoding_to_utf8, merge_video


def merge_ts(content_list: list,
             parent_dir: str,
             source_path: str,
             target_file_name: str,
             target_path: str = ''):
    os_name = platform.system().lower()
    encoding_to_utf8(os_name)
    indexs = [f'{i["index"]}.ts' for i in content_list]
    act_indexs = [i for i in os.listdir(source_path) if '.ts' in i]
    if indexs != act_indexs:
        bar_print(
            f'合并失败 {target_file_name} 失败列表 {set(indexs)-set(act_indexs)}')
        return -1
    is_long = True if len(act_indexs) > 800 else False
    res = merge_video(os_name, act_indexs, parent_dir, source_path,
                      f'{target_file_name}.mp4', target_path, is_long)
    return res
