import os
import json
from flask import Flask, jsonify
from flask_cors import CORS
from tools import Tools

app = Flask(__name__)
CORS(app)  # 这行代码启用了CORS，允许来自任何源的请求
# 初始化
t = Tools()
os.chdir(t.same_path)

# 如果有预设就读取
if os.path.exists("config.json"):
    t.get_config()

# 欢迎
@app.route('/api/welcome', methods = ['GET'])
def welcome():
    return jsonify({"message": "道爷我成啦！"})

# 添加目标路径
@app.route("/api/target", method = ["PUT"])
def load_filenames(path):
    '''输入目标文件夹'''
    t.target_path = path
    return "ok"

# 添加模板
@app.route("/api/template", method = ["PUT"])
def load_template(template):
    '''输入模板'''
    t.template = template
    return "ok"

# 查看作业完成情况，返回done，miss，error列表
@app.route("/api/check", method = ["GET"])
def check():
    return "ok"

# 打开文件
@app.route("/api/open", method = ["GET"])
def open_file():
    return "ok"

# 导出名单
@app.route("/api/export", method = ["GET"])
def export():
    return "ok"