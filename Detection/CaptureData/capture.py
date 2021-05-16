# -*- coding: utf-8 -*-
"""
Created on Tue May  4 21:30:19 2021

@author: ricky
"""

import numpy as np
from PIL import ImageGrab
import cv2
import time
def main():

    last_time = time.time()
    while(True):
        
        screen = np.array(ImageGrab.grab(bbox =(0,40,800,640)))


        print('Loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window', screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
