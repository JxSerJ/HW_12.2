from flask import Flask, request, render_template, send_from_directory
from config import POST_PATH, UPLOAD_FOLDER
from functions import load_file, post_search
from main.views import photo_viewer
from loader.views import post_loader

app = Flask(__name__)
app.config["EXPLAIN_TEMPLATE_LOADING"] = True

app.register_blueprint(photo_viewer)
app.register_blueprint(post_loader)

posts_list = load_file(POST_PATH)


@app.route("/list")
def page_tag():
    pass


@app.route("/uploads/<path:path>", methods=["POST"])
def static_dir(path):
    picture = request.files.get("picture")
    return send_from_directory("uploads", path)


app.run(debug=True)
