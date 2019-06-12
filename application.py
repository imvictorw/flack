import os

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")
    # return "Project 2: TODO"
    
@app.route("/channel", methods=["POST"])
def channel():
    name = request.form.get("name")
    print("1  :" + name)
    return render_template("channel.html", name=name)
    
@app.route("/chatpost", methods=["POST"])
def chatpost():
    name = request.form.get("username")
    message = request.form.get("message")
    outputM = name + ": " + message
    print(name)
    print(message)
    return render_template("channel.html", outputM = outputM)