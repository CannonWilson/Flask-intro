from urllib import response
from flask import Flask, request, redirect, render_template, url_for
from markupsafe import escape
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app = Flask(__name__, static_url_path='', 
            static_folder='/static') # create instance of Flask class

@app.route("/") # create route decorator to bind function to route
def hello_world(): # function triggered at route
    return "<p>Hello, World!</p>"

@app.route("/<name>", methods=['GET', 'POST'])
def print_name(name):
    if request.method == 'POST':
        return f"Added, {escape(name)}"
    else:
        return f"Found, {escape(name)}"

@app.route('/get_route')
def handle_get():
    return "<h1>GET got</h1>"

@app.route('/post_route')
def handle_post():
    return "<h1>POST'd</h1>"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect('/')
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    ''' 