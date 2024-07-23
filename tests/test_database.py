from backend.database import *
import unittest



class Test_import_normal(unittest.TestCase):
    def setUp(self) -> None:
        self.db = Database()
        
    def test_make_insert_ok(self):
        '''测试插入语句构建函数是否正常工作'''
        # 答案
        ans = "INSERT INTO students (sid, sname) VALUES (?, ?)"
        # 学生字段
        s_field = ["sid", "sname"]
        # 输出
        out = self.db.make_insert("students",s_field)
        # 断言
        self.assertEqual(out, ans)
    
    def test_make_update_ok(self):
        '''测试更新语句'''
        ans = "UPDATE submits SET hw = ?, status = ?, path = ? WHERE sid = ?"
        field = ["hw", "status", "path"]
        condition = "sid"
        out = self.db.make_update("submits", field, condition)
        self.assertEqual(out, ans)

