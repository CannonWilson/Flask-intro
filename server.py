from flask import Flask
from markupsafe import escape

app = Flask(__name__) # create instance of Flask class

@app.route("/") # create route decorator to bind function to route
def hello_world(): # function triggered at route
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def print_name(name):
    return f"Hello, {escape(name)}"