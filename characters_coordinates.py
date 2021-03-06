# -*- coding: utf-8 -*-
"""characters_coordinates.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MlY_RjHQPh6AnFheVvnTmKwEa0g2Y3Za
"""

# Python code to find the co-ordinates of
# the contours detected in an image.
import numpy as np
import cv2
from google.colab.patches import cv2_imshow

font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.imread('/content/drive/MyDrive/ocr_images/ROI_5.jpeg', cv2.IMREAD_COLOR)
gray_scale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray_scale,(5,5),0)
edged = cv2.Canny(blurred,50,150)
contours,_ = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours :
  
    approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
  
    # draws boundary of contours.
    cv2.drawContours(img, [approx], 0, (0, 255,0), 5) 
  
    # Used to flatted the array containing
    # the co-ordinates of the vertices.
    n = approx.ravel() 
    i = 0
  
    for j in n :
        if(i % 2 == 0):
            x = n[i]
            y = n[i + 1]
  
            # String containing the co-ordinates.
            string = str(x) + " " + str(y) 
  
            if(i == 0):
                # text on topmost co-ordinate.
                cv2.putText(img, string, (x, y),
                                font, 0.5, (255, 0, 0)) 
            #else:
                # text on remaining co-ordinates.
                #cv2.putText(img, string, (x, y), 
                         # font, 0.5, (255, 0, 0)) 
        i = i + 1


cv2_imshow(img)

