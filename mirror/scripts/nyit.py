
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
from vars import *


class Nyit(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')
        self.title = 'NYIT Box' # 'News' is more internationally generic
        self.newsLbl = Label(self, text=self.title, font=('Helvetica', medium_text_size), fg="white", bg="black")
        self.newsLbl.pack(side=TOP, anchor=W)
        self.headlinesContainer = Frame(self, bg="black")
        self.headlinesContainer.pack(side=TOP)
        self.get_headlines()

    def get_headlines(self):
        try:
            # remove all children
            for widget in self.headlinesContainer.winfo_children():
                widget.destroy()
            all_events = get_events()
            all_news = get_news()
            for news in all_news[:5]:
                headline = Headline(self.headlinesContainer, news)
                headline.pack(side=TOP, anchor=W)
            # for event in all_events[:5]:
            #     headline = Headline(self.headlinesContainer, event)
            #     headline.pack(side=TOP, anchor=W)
        except Exception as e:
            traceback.print_exc()
            # print "Error: %s. Cannot get news." % e

        self.after(600000, self.get_headlines)
        # self.after(10000, self.get_headlines)


class Headline(Frame):
    def __init__(self, parent, dictionary):
        Frame.__init__(self, parent, bg='black')

        # image = Image.open("assets/Newspaper.png")
        # image = image.resize((25, 25), Image.ANTIALIAS)
        # image = image.convert('RGB')
        # photo = ImageTk.PhotoImage(image)

        # self.iconLbl = Label(self, bg='black', image=photo)
        # self.iconLbl.image = photo
        # self.iconLbl.pack(side=LEFT, anchor=N)

        self.eventName = dictionary["title"]
        self.eventNameLbl = Label(self, text=self.eventName, font=('Helvetica', small_text_size, 'bold'), fg="white",
                                  bg="black")
        self.eventNameLbl.pack(side=LEFT, anchor=N)
        self.eventDate = '[' + dictionary["date"] + ']'
        self.eventDateLbl = Label(self, text=self.eventDate, font=('Helvetica', small_text_size, 'italic'), fg="white",
                                  bg="black")
        self.eventDateLbl.pack(side=LEFT, anchor=S)
