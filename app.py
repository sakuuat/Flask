# coding:utf-8
import cv2
import numpy
from glob import glob
import os
from flask import Flask, render_template, request
from cut_parts import cut_img
from color import personal_color
from os.path import join, relpath

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message='Select the face image')

@app.route('/uploader', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        cut_img(f)

#    import pdb; pdb.set_trace()
    path = os.path.join(os.path.dirname(__file__),"static/image/")
    image_names = [relpath(img_path, path) for img_path in glob(join(path, '*.jpg'))]
    my_liist = []
    for image in image_names:
        my_dic = {}
        my_dic['image_name'] = 'static/image/' + image
        my_liist.append(my_dic)
    return render_template('cut.html', message='Select the eye,nose and mouth', parts=my_liist) 

@app.route('/uploader/select', methods=['POST'])
def select_parts():
    if request.method == 'POST':
        eye = int(request.form['number1'])
        nose = int(request.form['number2'])
        mouth = int(request.form['number3'])

        personal_color(eye, nose, mouth)

    return render_template('index.html', message='Select the face image')

if __name__ == "__main__":
    app.run()
