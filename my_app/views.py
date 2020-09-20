from my_app import app
from flask import render_template, request, redirect
import requests

post_profile = {
    "Pomodoro": [
        {"min": 25, "sec": 0, "msg": "Work", "submsg": "Time to work!", "type":"work", "default":True},
        {"min": 5, "sec": 0, "msg": "Rest Period", "submsg": "Time to rest!", "type":"break", "default":True}
    ],
    "20-20-20": [
        {"min": 20, "sec": 0, "msg":"Work", "submsg": "Time to work!", "type":"work", "default":True},
        {"min": 0, "sec": 20, "msg": "Rest Period", "submsg": "Rest Period; Focus your eyes on something at least 20 feet away!", "type":"break", "default":True}
    ]
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profile", methods=["GET","POST"])
def profile():
    if request.method == "GET":
        return render_template("profile.html", profiles=post_profile)
    elif request.method == "POST":
        post_info = request.get_json()
        """Name will be something like "Pomodoro", and method will be something like [
         {"min": 25, "sec": 0, "msg": "Work", "submsg": "Time to work!", "type":"work"},
         {"min": 5, "sec": 0, "msg": "Rest Period", "submsg": "Time to rest!", "type":"break"}] """

        if post_info['name'] in post_profile.keys():
            # Exception; tryig to post a custom study habit that is already in the list
            return redirect("/profile/overlap-error")
        post_profile[post_info['name']] = post_info["method"]
        return render_template("profile.html", profiles=post_profile)
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