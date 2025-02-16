from tkinter import*
import time
import subprocess

def showroom():
    win.destroy()
    subprocess.run(["python",".\showroom.py"])
    subprocess.run(["python",".\Mainn.py"])
    return
def customer():
    win.destroy()
    subprocess.run(["python",".\customer.py"])
    subprocess.run(["python",".\Mainn.py"])
    return
def admin():
    win.destroy()
    subprocess.run(["python",".\admin.py"])
    subprocess.run(["python",".\Mainn.py"])
    return
def dealer():
    win.destroy()
    subprocess.run(["python",".\dealer.py"])
    subprocess.run(["python",".\Mainn.py"])
    return
def car():
    win.destroy()
    subprocess.run(["python",".\car.py"])
    subprocess.run(["python",".\Mainn.py"])
    return
def about():
    win.destroy()
    subprocess.run(["python",".\about.py"])
    subprocess.run(["python",".\Mainn.py"])
    return
def clock():
    date=time.strftime('%d/%m/%Y')
    c_time=time.strftime('%H:%M:%S')
    dt_lbl.config(text=f'{date}  {c_time}')
    dt_lbl.after(1000,clock)
win=Tk()
win.title("MM CARS")
win.geometry('1200x600+0+0')
win.resizable(0,0)
win.configure(bg="light gray")
img=PhotoImage(file="./image/car1-removebg-preview.png")
label=Label(win,image=img,bg="light gray")
label.place(x=180,y=20,relwidth=1,relheight=1)

dt_lbl=Label(win,font=('times new roman',14,'italic'),bg="light gray")
dt_lbl.place(x=1015,y=565)
clock()
s1='VISHVAAS MM CARS'
s2='ZINDAGEE MM CARS'
sl_lbl=Label(win,text=s1,bg="light gray",font=('arial',28,'italic bold'))
sl_lbl.place(x=400,y=10)

bd=Frame(win,bg='black')
bd.place(x=0,y=0,width=80,height=600)

lf1=Frame(win,bg='black')
lf1.place(x=80,y=0,width=250,height=600)
lf=Frame(win,bg='black')
lf.place(x=80,y=60,width=250,height=600)

avS_btn=Button(lf,text='Available Showrooms',width=20,command=showroom)
avS_btn.grid(row=1,column=1,pady=20,padx=20)
cuA_btn=Button(lf,text='Customer Account',width=20,command=customer)
cuA_btn.grid(row=2,column=1,pady=20,padx=20)
adL_btn=Button(lf,text='Admin Login',width=20,command=admin)
adL_btn.grid(row=3,column=1,pady=20,padx=20)
mmD_btn=Button(lf,text='Dealer Login',width=20,command=dealer)
mmD_btn.grid(row=4,column=1,pady=20,padx=20)
shC_btn=Button(lf,text='Available Cars',width=20,command=car)
shC_btn.grid(row=5,column=1,pady=20,padx=20)
abt_btn=Button(lf,text='About',width=20,command=about)
abt_btn.grid(row=6,column=1,pady=20,padx=20)

win.mainloop()