import cv2
import numpy as np
from django.conf import settings
import os
import ntpath

#경로 전달 - 이미지 읽기

def opencv_sface(path):
    
    filename, file_extension = os.path.splitext(path) # '/path/to/somefile.ext' -> '/path/to/somefile' '.ext'
    saved_name = ntpath.basename(filename+"_result"+file_extension) #'/path/to/somefile.ext' -> somefile.ext
    print('######## saved_name : ',saved_name)

    capture = cv2.VideoCapture(path)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    fps = int(capture.get(cv2.CAP_PROP_FPS))
    full_frame = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    length = full_frame / fps
    print(fps,full_frame,frame_width,frame_height,length)
    #vfourcc = int(capture.get(cv2.CAP_PROP_FOURCC))

    writer = cv2.VideoWriter(saved_name, fourcc, fps, (frame_width, frame_height))
    pMOG2 = cv2.createBackgroundSubtractorMOG2(40,40,False)
    
    while (int(capture.get(1)) < full_frame):
        ret,img_color = capture.read()
        if ret == False:
            continue
        backgroundImage = pMOG2.getBackgroundImage()
        pMOG2.apply(img_color) 
        #cv2.imshow("Fianlly",img_color)
        writer.write(backgroundImage)
    
"""
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(BASE_DIR,'Car.mp4')
print(BASE_DIR)
print(FILE_DIR)
opencv_sface(FILE_DIR)"""