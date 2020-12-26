#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
from tkinter import filedialog


# In[2]:


def UploadAction(event=None):
    global filename
    filename = filedialog.askopenfilename(filetypes=[('png images','.png'), ('jpg images','.jpg')])
    print('Selected:', filename)
    root.destroy()
    
root = tk.Tk()
button = tk.Button(root, text='Upload your ID', command=UploadAction)
button.pack()

root.mainloop()


# In[ ]:


root = tk.Tk()
root.title("ID Card Details")
root.minsize(200,200)
root.maxsize(500,500)
tkName = tk.Label(root, text='Names: '+" ,".join(persons))
tkDates = tk.Label(root, text='Dates: '+" ,".join(dob))
tkNumbers = tk.Label(root,text='Numbers: '+ ','.join(numbers))
tkPhoto = ImageTk.PhotoImage(photo.resize((100,100)))
tkPhotoDisplay = tk.Label(image=tkPhoto)
tkPhotoDisplay.image=tkPhoto
closingButton = tk.Button(root, text='Close Window', command=root.destroy)
tkName.pack()
tkDates.pack()
tkNumbers.pack()
tkPhotoDisplay.pack()
closingButton.pack()

root.mainloop()

