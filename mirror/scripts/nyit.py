from Tkinter import *
import locale
import threading
import time
import requests
import json
import traceback
import feedparser


from nyit_data import *
from vars import *


class NyitNews(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')
        self.title = 'NYIT Box'
        self.newsLbl = Label(self, text=self.title, font=('Helvetica', medium_text_size), fg="white", bg="black", anchor=W)
        self.newsLbl.pack(side=TOP, anchor=W)
        self.headlinesContainer = Frame(self, bg="black")
        self.headlinesContainer.pack(side=TOP, anchor=W)
        self.get_headlines()

    def get_headlines(self):
        try:
            # remove all children
            for widget in self.headlinesContainer.winfo_children():
                widget.destroy()
            all_news = get_news()
            for news in all_news[:5]:
                headline = NyitHeadlineNews(self.headlinesContainer, news)
                headline.pack(side=TOP, anchor=W)
        except Exception as e:
            traceback.print_exc()
            # print "Error: %s. Cannot get news." % e

        self.after(600000, self.get_headlines)
        # self.after(10000, self.get_headlines)


class NyitHeadlineNews(Frame):
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
                                  bg="black", justify=LEFT, anchor=W)
        self.eventNameLbl.pack(side=LEFT, anchor=W)
        self.eventDate = '[' + dictionary["date"] + ']'
        self.eventDateLbl = Label(self, text=self.eventDate, font=('Helvetica', small_text_size, 'italic'), fg="white",
                                  bg="black", justify=LEFT, anchor=W)
        self.eventDateLbl.pack(side=RIGHT, anchor=W)


class NyitEvents(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')
        self.title = 'NYIT Events'
        self.newsLbl = Label(self, text=self.title, font=('Helvetica', medium_text_size), fg="white", bg="black", anchor=W)
        self.newsLbl.pack(side=TOP, anchor=W)
        self.headlinesContainer = Frame(self, bg="black")
        self.headlinesContainer.pack(side=TOP, anchor=W)
        self.get_headlines()

    def get_headlines(self):
        try:
            # remove all children
            for widget in self.headlinesContainer.winfo_children():
                widget.destroy()
            all_events = get_events()
            for event in all_events[:5]:
                headline = NyitHeadlineEvents(self.headlinesContainer, event)
                headline.pack(side=TOP, anchor=W)
        except Exception as e:
            traceback.print_exc()
            # print "Error: %s. Cannot get news." % e

        self.after(600000, self.get_headlines)
        # self.after(10000, self.get_headlines)


class NyitHeadlineEvents(Frame):
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
                                  bg="black", justify=LEFT, anchor=W)
        self.eventNameLbl.pack(side=LEFT, anchor=W)
        self.eventDate = '[' + dictionary["date"] + ']'
        self.eventDateLbl = Label(self, text=self.eventDate, font=('Helvetica', small_text_size, 'italic'), fg="white",
                                  bg="black", justify=LEFT, anchor=W)
        self.eventDateLbl.pack(side=RIGHT, anchor=W)
