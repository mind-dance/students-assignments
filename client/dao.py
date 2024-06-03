import sqlite3


class database():
    def __init__(self):
        # 连接数据库
        self.con = sqlite3.connect('database.db')
        self.cur = self.con.cursor()
        self.cur.execute()

    def load_students_data():
        pass

    def import_students_data():
        pass
    
    def insert_student():
        pass

# 连接数据库
con = sqlite3.connect('client/database.db')
cur = con.cursor()
temp = cur.execute("SELECT * FROM students")
for row in temp:
    id, name = row
    print(id,name)
con.commit()
con.close()