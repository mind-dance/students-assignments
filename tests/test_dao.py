from backend.database import *
import unittest



class Test_import_normal(unittest.TestCase):
    def setUp(self) -> None:
        self.db = Database()
        
    def test_make_insert_ok(self):
        '''测试插入语句构建函数是否正常工作'''
        # 答案
        ans = "INSERT INTO students (student_id, student_name) VALUES (?, ?)"
        # 学生字段
        s_field = ["student_id", "student_name"]
        # 输出
        out = self.db.make_insert("students",s_field)
        # 断言
        self.assertEqual(out, ans)
    @unittest.skip("还没写好测试")
    def test_import_csv(self):
        pass

class Test_Work(unittest.TestCase):
    def setUp(self) -> None:
        self.db = Database()

    def tearDown(self) -> None:
        pass
    @unittest.skip("还没写好测试")
    def test_get_all_s(self):
        out = self.db.read_s_table()
        print(out)
    def test_get_a_id(self):
        aid = self.db.get_a_id("t2024003", "抽卡时的心态管理")
        print(aid)
        pass
    # 测试获取学生名字
    def test_get_s_name(self):
        ans = [{'sid': '202412340103', 'sname': '张三'}, {'sid': '202412340104', 'sname': '李四'}, {'sid': '202412340105', 'sname': '王五'}]
        sid_list = ["202412340103","202412340104","202412340105"]
        out = self.db.get_s_dict(sid_list)
        self.assertEqual(out, ans)