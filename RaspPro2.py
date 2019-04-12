# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 08:54:40 2019

@author: Antwi Kwaku Ebenezer
"""

"""
Input/Otput pins are 3, 5 and 7

"""
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3,GPIO.OUT)


while True:  """ Forever loop"""
GPIO.output(3,GPIO.HIGH)  #turn on
time.sleep(3)
GPIO.output(3,GPIO.LOW)   # turn off
time.sleep(3)   #sleep 3s


GPIO.setup(5,GPIO.OUT)
while True:
 GPIO.output(5,GPIO.HIGH)  #turn on
 time.sleep(3)  #sleep 3s
 GPIO.output(5,GPIO.LOW)  # turn off
 time.sleep(3)  #sleep 3s


GPIO.setup(7,GPIO.OUT)
while True:
 GPIO.output(7,GPIO.HIGH)

 time.sleep(1)

 GPIO.output(7,GPIO.LOW)
 time.sleep(1)







GPIO.cleanup()