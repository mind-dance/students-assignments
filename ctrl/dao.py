import os
import csv
import sqlite3


class Database():
    def __init__(self, target_db = "database.db"):
        foo = os.getcwd()
        db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), target_db)
        # 连接数据库
        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()

    # 导入学生名单
    def import_s(self, csvfile):
        self.cur.execute("DELETE FROM students")
        # 打开文件
        with open(csvfile, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            # 读取学生信息
            for row in reader:
                # 插入数据库
                self.cur.execute("INSERT INTO students (student_id, student_name) VALUES (?, ?)", \
                                 (row["student_id"], row["student_name"]))
            self.con.commit()

    # 导入教师名单
    def import_t(self, csvfile):
        self.cur.execute("DELETE FROM teachers")
        with open(csvfile, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.cur.execute("INSERT INTO teachers (teacher_id, teacher_name) VALUES (?, ?)", \
                                    (row["teacher_id"], row["teacher_name"]))
            self.con.commit()
  
    # 导入作业布置情况
    def import_a(self, csvfile):
        self.cur.execute("DELETE FROM assignments")
        with open(csvfile, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.cur.execute("INSERT INTO assignments (assignment_id, teacher_id, assignment_name) VALUES (?, ?, ?)", \
                                    (row["assignment_id"], row["teacher_id"], row["assignment_name"]))
            self.con.commit()
    
    # 导入作业提交情况
    def import_m(self, csvfile):
        self.cur.execute("DELETE FROM submits")
        with open(csvfile, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.cur.execute("INSERT INTO submits (student_id, assignment_id) VALUES (?, ?)", \
                                    (row["student_id"], row["assignment_id"]))
            self.con.commit()
    


    # 更新学生作业提交情况，已交
    def add_submits(self, sid_set, aid):
        '''sid is list for student_id'''
        for i in sid_set:
            self.cur.execute("INSERT INTO submits (student_id, assignment_id) VALUES (?, ?)", \
                                    (i, aid))
        
# -- 假设表名为 your_table，包含列 name
# -- 要判断的条目 B 的值为 some_value

# BEGIN TRANSACTION;

# IF NOT EXISTS (SELECT 1 FROM submits WHERE student_id = ? AND assignment_id = ?) THEN
#     INSERT INTO submits (name) VALUES ('some_value');
# END IF;

# COMMIT TRANSACTION;


    # 删，删除某个学生
    
    # 修改学生信息

    # 查，所有学生
    def load_students_data(self, table = "students"):
        s_set = set()
        result = self.cur.execute("SELECT student_id FROM " + table)
        for row in result:
            s_set.add(row)
        return s_set
    
    # 查，作业提交情况
    # 本次实验X报告，应收A人，实收B人，缺交名单C
    def submits_status(self, assignment_id):
        smt_set = set()
        # 查找所有交了作业的名单
        smt = self.cur.execute("SELECT student_id FROM submits WHERE assignment_id = ?", assignment_id).fetchall()
        # 查找所有学生
        src = self.cur.execute("SELECT student_id FROM students").fetchall()
        smt = {row[0] for row in smt}
        src = {row[0] for row in src}
        miss = src.difference(smt)
        return miss



    # 查，学生个人作业提交率
