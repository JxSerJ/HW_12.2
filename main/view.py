from flask import Blueprint, render_template, request

from app import posts_data
from functions import post_search

photo_viewer = Blueprint("photo_viewer", __name__)


@photo_viewer.route("/")
def photo_page():
    return render_template("index.html")


@photo_viewer.route("/search")
def search_page():
    s = request.args.get("s")
    found_posts = post_search(s, posts_data)
    return render_template("post_list.html", s=s, found_posts=found_posts)
