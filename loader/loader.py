from flask import Blueprint, render_template, request

from utils import search_post, pic_saver, json_dumper

bp_loader = Blueprint('bp_loader', __name__, template_folder='templates')


@bp_loader.route('/post/')
def load_post_page():
    return render_template('post_form.html')


@bp_loader.route('/post/', methods=['POST'])
def download_post_page():
    picture = request.files.get('picture')
    content = request.form.get("content")
    pic_saver(picture)
    pic_path = pic_saver(picture)
    post = json_dumper({'pic': pic_path, "content": content})
    return render_template('post_uploaded.html', post=post)
