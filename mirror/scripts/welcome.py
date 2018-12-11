# welcome screen for user @ middle display
import tkFont
from Tkinter import *
import traceback
from vars import *
# from user_profiles import *
from train_time import *


class Welcome(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')
        self.title = station_name
        self.nameLbl = Label(self, text=self.title, font=('Helvetica', medium_text_size), fg="white", bg="black", anchor=E)
        self.nameLbl.pack()
        # clone the font, set the underline attribute,
        # and assign it to our widget
        f = tkFont.Font(self.nameLbl, self.nameLbl.cget("font"))
        f.configure(underline=True)
        self.nameLbl.configure(font=f)
        self.nameLbl.pack(side=TOP, anchor=E)
        self.nameContainer = Frame(self, bg="black")
        self.nameContainer.pack(side=TOP, anchor=E)
        self.local_trains()

    def local_trains(self):
        try:
            # remove all children
            for widget in self.nameContainer.winfo_children():
                widget.destroy()
            train_data = arriving_trains()
            for train_info in train_data[:5]:
                headline = DisplayLocalTrains(self.nameContainer, train_info)
                headline.pack(side=TOP, anchor=E)
        except Exception as e:
            traceback.print_exc()
            # print "Error: %s. Cannot get news." % e

        self.after(600000, self.local_trains)
        # self.after(10000, self.get_user)


class DisplayLocalTrains(Frame):
    def __init__(self, parent, dictionary):
        Frame.__init__(self, parent, bg='black')

        self.trainTime = dictionary["train_times"]
        self.trainTimeLbl = Label(self, text=self.trainTime, font=('Helvetica', small_text_size, 'bold'), fg="white",
                                  bg="black", justify=RIGHT, anchor=E)
        self.trainTimeLbl.pack(side=RIGHT, anchor=E)
        self.trainName = dictionary["train_names"]
        self.trainNameLbl = Label(self, text=self.trainName, font=('Helvetica', small_text_size, 'bold'), fg="white",
                                  bg="black", justify=RIGHT, anchor=E)
        self.trainNameLbl.pack(side=RIGHT, anchor=E)
