
"""
Created on Tue May 11 06:23:28 2021

@author: ricky
"""
import cv2
import numpy as np
from PIL import Image


img = cv2.imread("dataGTA/SC-981.jpg")

rows,cols,_ = img.shape
print("Rows",rows)
print("Cols",cols)
imgR = img[25: 200,700: 800]
cv2.imshow("imageR",imgR)



#Region of interest
cv2.rectangle(img,(680,25),(1380,400),(0,255,0))
  
  
cv2.imshow("image",img)
cv2.waitKey(0)

chemin="data/"
nbrimg = 5297
def main():
    for k in range(0,nbrimg):
        img = cv2.imread("dataGTA/SC-"+str(k)+".jpg")
        imgR = img[25:200,700:800]
        cv2.imwrite(chemin+"SCR-"+str(k)+".jpg",imgR)
        print(chemin+"SCR-"+str(k)+".jpg")
    