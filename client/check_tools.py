import os
import re
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
    # 返回所有文件名
    return files

# 生成命名列表
def generate_filenames(src, config):
    parts = []
    for placeholder in config:
        parts.append(src.get(placeholder))
    new_name = '-'.join(parts) + '.docx'
    return

# 检查作业是否提交
def check_files(files, src):
    files = set(files)
    src = set(src)
    done = src.intersection(files)
    miss = src.difference(files)
    error = files.difference(src)
    return done, miss, error

# 读取文件名id
def read_id(files):
    error_list = []
    etc = []
    pat = re.compile(r"\d{12}")
    for i in files:
        id = re.findall(pat,i)
        if id:
            error_list.append((id[0],i))
        else:
            etc.append(i)
    return error_list, etc

# 重命名文件
# def rename_file(target_file, src, config):
    
#     correct_name = "-".join(config[:-1]).join(config[-1])
#     os.rename(target_file, correct_name)

def rename_file(target_file, src, config):
    parts = []
    for field in config:
        parts.append(str(src.get(field)))
    new_name = '-'.join(parts) + '.docx'
    os.rename(target_file, new_name)

# 示例用法
src_data = {'student_id': '202412340603', 'name': '张三'}
config = ['student_id', 'name']
rename_file('old_file.txt', src_data, config)
