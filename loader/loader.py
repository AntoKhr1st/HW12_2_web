import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from utils import pic_saver, json_dumper

# создание блупринта
bp_loader = Blueprint('bp_loader', __name__, template_folder='templates')


@bp_loader.route('/post/')
def load_post_page():
    return render_template('post_form.html')


@bp_loader.route('/post/', methods=['POST'])
def download_post_page():
    picture = request.files.get('picture')
    content = request.form.get("content")
    # проверка на наличие контента в форме
    if not picture or not content:
        return "нет коммента или картинки"
    # проверка на расширение картинки
    if picture.filename.split('.')[-1] not in ['jpeg', 'png']:
        logging.error('неверный формат файла')
        return "неверный формат файла"
    try:
        pic_path = pic_saver(picture)
        post = json_dumper({'pic': pic_path, "content": content})
        return render_template('post_uploaded.html', post=post)
    except FileNotFoundError:
        logging.error('файл с постами не найден')
        return 'файл с постами не найден'
    except JSONDecodeError:
        return 'проблема с json файлом'
