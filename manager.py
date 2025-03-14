from tkinter import *
from tkinter import messagebox
import database

win = Tk()
win.title("Login Form")
win.geometry("400x450")


db1 = database.Database("c:/class/data.db")

#=======function===========
def delete():
    ent_fname.delete(0, END)
    ent_lname.delete(0, END)
    ent_email.delete(0, END)
    ent_password.delete(0, END)
    ent_fname.focus_set()

def sign_up():
    fname = ent_fname.get()
    lname = ent_lname.get()
    email = ent_email.get()
    password = ent_password.get()
    if len(email)==0  or len(password) == 0:
        messagebox.showerror("error", "Email and Password are compulsory")
        
    else:
        db1.insert(fname, lname, email, password)
        messagebox.showinfo("good", "person joined")
        delete()

def sign_in():
    email = ent_email.get()
    password = ent_password.get()
    fname=ent_fname.get()
    lname=ent_lname.get()
    if len(email) ==0  or len(password) == 0:
        messagebox.showerror("error", "Email and Password are compulsory")
        
    else:
        file= db1.search(email, password)
        if file:
            messagebox.showinfo('Welcome', f'{data[0]} {data[1]}, welcome!')
            delete()
        else:
            messagebox.showerror("error", " email or password is not defind ")
        

#=======widget===========

lbl_fname = Label(win, text="fname", font="arial")
lbl_fname.place(x=20,y=20)
ent_fname = Entry(win,font="arial",width=14)
ent_fname.place(x=110,y=20)
lbl_lname = Label(win, text="lname", font="arial")
lbl_lname.place(x=20,y=70)
ent_lname = Entry(win, font="arial", width=14)
ent_lname.place(x=110,y=70)
lbl_email = Label(win, text="email", font="arial")
lbl_email.place(x=20,y=120)
ent_email = Entry(win, font="arial", width=14)
ent_email.place(x=110,y=120)
lbl_password = Label(win, text="password", font="arial")
lbl_password.place(x=15,y=170)
ent_password = Entry(win, font="arial", width=14)
ent_password.place(x=110,y=170)
lbl_star=Label(win,text="*",font="arial",fg="red")
lbl_star.place(x=0,y=170)
lbl_star1=Label(win,text="*",font="arial",fg="red")
lbl_star1.place(x=10,y=120)
btn_sign_up = Button(win, text="sign up", font="arial", width=12, command=sign_up)
btn_sign_up.place(x=50,y=300)
btn_sign_in = Button(win, text="sign in", font="arial", width=12, command=sign_in)
btn_sign_in.place(x=200,y=300)
win.mainloop()
