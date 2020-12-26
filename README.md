# IdScanner

Id Card Scanner using Python with Libraries PILLOW, Tesseract, OpenCV, spaCy, tkinter

This is a beginner project made by me to scan ID cards using photo and text recognition.

## Input

The tkinter graphical user interface is used to ask the user to choose the file to upload (either in .png or .jpg format).

![image](https://user-images.githubusercontent.com/71396561/103150248-4b5e3b80-4798-11eb-806a-b0d4240ac341.png)

After the file is selected, the path to file is outputted and the image is displayed. 

![image](https://user-images.githubusercontent.com/71396561/103150845-0937f880-479e-11eb-80f7-70a784370fde.png)

Using the Pillow library, the ID card is grayscaled as well as converted to four different binarized versions with different threshold values. All these versions are stored in an array.

## Text and Image Recognition

Using Tesseract OCR, the text is read from all the versions of the id. The NLP Library, spaCy is used to identify the names, dates and important numbers present on the ID card. These are then put into their own containers.

The OpenCV facial recognition haar cascades are used to recognise the photo present on the ID card, and return the photo. A text message of 'Photo Not found' is returned if the learner fails to recognize any faces on the ID card.

## Output

Again, the tkinter GUI is used to produce an output window. The window contains the names, dates and important numbers present on the ID card. Additionally, it also displays the face present on the ID card.

![image](https://user-images.githubusercontent.com/71396561/103150916-ec4ff500-479e-11eb-9498-79891300fb88.png)
