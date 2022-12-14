import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from utils import search_post

bp_main = Blueprint('bp_main', __name__, template_folder='templates')


@bp_main.route('/')
def main_page():
    return render_template('index.html')


@bp_main.route('/search/')
def search_page():
    # запрос значения query параметра из формы (название переменной из html)
    text_to_search = request.args.get('s')
    logging.info('выполнение поиска')
    try:
        post_list = search_post(text_to_search)
        return render_template('post_list.html', post_list=post_list, text_to_search=text_to_search)
    except FileNotFoundError:
        logging.error('файл с постами не найден')
        return 'файл с постами не найден'
    except JSONDecodeError:
        return 'проблема с json файлом'
