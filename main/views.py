from flask import Blueprint, render_template, request, url_for

from config import POST_PATH
from functions import post_search, load_file

photo_viewer = Blueprint("photo_viewer", __name__, template_folder="loader_templates")

posts_list = load_file(POST_PATH)


@photo_viewer.route("/")
def photo_page():
    url_css = url_for('static', filename='style.css')
    return render_template("index.html", url_css=url_css)


@photo_viewer.route("/search")
def search_page():
    url_css = url_for('static', filename='style.css')
    s = request.args.get("s")
    found_posts = post_search(s, posts_list)
    return render_template("post_list.html", s=s, found_posts=found_posts, url_css=url_css)
