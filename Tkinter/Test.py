import tkinter

from tkinter import  messagebox

from DatabaseConnectivity import DBConnect

#intialize database connection
dbobj=DBConnect.DataBaseConfig("Python")




def checkLogin(uname,pwd):
    print("Testing login module",uname.get(),pwd.get())
    if len(str(uname.get()))<=0 :
        messagebox.showerror("Error","User name cannot be blank")
    elif len(str(pwd.get()))<=0:
        messagebox.showerror("Error","Password cannot be blank")
    credentials=dbobj.getLogin_Details()




mainwindow=tkinter.Tk()

mainwindow.geometry('400x200+500+300')

username=tkinter.StringVar()
password=tkinter.StringVar()



#User_Name Label
username_label=tkinter.Label(mainwindow,text="User Name :",font=("Courier",20))
username_label.grid(sticky='W',row=1,column=0)
# User_Name Text Box

userName_TextBox=tkinter.Entry(mainwindow,width=25,textvariable=username,font=("Courier",10))
userName_TextBox.grid(sticky='W',row=1,column=1)

# Password _Label
password_label=tkinter.Label(mainwindow,text="Password  :",font=("Courier",20))
password_label.grid(sticky='W',row=2,column=0)

# Password _TextBox
password_TextBox=tkinter.Entry(mainwindow,width=25,textvariable=password,font=("Courier",10))
password_TextBox.grid(sticky='W',row=2,column=1)

# Sign in Button

loginbutton=tkinter.Button(text="Sign in",font=("Courier",20),command=lambda:checkLogin(username,password))
loginbutton.grid(row=3,column=1)



mainwindow.mainloop()