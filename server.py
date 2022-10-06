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

@app.get('/get_route')
def handle_get():
    return "<h1>GET got</h1>"

@app.post('/post_route')
def handle_get():
    return "<h1>POST'd</h1>"