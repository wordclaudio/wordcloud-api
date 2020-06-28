import os
from flask import Flask, request, session, send_file
from werkzeug.utils import secure_filename
from flask_cors import CORS
from word_cloud import generate_wordcloud_from_chat

UPLOAD_FOLDER = "/tmp/"

app = Flask(__name__)
CORS(app)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/upload", methods=["POST"])
def file_upload():
    target = os.path.join(UPLOAD_FOLDER, "word_cloud")
    if not os.path.isdir(target):
        os.mkdir(target)
    file = request.files["file"]
    filename = secure_filename(file.filename)
    destination = "/".join([target, filename])
    file.save(destination + ".txt")
    return "Done."


def generate_word_cloud(filename):
    destination_folder = os.path.join(UPLOAD_FOLDER, "word_cloud")
    path = "/".join([destination_folder, filename])
    generate_wordcloud_from_chat(path)
    return "WordCloud Generated"


@app.route("/download")
def download_file():
    uuid = secure_filename(request.args.get("fileName"))
    destination_folder = os.path.join(UPLOAD_FOLDER, "word_cloud")
    image_file = uuid + ".png"
    path = "/".join([destination_folder, image_file])
    return send_file(
        path, as_attachment=True, attachment_filename=image_file, mimetype="text"
    )


if __name__ == "__main__":
    app.run(debug=True)
