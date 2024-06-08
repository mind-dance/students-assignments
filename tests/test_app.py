import os
import csv
import unittest
import shutil
from ctrl.check_tools import *
from ctrl.dao import *

class Test_app(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.db = Database("database2.db")
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
        self.t.aname = "抽卡时的心态管理"
        # 教师：派蒙
        self.t.tid = "t2024003"
        self.t.aid = self.db.get_a_id(self.t.tid, self.t.aname)
        demo_files = ["202412340103_嗨嗨嗨_大疆军火！", "202412340104——人工智障？蠢到家了",\
                      "噫好我中了！上课也要发202412340105次店", "鸡你太美-202412340101",\
                      "熊大快来，光头强又砍树了！","202412340106-赵六-抽卡时的心态管理",\
                      "202412340107-孙七-抽卡时的心态管理","202412340108-周八-抽卡时的心态管理",\
                      "202412340109-吴九-抽卡时的心态管理","202412340110-郑十-抽卡时的心态管理"]
        # 断言作业id
        self.assertEqual(self.t.aid,"YS20240106")
        # 数据库查询学生表（字典）
        s_dict = self.db.get_all_s()
        # 文件名设置：学号-姓名-作业标题.docx，后期可以优化数据库，让教师关联设置。
        config = ["sid", "sname", "aname"]
        # 准备收作业的文件夹
        abs_path = os.path.join(self.db.data_path, self.t.aname)
        # 清空文件夹
        if os.path.exists(abs_path):
            shutil.rmtree(abs_path)
        # 创建文件准备用于测试
        self.create_files(abs_path, demo_files)
        files_list = self.t.get_all_files(abs_path)
        # 断言文件读取函数
        self.assertEqual(set(files_list),set(demo_files))
        # 生成标准文件清单
        std_list = self.t.generate_files_list(s_dict, config)
        ans_std_list = ['202412340101-坤一-抽卡时的心态管理.docx', '202412340102-熊二-抽卡时的心态管理.docx', '202412340103-张三-抽卡时的心态管理.docx', '202412340104-李四-抽卡时的心态管理.docx', '202412340105-王五-抽卡时的心态管理.docx', '202412340106-赵六-抽卡时的心态管理.docx', '202412340107-孙七-抽卡时的心态管理.docx', '202412340108-周八-抽卡时的心态管理.docx', '202412340109-吴九-抽卡时的心态管理.docx', '202412340110-郑十-抽卡时的心态管理.docx']
        self.assertEqual(std_list, ans_std_list)
        # 检查提交信息
        done, miss, error = self.t.check_files(files_list, std_list)
        # 找出可以识别但文件名不正确的文件
        bug_tuple, etc = self.t.read_files_sid(error)
        # 生成bug的学号列表
        bug_sid_list = self.get_sub(bug_tuple,0)
        # 制作bug的学号字典
        bug_s_dict = self.db.get_s_dict(bug_sid_list)
        # 重命名
        self.t.rename_files(abs_path, bug_tuple, bug_s_dict, config)
        ans_bug_fix_files = []
        # 再次检查文件
        files_list = self.t.get_all_files(abs_path)
        done, miss, error = self.t.check_files(files_list, std_list)
        # 打印缺交列表
        miss, null = self.t.read_files_sid(miss)
        miss_id = self.get_sub(miss, 0)
        miss_dict = self.db.get_s_dict(miss_id)
        ans_miss_dict = [{"sid":"202412340102","sname":"熊二"}]
        self.assertEqual(miss_dict,ans_miss_dict)
        csv_path = os.path.join(abs_path,"miss.csv")
        with open(csv_path,"w",encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f,["sid","sname"])
            writer.writeheader()
            for row in miss_dict:
                writer.writerow(row)
        # 写入已交作业的名单
        m_tuple = self.t.make_m_tuple(done)
        self.db.set_submits(m_tuple)