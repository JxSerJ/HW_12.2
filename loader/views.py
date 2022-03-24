from flask import Blueprint, render_template, url_for

post_loader = Blueprint("post_loader", __name__, template_folder="loader_templates")


@post_loader.route("/post", methods=["GET", "POST"])
def loader_page():
    url_css = url_for('static', filename='style.css')
    return render_template("post_form.html", url_css=url_css)
