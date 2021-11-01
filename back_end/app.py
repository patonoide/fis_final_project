import json
import os
import zipfile

import cv2 as cv
import flask
import numpy as np
from flask import request
from keras import models

app = flask.Flask(__name__)




@app.route('/furry', methods=['GET'])
def test():
    response = app.response_class(
        response=json.dumps({'I am': 'alive'}),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/furry', methods=['POST'])
def scraping():
    padrao = request.form['type']

    if padrao == str(1):
        model = models.load_model('./main_model')
    elif padrao == str(2):
        model = models.load_model('./rotation_model')
    elif padrao == str(3):
        model = models.load_model('./grayscale_model')

    file = request.files['file']
    zip = zipfile.ZipFile(file)
    images = []
    file_names = []

    for file_name in zip.namelist():
        file = zip.read(file_name)
        file_array_np = np.frombuffer(file, np.uint8)
        image = cv.imdecode(file_array_np, cv.IMREAD_COLOR)
        if padrao == str(3):
            image = cv.resize(image, (64, 64), interpolation=cv.INTER_AREA)
            image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            image = image.reshape(64,64,1)
        else:
            image = cv.resize(image, (512, 512), interpolation=cv.INTER_AREA)
        images.append(image)
        file_names.append(file_name)

    labels = model.predict(np.array(images))

    results = []
    for i in range(len(labels)):
        entry = {'name': file_names[i], 'value': str(labels[i][0])}
        results.append(entry)

    response = app.response_class(
            response=json.dumps(results),
            status=200,
            mimetype='application/json'
        )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)


