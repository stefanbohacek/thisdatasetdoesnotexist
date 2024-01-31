import os
from random import choice
from flask import Blueprint, jsonify
import markovify

generate_blueprint = Blueprint('generate_blueprint', __name__)

text = ""

for subdir, dirs, files in os.walk("datasets"):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".txt"):
            # print(filepath)
            with open(filepath) as f:
                text += f.read() + "\n"

@generate_blueprint.route('/generate')
def generate():
    text_model = markovify.Text(text.rstrip('\r\n'))
    datasets = [text_model.make_sentence() for i in range(100)]
    datasets = [i for i in datasets if i is not None]
    dataset = choice(datasets)
    return jsonify(
        dataset=dataset
    )
