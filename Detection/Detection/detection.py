# -*- coding: utf-8 -*-
"""
Created on Wed May 12 01:42:22 2021

@author: ricky
"""

import cv2

traffic_light_cascade =cv2.CascadeClassifier("haar_xml_07_19.xml")

import numpy as np
from time import time
import win32gui
import win32ui
import win32con

def window_capture():

    
    w = 1920 
    h = 1080
    
    hwnd = win32gui.FindWindow(None, 'Grand Theft Auto V')

    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)
    
    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape=(h,w,4)
    #dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
    
    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    
    
    img = img[...,:3]
    
    return img
    
    

def main():
    loop_time = time()
    while(True):
        
        
        screenshot = window_capture()
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot,cv2.COLOR_RGB2BGR)
        
        

        print('FPS {}'.format(1/(time()-loop_time)))
        loop_time = time()
        traffic_light = traffic_light_cascade.detectMultiScale(screenshot, scaleFactor=1.5, minNeighbors=1)
        
        
        for x,y,w,h in traffic_light:
            print(traffic_light)
            cv2.rectangle(screenshot,(x,y),(x+w,y+h),(0,255,0),2)
        
        cv2.imshow('window', screenshot)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
