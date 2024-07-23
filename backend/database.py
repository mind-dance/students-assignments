import os
import csv
import sqlite3


class Database():


    def __init__(self, target_db = "database.db"):
        # 获取项目的根目录，以及其他高频的相对路径
        self.root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.same_path = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.same_path, target_db)
        self.sql_path = os.path.join(self.same_path, "sql")
        # 连接数据库
        self.con = sqlite3.connect(self.db_path)
        self.cur = self.con.cursor()
        # 合法sql表与字段
        self.valid_table = {"students", "submits"}
        self.valid_field = {"sid", "sname", "hw", "status", "path"}


    # 参考了cs50包含从句的query语句构建教程
    # https://cs50.readthedocs.io/libraries/cs50/python/#how-can-i-add-optional-clauses-to-a-query
    def make_insert(self, table: str, fields: list):
        '''构建插入语句，需要输入目标表，字段名，会检验字段名、表名是否合法，但是不会检测字段名是否应该出现在表中,由执行函数捕捉错误进行异常处理'''
        # 检查表是否合法
        if table not in self.valid_table:
            raise ValueError("表名有误")
        query = "INSERT INTO " + table
        clauses = []
        for i in fields:
            if i in self.valid_field:
                clauses.append("?")
            else:
                raise ValueError("字段名有误")
        if clauses:
            query = query + " (" + ", ".join(fields) + ") VALUES (" + ", ".join(clauses) + ")"
        return query

    def make_update(self, table: str, fields: list, condition: str):
        # 检查表是否合法
        if table not in self.valid_table:
            raise ValueError("表名有误")
        query = "UPDATE " + table + " SET "
        clauses = []
        for i in fields:
            if i in self.valid_field:
                clauses.append("?")
            else:
                raise ValueError("字段名有误")
        if clauses:
            query = query + ", ".join(f"{field} = ?" for field in fields)
            query = query + " WHERE " + condition + " = ?"
        return query
    
    def make_select(self, table: str, fields: list[str], condition = None):
        # 读取
        if table not in self.valid_table:
            raise ValueError("表名有误")
        query = "SELECT "
        query = query + ", ".join(f"{field}" for field in fields) + " FROM " + table
        if condition:
            query = query + " WHERE " + condition + " = ?"
        return query

    # 构建查询语句
    def import_csv(self, csvfile, table):
        '''导入表格，需要负责异常捕捉'''
        # 清空表格
        self.cur.execute("DELETE FROM " + table)
        try:
            # 打开csv文件
            with open(csvfile, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                # 读取字段
                fields = next(reader)
                query = self.make_insert(table, fields)
                for row in reader:
                    # 构建查询语句并执行
                    self.cur.execute(query,row)
                # 提交事务
                self.con.commit()
        # 捕捉异常，例如找不到字段无法插入等。
        except:
            print("出错了")
    

    # 获取所有学号
    def read_all_s_id(self):
        s_id = []
        result = self.cur.execute("SELECT student_id FROM students").fetchall()
        for row in result:
            s_id.append(row[0])
        return s_id
    
    # 获取学生json对象
    def get_s_object(self, sid):
        '''获取学生json对象'''
        s_dict = {}
        sname = self.cur.execute("SELECT sname FROM students WHERE sid = ?",sid).fetchone()[0]
        # 从元组中取出sname
        s_dict["sid"] = sid
        s_dict["sname"] = sname
        return s_dict
    
    # 根据学号查标注作业名
    def get_s_hw(self, sid):
        query = self.make_select("submits", ["hw"], "sid")
        values = [sid]
        hw = self.con.execute(query, values).fetchone()[0]
        return hw

    # 更新学生数据
    def update_s(self, fields:list, condition, values):
        query = self.make_update("submits", fields, condition)
        self.con.execute(query, values)
        self.con.commit()