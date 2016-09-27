# coding:utf-8
import cv2
import numpy
from flask import Flask, render_template, request
from cut_parts import cut_img 
import glob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message='Hello')

@app.route('/uploader', methods=['POST'])
def upload_file():
   # if request.method == 'POST':
    f = request.files['the_file']
    cut_img(f)

    
    return 'pass'

        

if __name__ == "__main__":
    app.run()
