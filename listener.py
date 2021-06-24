from grabscreen import grab_screen
import numpy as np
import os,sys
import cv2
import pytesseract
import time


#tesseract exec path
pytesseract.pytesseract.tesseract_cmd = os.path.dirname(os.path.realpath(__file__))+'/Tesseract-OCR/tesseract.exe'

#keyword that should exist in notifictn
key=sys.argv[-1]


#set this None for fullscreen
notificarea=(1920-500, 1080-500, 1920, 1080)
#notificarea=None

#get screen s -> screen capture, so -> old screen capture 
s=grab_screen(notificarea)
so=s

#if workin on a file look for a notification
workin=False

while True:
    #if not workin on a file get a file, post url and set workin true
    if not workin:
        #get file and post url
        #if file:
        workin=True
    
    else:
        so=s
        s=grab_screen(notificarea)
        #computin diff
        difference = cv2.subtract(s, so)
        #lookin fo indexes
        ys,xs=np.where(np.sum(np.abs(difference),axis=-1))
        if len(xs) and len(ys):
            #calculatin window
            xmin,xmax=np.min(xs),np.max(xs)
            ymin,ymax=np.min(ys),np.max(ys)
            #if window is big enaug
            if(xmax-xmin>50 and ymax-ymin>50):
                #geddin window from last screenshot
                frame=s[ymin:ymax,xmin:xmax]
                #lookin for keyword
                text=pytesseract.image_to_string(frame)
                #did we just find what we lookin fo
                if(key in text):
                    #yesss
                    print(text)
                    #cv2.imwrite("{}.jpg".format(time.time()),frame)
                    #send post data
                    
                    #job is done
                    workin=False
                    
    #chill
    time.sleep(0.1)
