import os
import unittest
import shutil

from ctrl.check_tools import *

# 正常工作单元测试，工作于临时文件夹
class Test_Tools_normal(unittest.TestCase):
    def setUp(self):
        # 创建测试文件夹
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        if os.path.exists("temp"):
            shutil.rmtree("temp")
        os.mkdir("temp")
        # 实例化工具类
        self.t = Tools()

    def tearDown(self):
        # 删除测试文件夹
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        shutil.rmtree("temp")

    def test_get_all_file(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        temp_path = os.path.join(current_path, 'temp')
        os.chdir(temp_path)
        # 批量创建文件和文件夹
        folders = ["folder1", "folder2", "folder3"]
        files = ["file1.txt", "file2.txt", "file3.txt"]
        # folders = ["Don't panic", "42", "The answer of everything"]
        # files = ["The Hitchhiker's Guide to the Galaxy.txt", "The Restaurant at the End of the Universe.mobi", "Life, the Universe and Everything.azw3", "So Long, and Thanks for All the Fish.epub", "Mostly Harmless.pdf"]
        for item in folders:
            os.makedirs(item, exist_ok=True)
        for item in files:
            with open(item, 'w') as f:
                f.write('This is a test file.')
        # 测试函数
        get_file = self.t.get_all_file(temp_path)
        # 断言
        self.assertEqual(set(get_file), set(files))
    
    def test_generate_filenames(self):
        ans = ['202412340101-骰子-实验1-日常生活中如何进攻一个村庄.docx', '202412340102-红中-实验1-日常生活中如何进攻一个村庄.docx', '202412340103-张三-实验1-日常生活中如何进攻一个村庄.docx']
        src = [{"sid":"202412340101","sname":"骰子","aname":"实验1-日常生活中如何进攻一个村庄"},\
               {"sid":"202412340102","sname":"红中","aname":"实验1-日常生活中如何进攻一个村庄"},\
               {"sid":"202412340103","sname":"张三","aname":"实验1-日常生活中如何进攻一个村庄"},\
                ]
        config = ["sid","sname","aname"]
        out = self.t.generate_files_list(src,config)
        self.assertEqual(out,ans)

    # 检查文件提交情况，可能有正常提交，缺交，未知的文件名
    def test_check_files(self):
        files = ["张三-实验1.docx", "李四-实验1.docx", "孙七-实验1.docx", "周八-实验1.docx"]
        std = ["张三-实验1.docx",\
                "李四-实验1.docx",\
                "王五-实验1.docx",\
                "赵六-实验1.docx"]
        ans_done = {"张三-实验1.docx", "李四-实验1.docx"}
        ans_miss = {"王五-实验1.docx", "赵六-实验1.docx"}
        ans_error = {"孙七-实验1.docx", "周八-实验1.docx"}
        out_done, out_miss, out_error =  self.t.check_files(files, std)
        self.assertEqual(out_done, ans_done)
        self.assertEqual(out_miss, ans_miss)
        self.assertEqual(out_error, ans_error)

    
    # 测试从文件名中读取学号
    def test_read_id_list(self):
        # 样例文件名列表
        test_error_list = ["202412340603-xxx-实验1.docx",\
                "202412340604-李四-疯狂星期四.v50",\
                "202412340605-王五-kfc",\
                "202412340606-赵六-实验666.ppt",\
                "吴九-实验1.docx"]
        # 答案
        ans = [("202412340603", "202412340603-xxx-实验1.docx"), ("202412340604", "202412340604-李四-疯狂星期四.v50"), \
               ("202412340605", "202412340605-王五-kfc"), ("202412340606", "202412340606-赵六-实验666.ppt")]
        ans_etc = ["吴九-实验1.docx"]
        # 测试函数
        result, etc = self.t.read_id_list(test_error_list)
        # 断言
        self.assertEqual(set(result),set(ans))
        self.assertEqual(set(etc),set(ans_etc))

    # 测试批量重命名
    def test_rename_files(self):
        src = [{"sid":"202412340101","sname":"骰子","aname":"实验1-日常生活中如何进攻一个村庄"},\
               {"sid":"202412340102","sname":"红中","aname":"实验1-日常生活中如何进攻一个村庄"},\
               {"sid":"202412340103","sname":"张三","aname":"实验1-日常生活中如何进攻一个村庄"},\
                ]
        config = ["sid","sname","aname"]
        
        pass





    # def test_generate_filenames(self):
    #     current_path = os.path.dirname(os.path.abspath(__file__))
    #     temp_path = os.path.join(current_path, 'temp')
    #     os.chdir(temp_path)
    #     config = [id, name, exp]
    #     src = [{"student_id": "202412340604", "name": "李四", "exp":"实验1"},\
    #            {"student_id": "202412340605", "name": "王五", "exp":"实验1"},\
    #            {"student_id": "202412340606", "name": "赵六", "exp":"实验1"},
    #            ]
    #     out = rename_file("file1.txt", )