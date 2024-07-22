from flask import Flask, jsonify
from flask_cors import CORS
from tools import Tools
from database import Database

app = Flask(__name__)
CORS(app)  # 这行代码启用了CORS，允许来自任何源的请求

t = Tools()
db = Database()

@app.route('/api/welcome', methods=['GET'])
def welcome():
    return jsonify({"message": "道爷我成啦！"})

@app.route("/api/load-filenames")
def load_filenames(abs_path):
    '''加载本地文件夹中所有的文件名'''
    return t.load_filenames(abs_path=abs_path)

@app.route("/api/s-object")
def s_object():
    return "ok"

@app.route("/api/test")
def test():
    return "this is test"