import json


def post_from_json():
    '''возвращает список постов из файла'''
    with open('posts.json', 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def search_post(text_in_post):
    posts_with_str = []
    all_posts = post_from_json()
    for post in all_posts:
        if text_in_post.lower() in post['content'].lower():
            posts_with_str.append(post)
    return posts_with_str


def pic_saver(picture):
    '''сохраняет фоточку в папку uploads/images'''
    filename = picture.filename
    path = f'/uploads/images/{filename}'
    picture.save('.'+path)
    return path


def json_dumper(post):
    "обновляет json файл"
    data = post_from_json()
    data.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(data, file,ensure_ascii=False)
    return post
