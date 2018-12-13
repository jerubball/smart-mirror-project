
from Tkinter import *
import locale
import threading
import time
import requests
import json
import traceback
import feedparser
import cv2

import os
import RPi.GPIO as GPIO
import random

from PIL import Image, ImageTk
from contextlib import contextmanager

from scripts.vars import *
from opencv.Facerec import *

photo_delay = 5000

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

class Camera(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')
        self.title = 'Face Info'
        self.cameraLbl = Label(self, text=self.title, font=('Helvetica', medium_text_size), fg="white", bg="black", anchor=N)
        self.cameraLbl.pack(side=TOP, anchor=N)
        self.predict_previous = None
        self.predict_result = None
        self.list = []
        self.list_limit = 3
        self.predict_text = Label(self, text="", font=('Helvetica', medium_text_size), fg="white", bg="black")
        self.predict_text.pack(side=TOP, anchor=CENTER)
        
        self.inputContainer = Frame(self, bg="black")
        self.inputContainer.pack(side=TOP, anchor=N)
        self.hold = False
        
        with open("preference.json") as file:
            self.preference = json.load(file)
        
        #self.textbox = Entry(self)
        #self.textbox.pack()
        #self.textbox.focus_set()
        #self.button = Button(self,text='okay',command=None)
        #self.button.pack()
        # self.do_loop()
        
        #self.cap = cv2.VideoCapture(0)
        self.after(photo_delay, self.do_loop)
    
    def do_update(self, event=None):
        #self.predict_text.config(text=self.textbox.get())
        #self.textbox.delete(0, END)
        #self.textbox.insert(0, "")
        pass
    
    def do_reset(self, event=None):
        self.list = []
        self.predict_previous = "Face is not Detected"
        self.predict_result = "Face is not Detected"
        self.predict_text.config(text=self.predict_previous)
        for widget in self.inputContainer.winfo_children():
                            widget.destroy()
    def do_hold(self, event=None):
        self.hold = not self.hold

    def do_camera(self):
        try:
            # take photo
            # os.system("raspistill -o image.png -k -t 0 -p '50,350,800,600'")
            GPIO.output(18,GPIO.HIGH)
            os.system("raspistill -o image.jpg -t 1 -vf -p '0,600,400,300'")
            GPIO.output(18,GPIO.LOW)
            #os.system("raspistill -o image.png -t 1 -n -vf  -hf")
            #os.system("raspistill -o image.png -t 50 -n -vf")
            
            #state = False
            #while not state:
            #    state, frame = self.cap.read()
            #os.system("rm -f image.jpg")
            #frame = cv2.flip(frame, 0)
            #cv2.imwrite("image.jpg", frame)
            
            # perform recognition
            #self.predict_result = do_prediction_single(frame)
            self.predict_result = do_prediction_single_file("image.jpg")
            
            # do correction
            if len(self.list) > self.list_limit:
                self.list = self.list[1:]
                
            if self.predict_result is None:
                self.list.append(None)
                if reduce(lambda x, y : x and y is None, self.list, True):
                    self.predict_previous = "Face is not detected"
                    # remove all children
                    for widget in self.inputContainer.winfo_children():
                        widget.destroy()
            else:
                self.list.append(self.predict_result)
                if self.predict_result in self.list[:-1]:
                    state = self.predict_previous == self.predict_result
                    self.predict_previous = self.predict_result
                    # Detected person.
                    
                    if not state:
                        # remove all children
                        for widget in self.inputContainer.winfo_children():
                            widget.destroy()
                        # set new button
                        if self.predict_result in self.preference:
                            item = random.choice(self.preference[self.predict_result])
                            button = Button(self.inputContainer, text=item['label'], font=('Helvetica', medium_text_size), fg="black", bg="white", command=lambda: os.system("chromium-browser " + item['url']))
                            button.pack(side=TOP, anchor=CENTER)
                else:
                    self.predict_previous = "Face is detected, confirming. Stay still..."
            self.predict_text.config(text=self.predict_previous)
            
        except Exception as e:
            traceback.print_exc()
            # print "Error: %s. Cannot get news." % e

    def do_loop(self):
        if not self.hold:
            thread1 = threading.Thread(target=self.do_camera)
            
            # if __name__=="__main__": self = 2
            # self.do_camera
            thread1.start()
            
            # not needed?
            # thread1.join()
        
        self.after(photo_delay, self.do_loop)
        # self.after(10000, self.do_camera)

