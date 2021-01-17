from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/home')
def index():
    return 'Hello Flask'

@app.route('/user/<user_id>', methods = ["GET", "POST", "PULL", "DELETE"])
def param(user_id):
    if request.method == "GET":
        return "GET method"
    elif request.method == "POST":
        data = request.form
        return data
    elif request.method == "PULL":
        return "PULL method"
    elif request.method == "DELETE":
        return "DELETE method"
    else :
        return "Not allowed method"

app.run()  # app.run(host = 'http://localhost')