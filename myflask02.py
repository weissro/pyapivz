#!/usr/bin/python3

from flask import Flask, redirect, url_for, request, render_template

# Flask constructor takes the name of the current
# module (__name__) as argument
app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name} glad you could join us"

if __name__  == "__main__":
    app.run(port=5006)
