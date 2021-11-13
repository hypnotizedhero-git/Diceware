from flask import Flask,url_for
import random

from flask.templating import render_template

numbers=list(str(i) for i in range(1,7))
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/canvas")
def render():
    return render_template('index.html')