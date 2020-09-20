from my_app import app
from flask import render_template, request, redirect
import requests

post_profile = {
    "Pomodoro": {
        "Work": {"min": 25, "sec": 0, "msg": "Time to Work!"},
        "Break": {"min": 5, "sec": 0, "msg": "Rest Period"}
    },
    "20-20-20": {
        "Work": {"min": 20, "sec": 0, "msg": "Time to Work!"},
        "Break": {"min": 0, "sec": 20, "msg": "Rest Period; Focus your eyes on something at least 20 feet away!"}
    }
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profile")
def profile():
    if request.method == "POST":
        post_info = request.get_json()
        # TODO
    return render_template("profile.html") # TODO
    
@app.route("/name/<string:name>")
def name(name):
    return "Hello" + str(name) + "!"

@app.route("/timer")
def timer():
    return render_template("timer.html")

"""@app.route("/choose", methods=["POST"])
def choose():
    if request.method == "POST":
        post_info = request.get_json()
        new_post = Post(title=post_info['name'], minute=post_info['min'],  second=post_info['sec'])
    return render_template("choose.html")

@app.route("/post", methods=["POST"])
def post():
    if request.method == "POST":
        print(request)
        post_info = request.get_json()
        new_post = Post(title=post_info['title'], description=post_info['description'])
        db.session.add(new_post)
        db.session.commit()
    return redirect("/")"""