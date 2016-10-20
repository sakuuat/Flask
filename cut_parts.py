#coding: utf-8

import os
import cv2
import numpy

def cut_img(img):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_mcs_righteye.xml')
    nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
    mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

    # OpenCVで読み込む為に一度保存。
    current_dir = os.path.dirname(__file__)
    img.save(os.path.join(current_dir, img.filename))
    filename = img.filename
    
    img = cv2.imread(os.path.join(current_dir, img.filename), cv2.IMREAD_COLOR)
    os.remove(os.path.join(current_dir, filename))

    if(img is None):
        return False

    else:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray)

        if type(face) is tuple:
            return False

        i=0

        #切り抜いて格納
        for (x,y,w,h) in face:
            roi_gray = gray[y:y+h, x:x+w]
            roi_face = img[y:y+h, x:x+w]


            #ここを調整したら正確性が上がる！    
            eyes = eye_cascade.detectMultiScale(roi_gray)
            nose = nose_cascade.detectMultiScale(roi_gray)
            mouth = mouth_cascade.detectMultiScale(roi_gray)

        if type(eyes) is tuple:
            roi_eyes = False
        else:
            for (ex,ey,ew,eh) in eyes:
                i+=1
                cv2.imwrite(current_dir+'/static/image/'+str(i)+'.jpg', roi_face[ey:ey+eh,ex:ex+ew])

        if type(nose) is tuple:
            roi_nose = False
        else:
            for (nx,ny,nw,nh) in nose:
                i+=1
                cv2.imwrite(current_dir+'static/image/'+str(i)+'.jpg', roi_face[ny:ny+nh, nx:nx+nw])

        if type(mouth) is tuple:
            roi_mouth = False
        else:
            for (mx,my,mw,mh) in mouth:
                i+=1
                cv2.imwrite(current_dir+'static/image/'+str(i)+'.jpg', roi_face[my:my+mh, mx:mx+mw])

#import pdb; pdb.set_trace()
