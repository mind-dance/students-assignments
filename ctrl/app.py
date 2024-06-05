from flask import Flask
from dao import *
from check_tools import *
app = Flask(__name__)

db = Database()
t = Tools()







@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"