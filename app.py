import os
import re
from flask import Flask, render_template, Response, jsonify
from random import choice
import markovify

text = ""

for subdir, dirs, files in os.walk("datasets"):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".txt"):
            # print(filepath)
            with open(filepath) as f:
                text += f.read() + "\n"

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 604800

response = Response()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/generate', methods=['GET'])
def generate():
    text_model = markovify.Text(text.rstrip('\r\n'))
    datasets = [text_model.make_sentence() for i in range(100)]
    datasets = [i for i in datasets if i is not None]
    dataset = choice(datasets)
    return jsonify(
        dataset=dataset
    )

# @app.route("/favicon.ico")
# def favicon():
# 	return app.send_static_file('images/favicon.ico')

# @app.route("/humans.txt")
# def humans():
# 	return app.send_static_file('humans.txt')

# @app.errorhandler(404)
# def page_not_found(error):
# 	return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
