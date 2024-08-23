#detect motion 5 times and give an alert

import smtplib
from notifypy import Notify
import numpy as np
import cv2
from mss import mss
from PIL import ImageGrab
import time
from datetime import datetime

count=0

time.sleep(3)

while(1):
    #capture images in the specified coordinates with a gap of 1 second and convert images to greyscale
    img1 = ImageGrab.grab(bbox=(100,0,400,300))
    img1= cv2.cvtColor(np.array(img1), cv2.COLOR_RGB2GRAY)
    time.sleep(1)
    img2 = ImageGrab.grab(bbox=(100,0,400,300))
    img2= cv2.cvtColor(np.array(img2), cv2.COLOR_RGB2GRAY)
    
    #take the difference between the greyscaled images
    a=cv2.absdiff(img1,img2)
    
    #driver for alert
    if np.any(a) and count<5:
        count=count+1
    elif np.any(a) and count>=5:
        #get current time and define alert
        now=str(datetime.now())
        alert=Notify()
        alert.title="title"
        alert.message=now
        alert.icon=r"""D:\plants and pokie\pokemon fire red\Pokemon Orange Generation\Pokemon Dragonstone_01.png"""
        alert.send()
        break
