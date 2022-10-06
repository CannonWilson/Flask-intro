from flask import Flask

app = Flask(__name__) # create instance of Flask class

@app.route("/") # create route decorator
def hello_world(): # function triggered at route
    return "<p>Hello, World!</p>"