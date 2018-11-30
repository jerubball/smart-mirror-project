
from Tkinter import *
import locale
import threading
import time
import requests
import json
import traceback
import feedparser

import os

from PIL import Image, ImageTk
from contextlib import contextmanager

from scripts.vars import *
from opencv.Facerec import *


class Camera(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')
        self.title = 'Face Info'
        self.cameraLbl = Label(self, text=self.title, font=('Helvetica', medium_text_size), fg="white", bg="black", anchor=N)
        self.cameraLbl.pack(side=TOP, anchor=N)
        #self.labelContainer = Frame(self, bg="black")
        #self.labelContainer.pack(side=TOP, anchor=N)
        self.predict_previous = None
        self.predict_result = None
        self.predict_counter = 4
        self.predict_text = Label(self, text="", font=('Helvetica', medium_text_size), fg="white", bg="black")
        self.predict_text.pack(side=TOP, anchor=CENTER)

        self.textbox = Entry(self)
        self.textbox.pack()
        self.textbox.focus_set()
        #self.button = Button(self,text='okay',command=None)
        #self.button.pack()
        # self.do_loop()
        self.after(5000, self.do_loop)
    
    def do_update(self, event=None):
        self.predict_text.config(text=self.textbox.get())
        self.textbox.delete(0, END)
        #self.textbox.insert(0, "")

    def do_camera(self):
        try:
            # take photo
            # os.system("raspistill -o image.png -k -t 0 -p '350,50,800,600'")
            os.system("raspistill -o image.png -t 1 -p '50,350,800,600'")
            # perform recognition
            self.predict_result = do_prediction_single("image.png")
            if self.predict_result is None:
                self.predict_counter += 1
                if self.predict_counter > 4:
                    self.predict_previous = "Face is not detected"
            else:
                self.predict_previous = self.predict_result
                self.predict_counter = 0
            
            # remove all children
            #for widget in self.labelContainer.winfo_children():
            #    widget.destroy()
            # set new label
            self.predict_text.config(text=self.predict_previous)
            
        except Exception as e:
            traceback.print_exc()
            # print "Error: %s. Cannot get news." % e

    def do_loop(self):
        thread1 = threading.Thread(target=self.do_camera)
        
        # if __name__=="__main__": self = 2
        # self.do_camera
        thread1.start()
        
        # not needed?
        # thread1.join()
        
        self.after(7500, self.do_loop)
        # self.after(10000, self.do_camera)

