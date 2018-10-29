

from Tkinter import *
import locale
import threading
import time
import requests
import json
import traceback
import feedparser


from nyit_events import *
from nyit_news import *


class Nyit(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')
        self.title = 'News' # 'News' is more internationally generic
        self.newsLbl = Label(self, text=self.title, font=('Helvetica', medium_text_size), fg="white", bg="black")
        self.newsLbl.pack(side=TOP, anchor=W)
        self.headlinesContainer = Frame(self, bg="black")
        self.headlinesContainer.pack(side=TOP)
        self.get_headlines()

    def get_headlines(self):
        try:
            get_events()
        except Exception as e:
            traceback.print_exc()
            #print "Error: %s. Cannot get news." % e

        self.after(600000, self.get_headlines)

