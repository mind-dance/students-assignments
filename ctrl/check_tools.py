import os
import re

class Tools():
    def __init__(self):
        pass
    
    def get_all_file(self,abs_path):
        '''获取目标目录的所有文件名'''
        files = []
        # 列出所有文件与子文件夹
        dirs = os.listdir(abs_path)
        # 过滤出文件
        for item in dirs:
            if os.path.isfile(os.path.join(abs_path, item)):
                files.append(item)
        # 返回所有文件名
        return files
    
    def generate_files_list(self, sid_list, config):
        '''生成应交作业名单，输入src列表，每个元素为字典。返回一个列表，用于判断正确提价的文件名'''
        std_list = []
        # 用于获取设置中的值
        for row in sid_list:
            parts = []
            for col in config:
                parts.append(row.get(col))
            new_name = '-'.join(parts) + '.docx'
            std_list.append(new_name)
        return std_list

    def check_files(self, files, std):
        '''比较已交文件夹中的文件与应交作业的名单，返回三个集合'''
        files = set(files)
        std = set(std)
        done = std.intersection(files)
        miss = std.difference(files)
        error = files.difference(std)
        return done, miss, error

    def read_id_list(self, files):
        '''尝试识别未识别的文件名'''
        cort_list = []
        etc = []
        pat = re.compile(r"\d{12}")
        for i in files:
            id = re.findall(pat,i)
            if id:
                cort_list.append((id[0],i))
            else:
                etc.append(i)
        return cort_list, etc

    def rename_files(self, abs_path, src, config):
        '''重命名已识别但不正确的文件名,src为识别成功准备重命名的列表，每个元素为元组，第一位为id，第二为文件名'''
        
        foo = self.generate_files_list(src, config)
        # os.rename(, new_name)
