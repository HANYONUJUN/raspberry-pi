#!/usr/bin/python

import time
import RPi.GPIO as GPIO

GPIO.setmodde(GPIO.BCM)
GPIO.setup(14, GPIO.IN)

def interrupt_fired(channel):
  print("interrupt_fired")
  print(channel)
GPIO.add_event_detect(14, GPIO.FALLING, callback=interrupt_fired)

while(True):
  time.sleep(1)
  print("Timer Fired")
