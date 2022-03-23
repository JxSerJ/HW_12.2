from flask import Flask, request, render_template, send_from_directory
from functions import load_file
from config import POST_PATH, UPLOAD_FOLDER

posts_data = load_file(POST_PATH)

app = Flask(__name__)

from main.view import photo_viewer

app.register_blueprint(photo_viewer)


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
