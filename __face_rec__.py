#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 23:48:48 2020

@author: antoniofoglia
"""
from cv2 import *
import face_recognition
import json
from __output__ import say
import os
import time
from __input__ import inp
from __recognise__ import recognise

def fr():
    with open('images.json', 'r') as f:
        images = json.load(f)
    #print(images)
    #print('1')
    cam=cv2.VideoCapture(0)
    time.sleep(0.1)
    s, img = cam.read()
    imwrite("pic.jpg",img)
    cam.release()
    name='unknown'
    for i in images:
        #print('images/{}'.format(images[i]))
        known_image = face_recognition.load_image_file('images/{}'.format(images[i]))
        unknown_image = face_recognition.load_image_file("pic.jpg")
        known_encoding = face_recognition.face_encodings(known_image)[0]
        try:
            unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
            results = face_recognition.compare_faces([known_encoding], unknown_encoding)
        except:
            print('Goffredo: "Face not found')
            return
        if results[0] == True :
            name = i
            #os.remove("pic.jpg")
    if name == 'unknown':
        say('Hello, what is your name?','en')
        fname=inp(4,'name')
        text = recognise(fname).lower()
        try:
            li=text.split(' ')
            li.remove('my')
            li.remove('name')
            li.remove('is')
            name = li[0]
        except:
            name=text
        os.rename('pic.jpg','images/{}.jpg'.format(name))
        images[name]='{}.jpg'.format(name)
    #print(name)
    #print(images)
    with open("images.json",'w') as f:
        json.dump(images,f)
    say("Hello, {}!".format(name),'en')
    return
