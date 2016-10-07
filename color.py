#coding: utf-8

import cv2
import numpy as np
import os
import glob

def personal_color(eye,nose,mouth):
    current_dir = os.path.dirname(__file__)

    roi_eyes = cv2.imread(current_dir+'/static/image/'+str(eye)+'.jpg', cv2.IMREAD_COLOR)
    roi_nose = cv2.imread(current_dir+'/static/image/'+str(nose)+'.jpg', cv2.IMREAD_COLOR)
    roi_mouth = cv2.imread(current_dir+'/static/image/'+str(mouth)+'.jpg', cv2.IMREAD_COLOR)


    def season(roi_parts):
        hue = 0
        saturation = 0
        value = 0

        if roi_parts is False:
            no_parts = roi_parts


        #HSV空間に変換
        hsvcat = cv2.cvtColor(roi_parts, cv2.COLOR_BGR2HSV)

        #切り抜いた画像の中心点
        tyuusin = (hsvcat[hsvcat.shape[0]/2, hsvcat.shape[1]/2]),\
              (hsvcat[hsvcat.shape[0]/2+1, hsvcat.shape[1]/2+1]),\
              (hsvcat[hsvcat.shape[0]/2+1, hsvcat.shape[1]/2-1]),\
              (hsvcat[hsvcat.shape[0]/2-1, hsvcat.shape[1]/2+1]),\
              (hsvcat[hsvcat.shape[0]/2-1, hsvcat.shape[1]/2-1])

        for h,s,v in tyuusin:
            hue += h.astype(np.float64)
            saturation += s.astype(np.float64)
            value += v.astype(np.float64)

            ave_hue = hue/5
            ave_saturation = saturation/5
            ave_value = value/5


        spring = 0
        summer = 0
        autumn = 0
        winter = 0

        #彩度と明度の判定
        if ave_saturation > (255/2) and ave_value > (255/2):
            spring += 1    
        elif ave_saturation < (255/2) and ave_value < (255/2):
            autumn += 1
        elif ave_saturation < (255/2) and ave_value > (255/2):
            summer += 1
        elif ave_saturation > (255/2) and ave_value < (255/2):
            winter += 1

        return spring, autumn, summer, winter


    if type(roi_eyes) != bool:
        spring, autumn, summer, winter = season(roi_eyes)
    else:
        print('目の色判別してないよ')

    if type(roi_nose) != bool:
        spring, autumn, summer, winter = season(roi_nose)
    else:
        print('鼻の色判別してないよ')

    if type(roi_mouth) != bool:
        spring, autumn, summer, winter = season(roi_mouth)
    else:
        print('口の色判別してないよ')


    list = [spring, summer, autumn, winter]
    re_season = max(list)

    if re_season == spring:
        print'春が来た'
    elif re_season == summer:
        print'夏が来た'
    elif re_season == autumn:
        print'秋が来た'
    elif re_season == winter:
        print'冬が来た'


    [os.remove(f) for f in glob.glob(current_dir+'static/image/'+'*.jpg')]
    #import pdb; pdb.set_trace()

