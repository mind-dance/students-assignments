from flask import Flask
from dao import *
from check_tools import *
app = Flask(__name__)

db = Database()
t = Tools()


t.tid = "t2024003"
t.aname = "抽卡时的心态管理"
# aname = input("输入需要统计的作业名")

# 需要统计的作业id
t.aid = db.get_a_id(t.tid ,t.aname)
# 学生名单
s_dict = db.load_s_data()
config = ["sid", "sname", "aname"]
# 加载文件列表
abs_path = input("文件夹 :")
files_list = t.get_all_files(abs_path)
std_list = t.generate_files_list(s_dict, config)
# 已提交、未找到、意料之外的文件名
done, miss, error = t.check_files(files_list, std_list)
bug_tuple, etc = t.read_id_list(error)
bug_sid_list = []
for row in bug_tuple:
    # 学号加入名单
    bug_sid_list.append(row[0])
bug_s_dict = db.get_s_name(bug_sid_list)
t.rename_files(abs_path, bug_tuple, bug_s_dict, config)

# 将错误文件名
# foo = t.check_files(fixed, miss)
# 获得最终提交了作业的名单，
# done.update(foo[0])
# miss.update(foo[1])







@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"