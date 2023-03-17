from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk
import pymysql


def clear():
    firstnameEntry.delete(0,END)
    lastnameEntry.delete(0,END)
    emailEntry.delete(0,END)
    passwordEntry.delete(0,END)

def firstname_enter(event):
    if firstnameEntry.get()=='Firstname':
        firstnameEntry.delete(0,END)

def lastname_enter(event):
    if lastnameEntry.get()=='Lastname':
        lastnameEntry.delete(0,END)

def email_enter(event):
    if emailEntry.get()=='Email':
        emailEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

def hide():
    openeye.config(file='Closeeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=show)

def show():
    openeye.config(file='Openeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=hide)

def connect_database():
    if firstnameEntry.get()=='' or lastnameEntry.get()=='' or emailEntry.get()==''  or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields are required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error', 'Database connection issue')
            return
        try:    
            query='create database registerdatabase'
            mycursor.execute(query)
            query='use registerdatabase'
            mycursor.execute(query)
            query='create table registration(id int auto_increment primary key not null, firstname varchar(50), lastname varchar(50), email varchar(50), password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use registerdatabase')

        query='insert into registration(firstname,lastname,email,password) values(%s,%s,%s,%s)'
        mycursor.execute(query,(firstnameEntry.get(),lastnameEntry.get(),emailEntry.get(),passwordEntry.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Success','Registration is sucessfull...')
        clear()
 
root=Tk()

root.geometry('1320x672')
root.resizable(0,0)
root.title('Registration Page')
bgImage=ImageTk.PhotoImage(file='background.jpg')

bgLabel=Label(root,image=bgImage)
bgLabel.place(x=0,y=0)

frame1=Frame(root,width=400,height=550,highlightbackground='#999966',highlightthickness=2)
frame1.place(x=480,y=70)

heading=Label(root,text='REGISTER',font=('Times New Roman',20,'bold'),bd=0,fg='grey')
heading.place(x=605,y=120)

firstnameEntry=Entry(root,width=20,font=('Times New Roman',20,'bold'),bd=1,fg='#808080',bg='#f2f2f2')
firstnameEntry.place(x=540,y=200)
firstnameEntry.insert(0, 'Firstname')
firstnameEntry.bind('<FocusIn>',firstname_enter)

lastnameEntry=Entry(root,width=20,font=('Times New Roman',20,'bold'),bd=1,fg='#808080',bg='#f2f2f2')
lastnameEntry.place(x=540,y=270)
lastnameEntry.insert(0, 'Lastname')
lastnameEntry.bind('<FocusIn>',lastname_enter)

emailEntry=Entry(root,width=20,font=('Times New Roman',20,'bold'),bd=1,fg='#808080',bg='#f2f2f2')
emailEntry.place(x=540,y=340)
emailEntry.insert(0, 'Email')
emailEntry.bind('<FocusIn>',email_enter)

passwordEntry=Entry(root,width=20,show='*',font=('Times New Roman',20,'bold'),bd=1,fg='#808080',bg='#f2f2f2')
passwordEntry.place(x=540,y=410)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>',password_enter)


openeye=PhotoImage(file='Openeye.png')
eyeButton=Button(root,image=openeye,bd=0,cursor='hand2',command=hide)
eyeButton.place(x=780, y=412) 

forgetButton=Button(root,text='Forgot Password?',bd=0,font=('Times New Roman',10,'bold'),fg='firebrick1',activeforeground='firebrick1',cursor='hand2')
forgetButton.place(x=720, y=460) 

loginButton=Button(root,text='Login',font=('Times New Roman',16,'bold'),fg='white',bg='firebrick1',
activeforeground='white',cursor='hand2',bd=0,width=19,command=connect_database)
loginButton.place(x=565, y=500)

root.mainloop()