from tkinter import *


#######
#
# Widget class with all the templates we used in the BuildScreens
#
#####

class Widget(object):



      # build Label template from tkinter
    def label(window,width,text):

       return Label(window, width=width, text=text)

      # build entry template from tkinter
    def entry(window,width):
       return Entry(window, width=width)

      # build button template from tkinter
    def button(window,text,function):
         Button(window,text=text,command=lambda: function)