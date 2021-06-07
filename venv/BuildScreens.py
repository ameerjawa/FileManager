from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import tkinter as tk
from Actions import Actions
from Widgets import Widget


#########
#
#
# BuildScreens class with all the UI bullding and use Widgets from Widgets file
#
#
# the button we create in Widgets never used here because it now working from external class its do problems
#
#######



class BuildScreens(object):

    ## main default Settings
    def app():
        root = tk.Tk()
        root.geometry("360x360")
        root.title("FileManager")
        frame = tk.Frame(root, bg='lightblue')
        frame.place(relx=0.2, rely=0.2, relheight=0.6, relwidth=0.6)
        BuildScreens.loginPage(root)




    ## build the login page with the template widgets from Widgets file
    @staticmethod
    def loginPage(window):

        user_name_label = Widget.label(window, "50","Enter userName here")
        user_name_label.place(x=5, y=60)
        username_entry = Widget.entry(window, "30")
        username_entry.place(x=90, y=90)
        password_label = Widget.label(window, "50", "Enter Password")
        password_label.place(x=5, y=120)
        password_entry = Entry(window, width="30", show="*")
        password_entry.place(x=90, y=150)
        login_btn =Button(window,text="Login",command=lambda: BuildScreens.ActionsPage(username_entry.get(),window) if Actions.CheckifCorrectDetails(
                          username_entry.get(), password_entry.get()) == True else messagebox.showerror(
                          message="Wrong email/password"))
        login_btn.place(x=160, y=200)
        window.mainloop()



    ## build Actions page with the template widget from Widgets file
    def ActionsPage(username,window):
        window.destroy()
        window2 = Tk()
        window2.title("FileManagementProgram")
        window2.geometry("360x600")
        window2.iconbitmap("icons\\3123.ico")
        window2.resizable(False, False)
        scrolltext = scrolledtext.ScrolledText(window2, wrap=WORD, width=34, height=5, font=("Times New Roman", 15))
        scrolltext.place(x=0, y=450)
        welcome_username_label = Widget.label(window2, "50", f"Welcome {username}")
        welcome_username_label.place(x=5, y=30)
        actions_text_label = Widget.label(window2, "50", "Actions")
        actions_text_label.place(x=5, y=60)
        enter_two_file_label = Widget.label(window2, "20", "enter 2 files path")
        enter_two_file_label.place(x=10, y=80)
        enter_first_file_entry = Widget.entry(window2, "20")
        enter_first_file_entry.place(x=25, y=100)
        enter_second_file_entry = Widget.entry(window2, "20")
        enter_second_file_entry.place(x=25, y=120)
        copy_action_btn = Button(window2,text="copy first file to second file",command=lambda:  Actions.copyFiletoOther(scrolltext, enter_first_file_entry.get(), enter_second_file_entry.get()))
        copy_action_btn.place(x=160, y=107)
        enter_one_file_label = Label(window2, width="20", text="enter file path")
        enter_one_file_label.place(x=10, y=170)
        enter_first_file_entry_2=Widget.entry(window2, "20")
        enter_first_file_entry_2.place(x=25, y=190)
        delete_btn = Button(window2,text="delete file",command=lambda: Actions.deletefile(scrolltext, enter_first_file_entry_2.get()))
        delete_btn.place(x=160, y=180)
        enter_two_file_label.place(x=10, y=230)
        enter_first_file_entry_3=Widget.entry(window2, "20")
        enter_first_file_entry_3.place(x=25, y=250)
        enter_second_file_entry_2=Widget.entry(window2, "20")
        enter_second_file_entry_2.place(x=25, y=270)
        switch_btn = Button(window2,text="switch text in 2 files",command=lambda:Actions.switch_data_in_files(scrolltext, enter_first_file_entry_3.get(), enter_second_file_entry_2.get()))
        switch_btn.place(x=160, y=260)
        enter_one_file_label.place(x=10, y=310)
        enter_first_file_entry_4=Widget.entry(window2, "20")
        enter_first_file_entry_4.place(x=25, y=330)
        enter_word_label = Widget.label(window2, "20", "enter the word")
        enter_word_label.place(x=10, y=350)
        enter_word_entry=Widget.entry(window2, "20")
        enter_word_entry.place(x=25, y=370)
        delte_word_btn = Button(window2,text="delete word from file",command=lambda: Actions.replaceString(scrolltext, enter_first_file_entry_4.get(), enter_word_entry.get()))
        delte_word_btn.place(x=160, y=350)
        exit_btn = Button(window2,text="exit",command=lambda: Actions.on_exit(window2))
        exit_btn.place(x=160, y=400)
        window2.mainloop()





