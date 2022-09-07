import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from functions import save_picture, function_add_post

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates_names')


@loader_blueprint.route('/post/')
def add_post_page():
    return render_template('post_form.html')


@loader_blueprint.route('/post/', methods=['POST'])
def add_post():
    picture = request.files.get('picture')
    content = request.form.get('content')
    if not picture or not content:
        return 'Нет картинки и/или текста'
    if picture.filename.split('.')[-1] not in ['jpeg', 'png', 'jpg']:
        return 'Неверное расширение файла'
    try:
        picture_path: str = '/' + save_picture(picture)
    except FileNotFoundError:
        logging.info('Файл не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        return "Невалидный файл"
    post: dict = function_add_post({'pic': picture_path, 'content': content})
    return render_template('post_uploaded.html', post=post)

