from flask import Flask, jsonify
from flask_cors import CORS
from tools import Tools
from database import Database

app = Flask(__name__)
CORS(app)  # 这行代码启用了CORS，允许来自任何源的请求
# 初始化
t = Tools()
db = Database()
# 读取学生表，制作标准名单并存储到属性
t.std_list = t.create_std_list(db.read_s_table())
error_list = t.check_hw()
etc = t.read_error_list(error_list)
@app.route('/api/welcome', methods=['GET'])
def welcome():
    return jsonify({"message": "道爷我成啦！"})

@app.route("/api/load-filenames")
def load_filenames(abs_path):
    '''加载本地文件夹中所有的文件名'''
    return t.read_filenames(abs_path=abs_path)

@app.route("/api/s-object")
def s_object():
    return "ok"

@app.route("/api/test")
def test():
    return "this is test"