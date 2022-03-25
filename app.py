from flask import Flask, render_template, send_from_directory, url_for

from loader.views import post_loader
from search.views import search

app = Flask(__name__)
app.config["EXPLAIN_TEMPLATE_LOADING"] = False
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

app.register_blueprint(search)
app.register_blueprint(post_loader)


@app.route("/uploads/<path:path>", methods=["GET"])
def static_dir(path):
    return send_from_directory("uploads", path)


@app.errorhandler(413)
def too_large_file(err):
    url_css = url_for("static", filename="style.css")
    error = f"Превышен максимальный размер файла ({app.config['MAX_CONTENT_LENGTH'] / 1024 / 1024} МБ)"
    return render_template("loader_error.html", url_css=url_css, error=error), 413


app.run(debug=False)
