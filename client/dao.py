import sqlite3


class Database():
    def __init__(self):
        # 连接数据库
        self.con = sqlite3.connect("client/database.db")
        self.cur = self.con.cursor()

    # 批量增加
    def import_students_data(self):
        pass
    # 单个增加
    def insert_student(self):
        pass
    # 增，学生作业提交情况，已交、缺交
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