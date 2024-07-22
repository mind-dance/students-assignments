import os
import re

class Tools():
    def __init__(self):
        self.root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.aid = ""
        self.aname = ""
        self.tid = ""
        self.tname = ""
        self.template = ""

    def get_root(self):
        return self.root_path
    
    def make_filename(self, s_object):
        '''生成一个文件名'''
        # 替换模板中的占位符
        filename = self.template
        for ph, val in s_object.items():
            filename = filename.replace("${" + ph + "}", val)
        return filename

    def save_filename(self, s_object, filename):
        '''将文件名记入字典中'''
        s_object["hw"] = filename

    def load_filenames(self,abs_path):
        '''获取目标目录的所有文件名'''
        filenames = []
        # 列出所有文件与子文件夹
        dirs = os.listdir(abs_path)
        # 过滤出文件
        for item in dirs:
            if os.path.isfile(os.path.join(abs_path, item)):
                filenames.append(item)
        # 返回所有文件名
        return filenames    

    def make_std_list(self):
        '''生成应交作业名单，输入学生的json对象，每个元素为字典。返回一个列表，用于判断正确提价的文件名'''
        std_list = []

        
        return std_list
    

    
    def make_m_tuple(self,done_set):
        '''根据完成sid，制作完成作业的元组(sid,aid)'''
        m_tuple = []
        out, null = self.read_files_sid(done_set)
        for row in out:
            sid = row[0]
            m_tuple.append((sid, self.aid))
        return m_tuple

    def check_files(self, files, std):
        '''比较已交文件夹中的文件与应交作业的名单，返回三个集合'''
        files = set(files)
        std = set(std)
        # 两集合的交集，被正确找到
        done = std.intersection(files)
        # 仅存在于标准中，未找到
        miss = std.difference(files)
        # 错误的文件名，暂时无法处理
        error = files.difference(std)
        return done, miss, error

    def read_files_sid(self, files):
        '''尝试识别未识别的文件名'''
        cort_tuple = []
        etc = []
        pat = re.compile(r"\d{12}")
        for i in files:
            id = re.findall(pat,i)
            if id:
                # 元组，学号0，文件名1
                cort_tuple.append((id[0],i))
            else:
                etc.append(i)
        return cort_tuple, etc

    def rename_files(self, abs_path, bug_tuple, s_dict, config):
        '''重命名已识别但不正确的文件名,s_dict为识别成功准备重命名的列表'''
        os.chdir(abs_path)
        cort_list = self.make_std_list()
        for i in range(len(s_dict)):
            os.rename(bug_tuple[i][1], cort_list[i])
        return 0