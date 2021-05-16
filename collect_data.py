# -*- coding: utf-8 -*-
"""
Created on Fri May  7 10:35:17 2021

@author: frang
"""
import numpy as np
import cv2
import time
import os
from grabscreen import grab_screen
from getkeys import key_check

def keys_to_output(keys):
    #[A,W,D]
    output = [0,0,0]
    
    if 'Q' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    else:
        output[1] = 1
    return output


file_name = 'training_data_rapport.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name, allow_pickle=True))
else:
    print('File does not exist, starting fresh')
    training_data = []

def main():
    
    #timer
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
    
    last_time = time.time()        
    paused = False
    
    while True:
        if not paused:
            screen = grab_screen(region=(0,40,800,640))
            # print('Frame took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (200,160)) 
            keys = key_check()
            output = keys_to_output(keys)
            training_data.append([screen,output])
            print([output])
            
            if len(training_data) % 50 ==0:
                print(len(training_data))
                np.save(file_name, training_data)
                    
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
            
        keys = key_check()

        #pause
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                
                time.sleep(1)


