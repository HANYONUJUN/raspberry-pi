#!/usr/bin/python3

import time
import RPi.GPIO as GPIO
import requests, json
from influxdb import InfluxDBClient as influxdb
# 파일 생성 시 import하는 부분을 파일 이름과 똑같이 짓지 말 것
# 서로 충돌이나 오류를 잡기 힘들어지기 때문

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)

def interrupt_fired(channel):
    print("interrupt Fired")
    a = 5
    data = [{
        'measurement' : 'pir',        
        'tags':{
            'VisionUni' : '2410',
        },
        'fields':{
            'pir' : a,
        }
    }]
    client = None
    try:
        client = influxdb('localhost',8086,'root','root','pir')
    except Exception as e:
        print("Exception" + str(e))
    if client is not None:
        try:
            client.write_points(data)
        except Exception as e:
            print("Exception write " + str(e))
        finally:
            client.close()
    print(a)
GPIO.add_event_detect(14, GPIO.FALLING, callback=interrupt_fired)

while(True):
    time.sleep(1)
    a = 1
    data = [{
        'measurement' : 'pir',        
        'tags':{
            'VisionUni' : '2410',
        },
        'fields':{
            'pir' : a,
        }
    }]
    client = None
    try:
        client = influxdb('localhost',8086,'root','root','pir')
    except Exception as e:
        print ("Exception" + str(e))
    if client is not None:
        try:
            client.write_points(data)
        except Exception as e:
            print("Exception write " + str(e))
        finally:
            client.close()
    print("running influxdb OK")
