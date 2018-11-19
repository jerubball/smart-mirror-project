# welcome screen for user @ middle display

from Tkinter import *
import traceback
from vars import *
from user_profiles import *


class Welcome(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')
        self.title = 'EMPTY'
        self.nameLbl = Label(self, text=self.title, font=('Helvetica', medium_text_size), fg="white", bg="black")
        self.nameLbl.pack(side=TOP, anchor=W)
        self.nameContainer = Frame(self, bg="black")
        self.nameContainer.pack(side=TOP)
        self.get_user()

    def get_user(self):
        try:
            # remove all children
            for widget in self.nameContainer.winfo_children():
                widget.destroy()
            user_data = get_user()
            for user_info in user_data[:5]:
                headline = DisplayUser(self.nameContainer, user_info)
                headline.pack(side=TOP, anchor=W)
        except Exception as e:
            traceback.print_exc()
            # print "Error: %s. Cannot get news." % e

        self.after(600000, self.get_user)
        # self.after(10000, self.get_user)


class DisplayUser(Frame):
    def __init__(self, parent, dictionary):
        Frame.__init__(self, parent, bg='black')

        self.userName = dictionary["name"]
        self.userNameLbl = Label(self, text=self.userName, font=('Helvetica', small_text_size, 'bold'), fg="white",
                                 bg="black")
        self.userNameLbl.pack(side=LEFT, anchor=N)
        self.userBio = '[' + dictionary["bio"] + ']'
        self.userBioLbl = Label(self, text=self.userBio, font=('Helvetica', small_text_size, 'italic'), fg="white",
                                  bg="black")
        self.userBioLbl.pack(side=LEFT, anchor=S)
