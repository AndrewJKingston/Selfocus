from my_app import app
from flask import render_template, request, redirect
import requests

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profile")
def profile():
    return '<h2>Profile Page</h2>'
    
@app.route("/name/<string:name>")
def name(name):
    return "Hello" + str(name) + "!"

@app.route("/timer/<int:time>")
def timer(time):
    return render_template("timer.html", time=time)