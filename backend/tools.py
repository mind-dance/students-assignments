import os
import re
from database import Database

db = Database()

class Tools():
    def __init__(self):
        self.root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.same_path = os.path.dirname(os.path.abspath(__file__))
        self.target_path = ""
        self.template = "计科-${sname}-${sid}-实验报告.docx"
        # self.std_list = []

    def get_root(self):
        return self.root_path
    
    def get_path(self, file):
        return os.path.join(self.target_path, file)

    def _make_filename(self, sid):
        '''生成单个文件名'''
        s_object = db.get_s_object(sid)
        # 替换模板中的占位符
        filename = self.template
        for ph, val in s_object.items():
            filename = filename.replace("${" + ph + "}", val)
        return filename
    
    def _rename_file(self, file, filename):
        '''重命名已识别但不正确的文件名,s_dict为识别成功准备重命名的列表'''
        os.chdir(self.target_path)
        os.rename(file, filename)

    # 第一步，读取文件
    def read_filenames(self,abs_path):
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
    
    # 第二步，读取学号，生成标准名单，写入数据库
    def create_std_list(self):
        '''生成标准名单，写入数据库'''
        s_id = db.read_all_s_id()
        fields = ["hw", "status"]
        for sid in s_id:
            row = [self._make_filename(sid), 0]
            query = db.make_update("submits", fields, sid)
            db.cur.execute(query, row)
        db.con.commit()

    # 第三步，检查作业，添加路径到数据库
    def check_hw(self):
        filenames = self.read_filenames(self.target_path)
        error_list = []
        # 从数据库读取所有作业名，保存为列表
        query = db.make_select("submits", ["hw"])
        out = db.cur.execute(query)
        std_list = []
        for row in out:
            std_list.append(row[0])
        # 检测单个文件名是否在标注名单中
        for file in filenames:
            if file in std_list:
                # 将提交数据写入数据库
                path = self.get_path(file)
                # 更新数据
                db.update_s(["status", "path"], "hw", [1, path, file])
            else:
                error_list.append(file)
        db.con.commit()
        return error_list

    # 第四步，修正文件名
    def read_error_list(self, error_list):
        '''尝试识别未识别的文件名'''
        etc = []
        pat = re.compile(r"\d{12}")
        for file in error_list:
            # 读取学号
            sid = re.findall(pat,file)[0]
            # 如果找到学号
            if sid:
                # 查询该学号的标准文件名
                hw = db.get_s_hw(sid)
                # 重命名
                self._rename_file(file, hw)
                path = self.get_path(hw)
                # 更新数据
                db.update_s(["status", "path"], "sid", [1, path, sid])
            else:
                etc.append(file)
        return etc