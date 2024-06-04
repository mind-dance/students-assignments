import os
import csv
import sqlite3


class Database():
    def __init__(self):
        foo = os.getcwd()
        db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"database.db")
        # 连接数据库
        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()
        
        

    # 导入学生名单
    def import_s(self, csvfile, table = "students"):
        # try:
        # 打开文件
        with open(csvfile, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            # 读取学生信息
            for row in reader:
                # 插入数据库
                self.cur.execute("INSERT INTO " + table + " (student_id, student_name) VALUES (?, ?)", \
                                 (row["student_id"], row["student_name"]))
            self.con.commit()
        # except:
        #     print("打不开文件")
    
    # 导入作业布置情况
    def import_a(self, csvfile, table = "assignments"):
        try:
            with open(csvfile) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.cur.execute("INSERT INTO " + table + " (assignment_id, teacher_id, assignment_name) VALUES (?, ?, ?)", \
                                     row["assignment_id"], row["teacher_id"],row["assignment_name"])
                self.con.commit()
        except:
            pass
    
    # 导入作业提交情况
    def import_m(self, csvfile, table = "submits"):
        try:
            with open(csvfile) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.cur.execute("INSERT INTO " + table + " (student_id, assignment_id, status) VALUES (?, ?, ?)", \
                                     row["student_id"], row["assignment_id"],row["status"])
                self.con.commit()
        except:
            pass
    
    # 导入教师名单
    def import_t(self, csvfile, table = "teachers"):
        try:
            self.table_t = ["teacher_id", "teacher_name"]
            with open(csvfile) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.cur.execute("INSERT INTO " + table + " (teacher_id, teacher_name) VALUES (?, ?)", \
                                     row["teacher_id"], row["teacher_name"])
                self.con.commit()
        except:
            pass



    # 单个增加
    def insert_student(self):
        pass
    # 增，学生作业提交情况，已交、缺交
    def status():
        pass
    # 删，删除某个学生
    
    # 修改学生信息

    # 查，所有学生
    def load_students_data(self):
        pass
    # 查，作业提交情况
    # 查，学生个人作业提交率

# temp = cur.execute("SELECT student_id, name FROM students")
# for row in temp:
#     id, name = row
#     print(id,name)
# con.commit()
# con.close()