from BuildScreens import BuildScreens
from tkinter import *
from tkinter import scrolledtext
import time
import os

import tkinter as tk


root=tk.Tk()
root.geometry("360x360")

frame=tk.Frame(root,bg='lightblue')
frame.place(relx=0.2,rely=0.2,relheight=0.6,relwidth=0.6)





def on_exit(window2):
    label = Label(window2, width="50", text="Thank you for using our file management program Exiting...")
    label.place(x=5, y=420)
    response=messagebox.askyesno('Exit','Are you sure you want to exit?')
    if response:
        window2.destroy()




def copyFiletoOther(text,file1path,file2path):
    try:
        file1name=os.path.basename(file1path)
        file2name=os.path.basename(file2path)

        if os.path.isfile(file1path) and os.path.isfile(file2path):

            if os.path.exists(file1path) and os.path.exists(file2path):
                    if os.stat(file1path).st_size != 0:
                        with open(file1path) as f:
                           with open(file2path, "a") as f1:
                               for line in f:
                                      f1.write(line)
                               showresult(text,file2path)
                           print("i am a succesfull person")
                    else:
                            print("the first file is Empty!!")
            else:
                    print("File does not exists check the path please!!")
        else:
                print("its not a File!!")
    except IOError as x:
        if x.errno == errno.ENOENT:
            print(file1name, '- does not exist')
        elif x.errno == errno.EACCES:

            print(file1name, '- cannot be read')
        elif x.errno == errno.EACCES:
              print(file2name, 'no perms')
        else:
             print(file1name, '- some other error')

def showresult(text,file2path):
    text.delete("1.0", END)
    x = open(file2path, "r")
    text.insert(END, x.read())

    # for line in open(file1path, "r").readlines():  # Read the lines
    #     login_info = line.split()
    # ip = os.popen(f"cd {file1path}")

def deletefile(filepath):
        try:
                if os.path.exists(filepath):
                            os.remove(filepath)
                else:
                        print("file does not Exists check the filepath!!")


        except:
               print("something went wrong")


def switch_data_in_files(file1path,file2path):

    try:
        if os.access(file1path,os.W_OK)and os.access(file1path,os.R_OK) or os.access(file2path,os.W_OK) and os.access(file2path,os.R_OK):

                lines = []
                with open(file1path, "r") as f1:
                    for line in f1:
                        lines.append(line.__str__())
                with open(file2path, "r") as f:
                    with open(file1path, "w") as f1:
                        for line in f:
                            f1.write(line)
                with open(file2path, "w") as f:
                    for line in lines:
                        print(line)
                        f.write(line)
    except:
        print("something went wrong!!")


def replaceString(filepath,word):

    with open(filepath, "r") as f:
        data = f.read()
        with open(filepath, "w") as f:
            f.write(data.replace(word.lower(), ""))





def ActionsPage(username):
        root.destroy()
        window2 = Tk()
        window2.title("FileManagementProgram")
        window2.geometry("360x520")
        window2.iconbitmap("3123.ico")
        window2.resizable(False, False)
        label = Label(window2, width="50", text=f"Welcome {username}")
        label.place(x=5, y=30)
        label = Label(window2, width="50", text="Actions ")
        label.place(x=5, y=60)
        label = Label(window2, width="20", text="enter 2 files path")
        label.place(x=10, y=80)
        entry3 = Entry(window2, width="20")
        entry3.place(x=25, y=100)
        entry4 = Entry(window2, width="20")
        entry4.place(x=25, y=120)
        btn4 = Button(window2, text="copy first file to second file", command=lambda: copyFiletoOther(textto,entry3.get(),entry4.get()))
        btn4.place(x=160, y=107)
        label = Label(window2, width="20", text="enter file path")
        label.place(x=10, y=170)
        entry5 = Entry(window2, width="20")
        entry5.place(x=25, y=190)
        btn5 = Button(window2, text="delete file", command=lambda: deletefile(entry5.get()))
        btn5.place(x=160, y=180)
        label = Label(window2, width="20", text="enter 2 files path")
        label.place(x=10, y=230)
        entry6 = Entry(window2, width="20")
        entry6.place(x=25, y=250)
        entry7 = Entry(window2, width="20")
        entry7.place(x=25, y=270)
        btn6 = Button(window2, text="switch text in 2 files", command=lambda:switch_data_in_files(entry6.get(),entry7.get()))
        btn6.place(x=160, y=260)
        label = Label(window2, width="20", text="enter file path")
        label.place(x=10, y=310)
        entry8 = Entry(window2, width="20")
        entry8.place(x=25, y=330)
        label = Label(window2, width="20", text="enter the word")
        label.place(x=10, y=350)
        entry9 = Entry(window2, width="20")
        entry9.place(x=25, y=370)
        btn7 = Button(window2, text="delete word from file", command=lambda: replaceString(entry8.get(),entry9.get()))
        btn7.place(x=160, y=350)
        btn8 = Button(window2, text="exit", command=lambda :on_exit(window2))
        btn8.place(x=160, y=400)

        textto = scrolledtext.ScrolledText(window2, wrap= WORD, width=40, height=20, font=("Times New Roman", 15))
        textto.place(x=0,y=450)
        window2.mainloop()



label = Label(root, width="50", text="Enter userName here")
label.place(x=5, y=60)
entry1 = Entry(root, width="30")
entry1.place(x=90, y=90)
label = Label(root, width="50", text="Enter Password")
label.place(x=5, y=120)
entry2 = Entry(root, width="30", show="*")
entry2.place(x=90, y=150)
btn2 = Button(text="Login",
              command=lambda: ActionsPage(entry1.get()) if BuildScreens.CheckifCorrectDetails(
                  entry1.get(), entry2.get()) == True else messagebox.showerror(
                  message="Wrong email/password"))
btn2.place(x=160, y=200)

root.mainloop()