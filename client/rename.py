import os
import json


# 获取当前目录下的所有文件名
def get_all_file(abs_path):
    files = []
    # 列出所有文件与子文件夹
    dirs = os.listdir(abs_path)
    # 过滤出文件
    for item in dirs:
        if os.path.isfile(os.path.join(abs_path, item)):
            files.append(item)
    return files

def rename_file(target_file, config):
    pass


