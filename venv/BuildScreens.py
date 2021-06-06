from tkinter import *
from hashlib import sha256
from tkinter import messagebox




class BuildScreens(object):




    @staticmethod
    def loginPage(window):
     
        label = Label(window, width="50", text="Enter userName here")
        label.place(x=5, y=60)
        entry1 = Entry(window, width="30")
        entry1.place(x=90, y=90)
        label = Label(window, width="50", text="Enter Password")
        label.place(x=5, y=120)
        entry2 = Entry(window, width="30",show="*")
        entry2.place(x=90, y=150)
        btn2 = Button(text="Login", command=lambda:BuildScreens.ActionsPage(entry1.get(),window) if BuildScreens.CheckifCorrectDetails(entry1.get(),entry2.get())==True else messagebox.showerror(
        message="Wrong email/password"))
        btn2.place(x=160, y=200)



    def CheckifCorrectDetails(username,password):


        password= sha256(password.encode())

        for line in open("credentials.txt", "r").readlines():  # Read the lines
            login_info = line.split()  # Split on the space, and store the results in a list of two strings
            if username == login_info[0] and password.hexdigest() == login_info[1]:
                print("Correct credentials!")
                return True
        print("Incorrect credentials.")
        return False


    def ActionsPage(username,window):
        
        window2=Tk()
        window2.title("FileManagementProgram")
        window2.geometry("360x360")
        window2.iconbitmap("3123.ico")
        window2.resizable(False, False)
        label = Label(window2, width="50", text=f"Welcome {username}")
        label.place(x=5, y=30)
        label = Label(window2, width="50", text="Actions ")
        label.place(x=5, y=60)
        btn4 = Button(window2,text="Login", command=lambda:BuildScreens.loginPage() )
        btn4.place(x=160, y=100)
        btn5 = Button(window2,text="Login", command=lambda: BuildScreens.loginPage())
        btn5.place(x=160, y=130)
        btn6 = Button(window2,text="Login", command=lambda: BuildScreens.loginPage())
        btn6.place(x=160, y=160)
        btn7 = Button(window2,text="Login", command=lambda: BuildScreens.loginPage())
        btn7.place(x=160, y=190)
        btn8 = Button(window2,text="Login", command=lambda: BuildScreens.loginPage())
        btn8.place(x=160, y=220)
        window2.mainloop()