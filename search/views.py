from json import JSONDecodeError

from flask import Blueprint, render_template, request, url_for

from config import POST_PATH
from search.functions import post_search, load_file

search = Blueprint("main_page", __name__, template_folder="search_templates")

posts_list = []
error = None


@search.route("/")
def photo_page():

    global posts_list
    global error

    try:
        posts_list = load_file(POST_PATH)
    except FileNotFoundError:
        error = "Файл не найден"
    except JSONDecodeError:
        error = "Файл имеет неверный формат содержимого"
    finally:
        url_css = url_for("static", filename="style.css")
        if error:
            return render_template("error.html", url_css=url_css, error=error)
        else:
            return render_template("index.html", url_css=url_css, posts_list=posts_list)


@search.route("/search")
def search_page():

    url_css = url_for("static", filename="style.css")
    error = None
    s = request.args.get("s")
    found_posts = post_search(s, posts_list)
    if len(found_posts) == 0:
        error = "Ничего не найдено :("
        return render_template("error.html", url_css=url_css, error=error)
    return render_template("post_list.html", s=s, found_posts=found_posts, url_css=url_css)
