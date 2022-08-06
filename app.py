from flask import Flask, request, render_template, send_from_directory
# from functions import ...
from loader.loader import bp_loader
from main.main import bp_main
from utils import search_post

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.register_blueprint(bp_main)
app.register_blueprint(bp_loader)


@app.route("/list")
def page_tag():
    pass


@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    pass


@app.route("/post", methods=["POST"])
def page_post_upload():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(port=5001)
