import tkinter




def clikMe():
  print("Hello clicked me")
  print(uname.get())
  print(pwd.get())

  if(uname.get().lower()=="user01" and pwd.get()=="pass1234"):msg.configure(text="Sucessfull Login")
  else:msg.configure(text="Invalid passord")






window=tkinter.Tk()
window.geometry('700x500+500+300')

uname=tkinter.StringVar()
pwd=tkinter.StringVar()

# Creating a label for the windows applications

label=tkinter.Label(window,text="User Name",font=("Calibri Bold",20))
label.grid(row=0,column=0,padx=5,pady=5)

#Text Box

username=tkinter.Entry(width=30,textvariable=uname)
username.grid(sticky='W',row=0,column=1,padx=5,pady=5)




#Password Field
password_label=tkinter.Label(window,text="Password",font=("Calibri Bold",20))
password_label.grid(sticky='W',row=1,column=0,padx=5,pady=5)
#Text Box

password=tkinter.Entry(width=30,textvariable=pwd)
password.grid(row=1,column=1,padx=5,pady=5)





#Button

login=tkinter.Button(text="Login",bg="Orange",font=("Calibri Bold",20),command=clikMe)
login.grid(row=2,column=1,padx=5,pady=5)

msg=tkinter.Label(text="")
msg.grid(row=3,column=2)

window.mainloop()