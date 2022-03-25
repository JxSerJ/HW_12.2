from flask import Blueprint, render_template, url_for, request
from datetime import datetime

from loader.functions import add_post_into_json
from config import POST_PATH
from loader.config import ALLOWED_EXTENSIONS

post_loader = Blueprint("post_loader", __name__, template_folder="loader_templates")

error = None


@post_loader.route("/post", methods=["GET"])
def loader_page():
    url_css = url_for("static", filename="style.css")
    return render_template("post_form.html", url_css=url_css)


@post_loader.route("/post", methods=["POST"])
def load_post_page():
    url_css = url_for("static", filename="style.css")

    global error

    picture = request.files.get("picture")
    if picture:
        file_name_extension = picture.filename.split(".")[-1]
        if file_name_extension in ALLOWED_EXTENSIONS:
            picture_name = picture.filename[:-len(file_name_extension) - 1]
            file_full_name = f"{picture_name}_{datetime.now().strftime('%d%m%Y_%H%M%S')}.{file_name_extension}"

            url_pic = f"./uploads/images/{file_full_name}"
            try:
                picture.save(f"./uploads/images/{file_full_name}")
            except:
                error = "Данные не загружены"
                return render_template("loader_error.html", url_css=url_css, error=error)
            else:
                post_content = request.form.get("content")
                add_post_into_json(POST_PATH, (url_pic, post_content))
                return render_template("post_uploaded.html", url_css=url_css, post_content=post_content,
                                       url_pic=url_pic)
        else:
            error = f"Тип файла недопустим. Допустимые типы файлов: {', '.join(ALLOWED_EXTENSIONS)}"
    else:
        error = "Файл не загружен"

    return render_template("loader_error.html", url_css=url_css, error=error)
