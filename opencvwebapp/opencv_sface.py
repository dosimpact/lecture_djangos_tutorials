import cv2
import numpy as np
from django.conf import settings

class process_video:
    def __init__(self,vidname,clear_val=False,unsharp=False):
        self.vidfilename = vidname
        #self.pMOG2=cv2.createBackgroundSubtractorMOG(200,5,0.7,0)
        self.pMOG2=cv2.createBackgroundSubtractorMOG2(40,40,False)
        self.frame=None
        self.fgMaskMOG2=None
        self.clear=clear_val
        self.unsharp=unsharp
 
    def processVideo(self):
        try:
            self.capture = cv2.VideoCapture(self.vidfilename)
            # fps,width,height,codec 가져옴.
            self.full_frame = full =int(self.capture.get(cv2.CAP_PROP_FRAME_COUNT))
            self.frame_width = int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH))
            self.frame_height = int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self.vFourcc = self.capture.get(cv2.CAP_PROP_FOURCC)
            # 기초 코드
 
            #저장 방식
            self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
            self.video = cv2.VideoWriter('Output01.mp4',self.fourcc, 30.0, (self.frame_width,self.frame_height))
            #영상을 다 볼때까지.
            while (int(self.capture.get(1))<full):
                ret,self.frame=self.capture.read()
                self.backgroundImage=None
                self.pMOG2.apply(self.frame)
                cv2.imshow("Before",self.frame)
                #cv2.imshow("Mask01",self.fgMaskMOG2)
 
                self.img1 = None
                self.img2 = None
                ##################################################
                #self.kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,ksize=(5,5))
                #self.kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize=(10, 10))
                #self.fgMaskMOG2 =cv2.erode(self.fgMaskMOG2 ,self.kernel1)
                #self.fgMaskMOG2 =cv2.dilate(self.fgMaskMOG2 ,self.kernel2,)
 
                #kernel = np.ones((15,15), np.uint8)
                #self.fgMaskMOG2 = cv2.morphologyEx(self.fgMaskMOG2, cv2.MORPH_OPEN, kernel)
                #self.fgMaskMOG2 = cv2.morphologyEx(self.fgMaskMOG2, cv2.MORPH_CLOSE, kernel)
                ##################################################
                
                self.backgroundImage=self.pMOG2.getBackgroundImage()
 
                if self.clear==True:
                    test_k = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
                    self.backgroundImage = cv2.filter2D(self.backgroundImage, -1, test_k)
 
                if self.unsharp !=False:
                    #unsharp가 1.5에서 2.5로 들어감, Default가
                    gaussian_3 = cv2.GaussianBlur(self.backgroundImage, (9, 9), 10.0)
                    self.backgroundImage = cv2.addWeighted(self.backgroundImage, self.unsharp, gaussian_3, -0.5, 0, self.backgroundImage)
 
                #cv2.imshow("Filtet", self.img2)
                #cv2.imshow("Mask02",self.fgMaskMOG2)
                #cv2.imshow("Fianlly Result",self.backgroundImage)
                #cv2.imshow("HI2", self.frame)
                #self.video.write(self.backgroundImage)
 
                #if int(self.capture.get(1))%10==0:
                #    cv2.imwrite(filename="./im_data/Picture_%d.png"%(int(self.capture.get(1))//10),img=self.backgroundImage)
        except:
            return -1

a = process_video("Fub.mp4",clear_val=False,)
ret = a.processVideo()

import cv2
 
 
cap = cv2.VideoCapture(0)
#코덱을 설정한다.
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#저장할 동영상 파일명/코덱/ 프레임/ 해상도
writer = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))
 
while True:
    ret,img_color = cap.read()
 
    if ret == False:
        continue
 
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
 
    cv2.imshow("Color", img_color)
    cv2.imshow("Gray", img_gray)
 
    writer.write(img_color)
 
    if cv2.waitKey(1)&0xFF == 27:
        break
 
#자원을 해체
cap.release()
writer.release()


#경로 전달 - 이미지 읽기
def opencv_sface(path):
    
    img = cv2.imread(path, 1)
    if (type(img) is np.ndarray):
        print(img.shape)
        factor = 1
        if img.shape[1] > 640:
            factor = 640.0 / img.shape[1]
        elif img.shape[0] > 480:
            factor = 480.0 / img.shape[0]

        if factor != 1:
            w = img.shape[1] * factor
            h = img.shape[0] * factor
            img = cv2.resize(img, (int(w), int(h)))
        #정적 파일들을 한곳에 모아두는 MEDIA에서 학습된 데이터를 불러온다.
        baseUrl = settings.MEDIA_ROOT_URL + settings.MEDIA_URL
        face_cascade = cv2.CascadeClassifier(baseUrl + 'haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier(baseUrl + 'haarcascade_eye.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        #다시 이미지를 저장..
        print('######## image is wirted --> ', path)
        cv2.imwrite(path, img)

    else:
        print('someting error')
        print(path)