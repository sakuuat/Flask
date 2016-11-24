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
    return render_template('index.html', message='Select the face image.')

@app.route('/uploader', methods=['POST'])
def upload_file():
    f = request.files['the_file']
    if cut_img(f) != False:
        cut_img(f)

#       import pdb; pdb.set_trace()
        path = os.path.join(os.path.dirname(__file__),"static/image/")
        image_names = [relpath(img_path, path) for img_path in glob(join(path, '*.jpg'))]
        my_liist = []

        for image in image_names:
            my_dic = {}
            my_dic['image_name'] = 'static/image/' + image
            my_liist.append(my_dic)

        return render_template('cut.html', message='Select the eye,nose and mouth.if no you want use an image,please re-send the face image.', parts=my_liist) 
    else:
        return render_template('index.html', message='Re-select the another face image.')

@app.route('/uploader/select', methods=['POST'])
def select_parts():
    if request.method == 'POST':
        eye = int(request.form['number1'])
        nose = int(request.form['number2'])
        mouth = int(request.form['number3'])
        four_seasons = personal_color(eye, nose, mouth)
    
    if four_seasons == 1:
        return render_template('season_temp.html', base_color='yellow', season='spring')
    elif four_seasons == 2:
        return render_template('season_temp.html', base_color='blue', season='summer')
    elif four_seasons == 3:
        return render_template('season_temp.html', base_color='yellow', season='autumn')
    elif four_seasons == 4:
        return render_template('season_temp.html', base_color='blue', season='winter')

@app.route('/uploader/select/parsonalcolor', methods=['POST'])
def parsonal_color():
    return render_template('index.html', message='Select the face image.')

if __name__ == "__main__":
    app.run()
