#!/usr/bin/python3

from flask import Flask, make_response, request, render_template

## write some python code that connected to the database and pulled out the information you needed.

app = Flask(__name__)

@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/setcookie", methods = ["POST", "GET"])
def setcookie():
    if request.method == "POST":
        user = request.form.get("nm")

        resp = make_response(render_template("readcookie.html"))
        resp.set_cookie("userID", user)
        return resp
    elif request.method == "GET":
        return render_template("index.html")


@app.route("/getcookie")
def getcookie():
    name = request.cookies.get("userID")
    return f"Welcome back, {name}"

if __name__ == "__main__":
    app.run(port=5006)

    

