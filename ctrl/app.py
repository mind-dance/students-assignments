from flask import Flask
from dao import *
from check_tools import *
app = Flask(__name__)

db = Database()
t = Tools()


t.tid = "t2024003"
t.aname = input("输入需要统计的作业名")

# 需要统计的作业id
t.aid = db.get_a_id(t.tid ,t.aname)
# 学生名单
s_dict = db.get_s_data()
config = ["sid", "sname", "aname"]
# 加载文件列表
abs_path = input("文件夹 :")
files_list = t.get_all_files(abs_path)
std_list = t.generate_files_list(s_dict, config)
# 已提交、未找到、意料之外的文件名
done, miss, error = t.check_files(files_list, std_list)
# 找出可以识别但文件名不正确的文件
bug_tuple, etc = t.read_files_sid(error)
# 生成bug的学号列表
bug_sid_list = []
for row in bug_tuple:
    # 学号加入名单
    bug_sid_list.append(row[0])
# 制作bug的学号字典
bug_s_dict = db.get_s_dict(bug_sid_list)
# 重命名
t.rename_files(abs_path, bug_tuple, bug_s_dict, config)

# 再次检查文件
files_list = t.get_all_files(abs_path)
done, miss, error = t.check_files(files_list, std_list)
# 打印缺交列表

# 写入已交作业的名单
m_tuple = t.get_m_tuple(done)
db.set_submits(m_tuple)








@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"