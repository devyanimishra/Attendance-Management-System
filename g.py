from tkinter import *
from tkinter import ttk  
import sqlite3
from functools import partial
from tkinter import messagebox
import os

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

def reset():
	usernameEntry.delete(0,END)
	passwordEntry.delete(0,END)



root = Tk()
C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:/Python 3.6/MPR/grid2.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()
root.state('zoomed')
root.title("ARM")
screen_height = root.winfo_screenheight()  
label_0 = Label(root,text="ATTENDANCE MANAGEMENT SYSTEM",
		 bg = "white",
		 fg = "black",
		 font = "Helvetica 25 bold ")
label_0.place(x=screen_height/2-55,y=83)



usernameLabel = Label(root, text="User Name",width=20,font=("bold",10))
usernameLabel.place(x=350,y=350)
username = StringVar()
usernameEntry = Entry(root, textvariable=username,bg="#A0A5CF")
usernameEntry.place(x=530, y=350)  
#password label and password entry box
passwordLabel = Label(root,text="Password",width=20,font=("bold",10))
passwordLabel.place(x=750,y=350)
password = StringVar() 
passwordEntry = Entry(root, textvariable=password, show='*',bg="#A0A5CF")
passwordEntry.place(x=930, y=350) 

def validateLogin():
    
    flag = False
    conn = sqlite3.connect('FaceRec.db')
    cursor = conn.cursor()
    cursor.execute('SELECT Username,Password FROM Login ')
    for row in cursor.fetchall():
        if username.get() == row[0] and password.get() == row[1]:
            filename = 'C:/Python 3.6/MPR/main.py'
            os.startfile(filename)
            flag = True
    if flag != True:
        messagebox.showinfo("Error","Invalid Credential")
            

loginButton = Button(root, text='LOGIN',width=40,bg="blue",fg='white',command=validateLogin).place(x=550,y=400)
resetButton = Button(root, text='RESET',width=40,bg="blue",fg='white',command=reset).place(x=550,y=450)
root.mainloop() 
