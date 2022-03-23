from flask import Flask, request, render_template, send_from_directory
from config import POST_PATH, UPLOAD_FOLDER
from functions import load_file
from main.view import photo_viewer

app = Flask(__name__)


app.register_blueprint(photo_viewer)

DATA = load_file(POST_PATH)
print(DATA)


@app.route("/list")
def page_tag():
    pass


@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    pass


@app.route("/post", methods=["POST"])
def page_post_upload():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(debug=True)
