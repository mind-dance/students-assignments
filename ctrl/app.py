from flask import Flask
from dao import *
app = Flask(__name__)

db = Database()







@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"