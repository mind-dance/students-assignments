from client.dao import *
import unittest

class Test_import(unittest.TestCase):
    
    # 测试导入学生表
    def test_import_s(self):
        ans = [('202412340103', '张三'), ('202412340104', '李四'), ('202412340105', '王五'), \
               ('202412340106', '赵六'), ('202412340107', '孙七'), ('202412340108', '周八')]
        csvfile = os.path.join(os.path.dirname(os.path.abspath(__file__)),"demo\\demo_students.csv")
        db = Database("demo.db")
        db.cur.execute("DROP TABLE IF EXISTS students")
        db.cur.execute('''CREATE TABLE "students" (
            "student_id" VARCHAR NOT NULL,
            "student_name" VARCHAR NULL,
            PRIMARY KEY ("student_id"));''')
        db.import_s(csvfile)
        result = db.cur.execute("SELECT * FROM students").fetchall()
        self.assertEqual(result, ans)
        db.cur.execute("DROP TABLE students")
    
    # 测试导入教师表
    def test_import_t(self):
        ans = [('t2024001', '罗翔'), ('t2024002', '蔡徐坤'), ('t2024003', '马嘉祺'), ('t2024004', '丁程鑫'), ('t2024005', '宋亚轩'), ('t2024006', '刘耀文'), ('t2024007', '张真源'), ('t2024008', '严浩翔'), ('t2024009', '贺峻霖')]
        csvfile = os.path.join(os.path.dirname(os.path.abspath(__file__)),"demo\\demo_teachers.csv")
        db = Database("demo.db")
        db.cur.execute("DROP TABLE IF EXISTS teachers")
        db.cur.execute('''CREATE TABLE "teachers" (
            "teacher_id" VARCHAR(50) NOT NULL,
            "teacher_name" VARCHAR(50) NOT NULL,
            PRIMARY KEY ("teacher_id"));''')
        db.import_t(csvfile)
        result = db.cur.execute("SELECT * FROM teachers").fetchall()
        # self.assertEqual(result, ans)
        db.cur.execute("DROP TABLE teachers")
    
    # 测试导入作业布置表
    def test_import_a(self):
        ans = [('DB20240101', 't200043210101', '实验1-日常生活中如何进攻一个村庄'), ('DB20240102', 't200043210102', '实验2-铁山靠及其衍生动作的学习'), ('DB20240103', 't200043210103', '实验3-三角毛衣')]
        csvfile = os.path.join(os.path.dirname(os.path.abspath(__file__)),"demo\\demo_assignments.csv")
        db = Database("demo.db")
        db.cur.execute("DROP TABLE IF EXISTS assignment")
        db.cur.execute('''CREATE TABLE "assignment" (
            "assignment_id" VARCHAR(50) NOT NULL,
            "teacher_id" VARCHAR(50) NOT NULL,
            "assignment_name" VARCHAR(50) NOT NULL,
            PRIMARY KEY ("assignment_id")
            CONSTRAINT "0" FOREIGN KEY ("teacher_id") REFERENCES "teachers" ("teacher_id") ON UPDATE CASCADE ON DELETE NO ACTION);''')
        db.import_a(csvfile)
        result = db.cur.execute("SELECT * FROM assignment").fetchall()
        self.assertEqual(result, ans)
        db.cur.execute("DROP TABLE assignment")
    
    # 测试导入统计表
    def test_import_m(self):
        ans = [('202412340103', 'DB20240101', 0), ('202412340104', 'DB20240103', 1), ('202412340103', 'DB20240103', 0)]
        csvfile = os.path.join(os.path.dirname(os.path.abspath(__file__)),"demo\\demo_submits.csv")
        db = Database("demo.db")
        db.cur.execute("DROP TABLE IF EXISTS submits")
        db.cur.execute('''CREATE TABLE "demo_submits" (
            "student_id" VARCHAR(50) NOT NULL,
            "assignment_id" VARCHAR(50) NOT NULL,
            "status" INTEGER NULL DEFAULT '1',
            CONSTRAINT "0" FOREIGN KEY ("assignment_id") REFERENCES "assignment" ("assignment_id") ON UPDATE CASCADE ON DELETE NO ACTION,
            CONSTRAINT "1" FOREIGN KEY ("student_id") REFERENCES "students" ("student_id") ON UPDATE CASCADE ON DELETE NO ACTION);''')
        db.import_m(csvfile)
        result = db.cur.execute("SELECT * FROM submits").fetchall()
        self.assertEqual(result, ans)
        db.cur.execute("DROP TABLE submits")


class Test_load(unittest.TestCase):
    def test_load_students_data(self):
        pass