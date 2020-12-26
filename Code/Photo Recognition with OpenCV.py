#!/usr/bin/env python
# coding: utf-8

# In[5]:


import PIL
from PIL import Image, ImageDraw, ImageTk
import cv2 as cv


# In[ ]:


cvGrayId = cv.cvtColor(idcardcv, cv.COLOR_BGR2GRAY)
faceCascade = cv.CascadeClassifier('cvdata/haarcascade_frontalface_alt.xml')
faces = faceCascade.detectMultiScale(cvGrayId)


# In[2]:


if faces.size != 0:
    face = faces[0]
    width, height = cvGrayId.shape
    photo = idcard.crop((face[0]-0.05*width,face[1]-0.05*height,(face[0]+face[2])+0.05*width,(face[1]+face[3])+0.05*height))
else:
    photo = 'Photo Not Found'

