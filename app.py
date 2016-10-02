# coding:utf-8
import cv2
import numpy
from glob import glob
import os
from flask import Flask, render_template, request
from cut_parts import cut_img
from os.path import join, relpath

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message='Hello')

@app.route('/uploader', methods=['POST', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        cut_img(f)

#    import pdb; pdb.set_trace()
    path = "./static/image"
    image_names = [relpath(img_path, path) for img_path in glob(join(path, '*.jpg'))]
    my_liist = []
    for image in image_names:
        my_dic = {}
        my_dic['image_name'] = 'static/image/' + image
        my_liist.append(my_dic)
    return render_template('index.html', message = my_liist) 


if __name__ == "__main__":
    app.run()
