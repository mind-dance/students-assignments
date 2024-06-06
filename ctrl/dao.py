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
        # 合法sql表与字段
        self.valid_table = {"students", "teachers", "assignments", "submits"}
        self.valid_field = {"student_id","student_name", "teacher_id", "teacher_name", "assignment_id", "assignment_name"}

    # 构建查询语句
    def make_insert(self, table, field):
        '''输入目标表，字段名，数值，会检验字段名、表名是否合法，但是不会检测字段名是否应该出现在表中,有执行函数捕捉错误进行异常处理'''
        # 检查表是否合法
        if table not in self.valid_table:
            raise ValueError("表名有误")
        
        query = "INSERT INTO " + table
        clauses = []
        values = []
        for i in field:
            if i in self.valid_field:
                clauses.append("?")
                values.append(i)
            else:
                raise ValueError("字段名有误")
        if clauses:
            query = query + " (" + ", ".join(field) + ") VALUES (" + ", ".join(clauses) + ")"
        return query

    # 有sql注入风险。
    # 下一步完善计划，用if语句验证用户输入，用开发者添加从句，用户输入用？传参。
    # https://cs50.readthedocs.io/libraries/cs50/python/#how-can-i-add-optional-clauses-to-a-query
    def import_csv(self, csvfile, table):
        '''导入表格，需要负责异常捕捉'''
        # 清空表格
        self.cur.execute("DELETE FROM " + table)
        try:
            # 打开csv文件
            with open(csvfile, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                # 读取字段
                field = next(reader)
                for row in reader:
                    # 构建查询语句并执行
                    query = self.make_insert(table, field)
                    self.cur.execute(query,row)
                # 提交事务
                self.con.commit()
        # 捕捉异常，例如找不到字段无法插入等。
        except:
            print("出错了")
    

    # 更新学生作业提交情况，已交
    def add_submits(self, sid_set, aid):
        '''sid is list for student_id'''
        for i in sid_set:
            self.cur.execute("INSERT INTO submits (student_id, assignment_id) VALUES (?, ?)", \
                                    (i, aid))

    # 查看所有学生，
    def get_s_data(self):
        '''获取学生表，返回s_dict，list[dict{key,key}]'''
        s_dict = []
        result = self.cur.execute("SELECT student_id, student_name FROM students").fetchall()
        for row in result:
            s_dict.append({"sid":row[0],"sname":row[1]})
        return s_dict
    
    # 获取学号
    def get_s_dict(self, sid_list):
        '''根据学号查名字，回s_dict，list[dict{key,key}]'''
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
            self.cur.execute("INSERT OR IGNORE INTO submits (student_id, assignment_id) VALUES (?, ?)", row)
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

