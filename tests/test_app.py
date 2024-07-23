import os
import csv
import unittest
import shutil
from backend.tools import *
from backend.database import *

class Test_app(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.db = Database("demo.db")
        self.t = Tools()
        

    def create_files(self, abs_path, files):
        # 确保目标路径存在
        if not os.path.exists(abs_path):
            os.makedirs(abs_path)
        os.chdir(abs_path)
        for i in files:
            try:
                with open(i, 'w', encoding='utf-8') as f:
                    f.write('This is a test file.')
            except FileExistsError:
                pass
    
    def get_sub(self, packge, index):
        back = []
        for i in packge:
            back.append(i[index])
        return back

    def test_main(self):
        self.db.cur.execute("DELETE FROM submits")
        self.db.con.commit()
        demo_files = ["202412340103_嗨嗨嗨_大疆军火！", "202412340104——人工智障？蠢到家了",\
                      "噫好我中了！上课也要发202412340105次店", "鸡你太美-202412340101",\
                      "熊大快来，光头强又砍树了！","202412340106-赵六-抽卡时的心态管理",\
                      "202412340107-孙七-抽卡时的心态管理","202412340108-周八-抽卡时的心态管理",\
                      "202412340109-吴九-抽卡时的心态管理","202412340110-郑十-抽卡时的心态管理"]
        # 准备收作业的文件夹
        abs_path = os.path.join(self.db.same_path, "抽卡时的心态管理")
        # 清空文件夹
        if os.path.exists(abs_path):
            shutil.rmtree(abs_path)
        # 创建文件准备用于测试
        self.create_files(abs_path, demo_files)
        filenames = self.t.read_filenames(abs_path)
        # 断言文件读取函数
        self.assertEqual(set(filenames),set(demo_files))
        # 生成标准文件清单
        std_list = self.t.make_std_list(s_dict, config)
        ans_std_list = ['202412340101-坤一-抽卡时的心态管理.docx', '202412340102-熊二-抽卡时的心态管理.docx', '202412340103-张三-抽卡时的心态管理.docx', '202412340104-李四-抽卡时的心态管理.docx', '202412340105-王五-抽卡时的心态管理.docx', '202412340106-赵六-抽卡时的心态管理.docx', '202412340107-孙七-抽卡时的心态管理.docx', '202412340108-周八-抽卡时的心态管理.docx', '202412340109-吴九-抽卡时的心态管理.docx', '202412340110-郑十-抽卡时的心态管理.docx']
        self.assertEqual(std_list, ans_std_list)