from client.dao import *
import unittest

class Test_dao(unittest.TestCase):
    def test_import_s(self):
        ans = [('202412340103', '张三'), ('202412340104', '李四'), ('202412340105', '王五'), \
               ('202412340106', '赵六'), ('202412340107', '孙七'), ('202412340108', '周八')]
        db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"database.db")
        csvfile = os.path.join(os.path.dirname(os.path.abspath(__file__)),"demo\\demo_students.csv")
        table = "demo_students"
        db = Database()
        db.cur.execute('''CREATE TABLE "demo_students" (
                       "student_id" VARCHAR NOT NULL,
                       "student_name" VARCHAR NULL,
                       PRIMARY KEY ("student_id"));''')
        db.import_s(csvfile, table)
        result = db.cur.execute("SELECT * FROM " + table).fetchall()
        self.assertEqual(result, ans)
        db.cur.execute("DROP TABLE " + table)