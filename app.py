import logging

from flask import Flask, send_from_directory

# from functions import ...
from loader.loader import bp_loader
from main.main import bp_main

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
#регистрирует блупринт
app.register_blueprint(bp_main)
app.register_blueprint(bp_loader)
# логирование
logging.basicConfig(filename='basic.log', level=logging.INFO)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(port=5001)
