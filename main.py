from tkinter import *
from tkinter import ttk  
import sqlite3
import os

root = Tk()

C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:/Python 3.6/MPR/grid2.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()
root.state('zoomed')
root.title("Attendance Management")

def reset():
	e1.delete(0,END)
	e2.delete(0,END)
	e3.delete(0,END)
	e4.delete(0,END)

def new1():
	global e1,e2,e3,e4,e5,e6,e7
	root1= Tk()
	root1.geometry('500x700')
	root1.title("Registration Form")

	label_0 = Label(root1, text="Registration form",width=20,font=("bold", 20))
	label_0.place(x=90,y=53)

	label_1 = Label(root1, text="FIRST NAME",width=20,font=("bold", 10))
	label_1.place(x=80,y=130)
	e1 = Entry(root1,textvar=fname)
	e1.place(x=270,y=130)

	label_2 = Label(root1, text="LAST NAME",width=20,font=("bold", 10))
	label_2.place(x=80,y=180)
	e2 = Entry(root1,textvar=lname)
	e2.place(x=270,y=180)

	label_3 = Label(root1, text="ROLL No",width=20,font=("bold", 10))
	label_3.place(x=80,y=230)
	e3 = Entry(root1,textvar=roll)
	e3.place(x=270,y=230)

	label_4 = Label(root1, text="REGISTRATION NUMBER",width=20,font=("bold", 10))
	label_4.place(x=80,y=280)
	e4 = Entry(root1,textvar=rnum)
	e4.place(x=270,y=280)

	label_5 = Label(root1, text = "BRANCH",width=20,font=("bold",10))
	label_5.place(x=80,y=330)
	OptionList = [
	"COMPUTER",
	"INFORMATION TECHNOLOGY",
	"ELECTRONICS",                                                      
	"EXTC"
	] 
	variable = StringVar(root1)
	variable.set(OptionList[0])
	opt =OptionMenu(root1, variable, *OptionList)
	opt.config(width=30, font=('Helvetica', 8))
	opt.place(x=270,y=330)

	Button(root1, text='SUBMIT',width=20,bg='blue',fg='white',command=database).place(x=80,y=550)
	Button(root1, text='RESET FORM',width=20,bg='blue',fg='white',command=reset).place(x=240,y=550)
	Button(root1, text='QUIT',width=20,bg='blue',fg='white',command=root1.destroy).place(x=180,y=600)
	root1.mainloop()	



def database():
   
   conn = sqlite3.connect('FaceRec.db')
   cursor = conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (FIRST TEXT,LAST TEXT,ROLL INT,RNUM INT,BRANCH TEXT)')
   path = 'C:/Python 3.6/MPR/img/'+e1.get()+'_'+e2.get()+'/'
   print(path)
   name = e1.get()+'_'+e2.get()
   cursor.execute("""INSERT INTO StudentRec(FirstName,LastName,RollNo,RegNo,Branch,Ppath) VALUES(?,?,?,?,?,?)""",(e1.get(),e2.get(),e3.get(),e4.get(),variable.get(),path))
   conn.commit()
   
   Detection(name)

def Detection(name):
    from  Detection import main
  
    if not os.path.exists('C:/Python 3.6/MPR/img/Train/'+name) or not os.path.exists('C:/Python 3.6/MPR/img/Train/'+name):
                print("New directory created")
                os.makedirs('C:/Python 3.6/MPR/img/Train/'+name)
                os.makedirs('C:/Python 3.6/MPR/img/val/'+name)
                
    main(name)
    reset()
    
def Training():
    from extract_face_feature import main as face
    from  embedding import main as emb
    from Classification import training as train
    face()
    emb()
    train()

def Rec():
    from face import main as rec
    rec()
    
def Attendance():
    filename = 'C:/Python 3.6/MPR/new4.csv'
    os.startfile(filename)

roll=StringVar()
fname=StringVar()
lname=StringVar()
pnum=StringVar()
rnum=StringVar()
opt1=StringVar()
year=StringVar()
variable=StringVar()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

label_0 = Label(root,text="ATTENDANCE MANAGEMENT SYSTEM",
		 bg = "white",
		 fg = "black",
		 font = "Helvetica 25 bold")
label_0.place(x=screen_height/2-55,y=45)

Button(root, text='STUDENT REGISTRATION',width=40,bg='blue',fg='white',command=new1).place(x=600,y=250)
Button(root, text='TRAIN DATA',width=40,bg='blue',fg='white',command=Training).place(x=600,y=300)
Button(root, text='MARK ATTENDANCE ',width=40,bg='blue',fg='white',command=Rec).place(x=600,y=350)
Button(root, text='CHECK ATTENDANCE SHEET',width=40,bg="blue",fg='white',command=Attendance).place(x=600,y=400)
Button(root, text='EXIT',width=40,bg="blue",fg='white',command=root.destroy).place(x=600,y=450)

root.mainloop() 