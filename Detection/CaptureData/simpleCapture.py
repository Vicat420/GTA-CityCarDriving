# -*- coding: utf-8 -*-
"""
Created on Tue May  4 22:21:22 2021

@author: ricky
"""
import pyautogui as pag
import time
chemin = "dataGTA/"

def main():
    number = 0
    while(True):
        screen= pag.screenshot()
        name="SC-"+str(number)+'.jpg'
        screen.save(chemin+'SC-'+str(number)+'.jpg')
        print(name+' saved')
        time.sleep(0.2)
        number+=1
    