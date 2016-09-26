# coding:utf-8
#app.py
from flask import Flask, render_template, request
from kiritori import cut_img 
import cv,numpy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message='Hello')

@app.route('/uploader', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        kiritori.cut_img(f)

        

if __name__ == "__main__":
    app.run()
