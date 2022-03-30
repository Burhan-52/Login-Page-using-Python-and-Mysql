from tkinter import *
from datetime import date
import time
import tkinter.messagebox as mgb
import mysql.connector

now=date.today()
formatted_date=now.strftime("%Y-%m-%d")

now1=time.localtime()
formatted_time=time.strftime("%H:%M:%S")
# "%I:%M:%s" this is 12 hours format...

def delete():
    if user.get()=="" and pas.get()=="":
       mgb.showerror("Error","Empty failed")
    else:
       user.set("")
       pas.set("")
       mgb.showinfo("Information","Data clear successfully..")

def login():
    print(user.get())
    print(pas.get())

    mydb = mysql.connector.connect(host="Type_your_localhost", user="Type_your_user", passwd="Type_your_password", database="Type_your_dataname")
    mycursor = mydb.cursor()

    try:
        sql = "INSERT INTO login(dates,times,username,passwords) VALUES(%s,%s,%s,%s)"
        val = (formatted_date,formatted_time,user.get(),pas.get())
        mycursor.execute(sql,val)
        mydb.commit()
        mgb.showinfo("information","login succeeded...")
    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()


root=Tk()
root.geometry("300x180")
root.configure(bg="grey")
root.title("Login Page")
root.wm_iconbitmap("login_logo.ico")
l1= Label(root,text="Login page",font= "comicsansms 15 bold").grid(column=1,pady=10)
Label(root,text="Username: ").grid(row=1,column=0,padx=20)
Label(root,text="Password: ").grid(row=2,column=0,padx=10,pady=10)

user=StringVar()
pas=StringVar()

userentry=Entry(root,textvariable=user).grid(row=1,column=1,)
passentry=Entry(root,textvariable=pas).grid(row=2,column=1,)

Button(root,text="Close",command=quit).grid(row=3,column=1)
Button(root,text="Reset",command=delete).grid(row=3,column=2)
Button(root,text="Login",command=login).grid(row=4,column=0)

root.mainloop()