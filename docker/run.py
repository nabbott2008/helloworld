#!/usr/bin/env python3
from flask import Flask, render_template, request
app = Flask(__name__)

def handle_input()
    userIn = request.args.get('name', 'default name goes here')
    return render_template('user.html', user=userIn, data=data)

@app.route("/")
def hello():
    return "hello\nworld"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
