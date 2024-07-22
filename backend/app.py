from flask import Flask, jsonify
from flask_cors import CORS
from tools import Tools

app = Flask(__name__)
CORS(app)  # 这行代码启用了CORS，允许来自任何源的请求
# 初始化
t = Tools()

@app.route('/api/welcome', methods=['GET'])
def welcome():
    return jsonify({"message": "道爷我成啦！"})

# 由前端提供绝对路径
@app.route("/api/target")
def load_filenames(path):
    '''输入目标文件夹'''
    t.target_path = path
    return "0"

# 查看作业完成情况，返回done，miss，error列表
@app.route("/api/check")
def check():
    return "ok"

# 打开文件
@app.route("/api/open")
def open_file():
    return "this is test"

# 导出名单
@app.route("/api/export")
def export():
    return "nice"