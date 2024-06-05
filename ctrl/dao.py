import os
import csv
import sqlite3


class Database():
    def __init__(self, target_db = "database.db"):
        # 获取项目的根目录，以及其他高频的相对路径
        self.root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_path = os.path.join(self.root_path, "data")
        self.db_path = os.path.join(self.data_path, target_db)
        self.sql_path = os.path.join(self.data_path, "sql")
        # 连接数据库
        self.con = sqlite3.connect(self.db_path)
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
        
    # 查看所有学生
    def load_s_data(self):
        s_dict = []
        result = self.cur.execute("SELECT student_id, student_name FROM students").fetchall()
        for row in result:
            s_dict.append({"sid":row[0],"sname":row[1]})
        return s_dict
    
    def get_s_name(self, sid_list):
        '''根据学号查名字'''
        s_dict = []
        for i in sid_list:
            sname = self.cur.execute("SELECT student_name FROM students WHERE student_id = ?",(i,)).fetchone()
            # 从元组中取出sname
            s_dict.append({"sid":i,"sname":sname[0]})
        return s_dict
    
    # 获取作业id
    def get_a_id(self, tid, aname):
        '''获取作业id'''
        aid = self.cur.execute("SELECT assignment_id FROM assignments WHERE teacher_id = ? AND assignment_name = ?",(tid,aname)).fetchone()
        return aid[0]
    
    # 提交作业记录
    def set_submits(self, m_tuple):
        '''保存作业提交记录'''
        for row in m_tuple:
            self.cur.execute("INSERT INTO submits (student_id, assignment_id) VALUES (?, ?)", row)
        self.con.commit()

        
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

