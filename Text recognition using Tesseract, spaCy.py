#!/usr/bin/env python
# coding: utf-8

# In[5]:


from PIL import Image, ImageDraw, ImageTk
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
import numpy as np
import nltk
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()


# In[ ]:


def binarize(image, threshold):
    output = image.convert('L')
    output = output.point(lambda x: x > threshold and 255)
    return output


# In[2]:


idcardcv = cv.imread(filename)
idcard = Image.open(filename)

display(idcard)


# In[4]:


grayId = idcard.convert('L')
defaultBinarizedId = idcard.convert('1')
binarizedIds = [binarize(grayId, threshold) for threshold in np.linspace(0,255,4)]

ids = [grayId] + binarizedIds + [defaultBinarizedId]


# In[ ]:


texts = [pytesseract.image_to_string(idc) for idc in ids]
recognizers = [nlp(text) for text in texts]
labellist = [dict([(str(x), x.label_) for x in recognizer.ents]) for recognizer in recognizers]
persons=[]
dates=[]
orgs=[]
cardinals=[]
for dic in labellist:
    for x in dic.keys():
        if dic[x] == 'PERSON':
            persons.append(x.strip())
        if dic[x] == 'DATE':
            dates.append(x.strip())
        if dic[x] == 'ORG':
            orgs.append(x.strip())
        if dic[x] == 'CARDINAL':
            cardinals.append(x.strip())
persons = list(set([x for x in persons if len(x)>7]))
dob = list(set([x for x in dates if '-' in x or '/' in x or ',' in x]))
numbers = list(set([x for x in dates if (len(x)>3 and x not in dob)] + [x for x in cardinals if (len(x)>3 and x not in dob)]))


# In[ ]:




