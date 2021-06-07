from hashlib import sha256
from tkinter import *
import time
import os



######
#
# Actions class with all the methods we use in the fileManager
#
#
#####

class Actions(object):

    ## function that get the username and the password and check if it coorect from Users\credentials.txt file
    def CheckifCorrectDetails(username,password):

        password= sha256(password.encode())
        for line in open("Users\\credentials.txt", "r").readlines():  # Read the lines
            login_info = line.split()  # Split on the space, and store the results in a list of two strings
            if username == login_info[0] and password.hexdigest() == login_info[1]:
                print("Correct credentials!")
                return True
        print("Incorrect credentials.")
        return False


    ## function that get the open window and check if surre and destory it
    def on_exit(window2):
        label = Label(window2, width="50", text="Thank you for using our file management program Exiting...")
        label.place(x=5, y=420)
        response = messagebox.askyesno('Exit', 'Are you sure you want to exit?')
        if response:
            window2.destroy()


    ## function that get two files path and copy the text in first file to the second file
    def copyFiletoOther(text, file1path, file2path):
        try:
            file1name = os.path.basename(file1path)
            file2name = os.path.basename(file2path)

            if os.path.isfile(file1path) and os.path.isfile(file2path):

                if os.path.exists(file1path) and os.path.exists(file2path):
                    if os.stat(file1path).st_size != 0:
                        with open(file1path) as f:
                            with open(file2path, "a") as f1:
                                for line in f:
                                    f1.write(line)
                                Actions.showresult(text, file2path)
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


    ## function that show result in scrolled text from second file
    def showresult(text, file2path):
        text.delete("1.0", END)
        x = open(file2path, "r")
        text.insert(END, "file is copied!\n")
        text.insert(END, x.read())


    ## function that delete file by his path
    def deletefile(text, filepath):
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
                text.delete("1.0", END)
                text.insert(END, "file is deleted!")
            else:
                print("file does not Exists check the filepath!!")
        except:
            print("something went wrong")


    ## function that switch the data bitween the two files
    def switch_data_in_files(text, file1path, file2path):
        try:
            if os.access(file1path, os.W_OK) and os.access(file1path, os.R_OK) or os.access(file2path,os.W_OK) and os.access(file2path, os.R_OK):

                with open(file1path, "r") as f1:
                    lines=[line.__str__() for line in f1] ## list comprehension expression
                with open(file2path, "r") as f:
                    with open(file1path, "w") as f1:
                        for line in f:
                            f1.write(line)
                with open(file2path, "w") as f:

                    for line in lines:
                        f.write(line)
                text.delete("1.0", END)
                text.insert(END, "data is switched!")
        except:
            print("something went wrong!!")


    ## function that delete String from the file that we get in the entry.get
    def replaceString(text, filepath, word):
        with open(filepath, "r") as f:
            data = f.read()
            with open(filepath, "w") as f:
                f.write(data.replace(word.lower(), ""))
                text.delete("1.0", END)
                text.insert(END, "word is deleted!")

