from flask import Flask
from flask import request
from markupsafe import escape

app = Flask(__name__) # create instance of Flask class

@app.route("/") # create route decorator to bind function to route
def hello_world(): # function triggered at route
    return "<p>Hello, World!</p>"

@app.route("/<name>", methods=['GET', 'POST'])
def print_name(name):
    if request.method == 'POST':
        return f"Added, {escape(name)}"
    else:
        return f"Found, {escape(name)}"