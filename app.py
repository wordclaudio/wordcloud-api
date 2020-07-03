import os
from flask import Flask, request, session, send_file
from werkzeug.utils import secure_filename
from flask_cors import CORS
from word_cloud import generate_wordcloud_from_chat
import backoff
import logging

UPLOAD_FOLDER = "/tmp/"

app = Flask(__name__)
CORS(app)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def _get_destination(file):
    folder = os.path.join(UPLOAD_FOLDER, "word_cloud")
    if not os.path.isdir(folder):
        os.makedirs(folder, exist_ok=True)
    return "/".join([folder, file])


@app.route("/upload", methods=["POST"])
def file_upload():
    file = request.files["file"]
    uuid = secure_filename(file.filename)
    file.save(_get_destination(uuid) + ".txt")
    generate_word_cloud(uuid)
    return "Done"


def generate_word_cloud(uuid):
    wordcloud = generate_wordcloud_from_chat(_get_destination(uuid))
    wordcloud.to_file(_get_destination(uuid) + ".png")
    logging.info("Word cloud generated")


@backoff.on_exception(backoff.expo, FileNotFoundError)
def send_wordcloud(uuid):
    logging.info("Sending Wordcloud")
    image_file = uuid + ".png"
    path = _get_destination(image_file)
    return send_file(
        path, as_attachment=True, attachment_filename=image_file, mimetype="text"
    )


@app.route("/download")
def download_file():
    uuid = secure_filename(request.args.get("fileName"))
    return send_wordcloud(uuid)


if __name__ == "__main__":
    app.run(debug=True)
