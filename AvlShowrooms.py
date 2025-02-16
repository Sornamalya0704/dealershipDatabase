from tkinter import *
import time
import subprocess

def Ford():
    #subprocess.run(["python",".\showroom.py"])
    return
def Suzuki():
    #subprocess.run(["python",".\customer.py"])
    return
def Toyota():
    #subprocess.run(["python",".\admin.py"])
    return
def Tata():
    #subprocess.run(["python",".\dealer.py"])
    return
#def car():
      #subprocess.run(["python",".\car.py"])
      #return

def clock():
    date=time.strftime('%d/%m/%Y')
    c_time=time.strftime('%H:%M:%S')
    dt_lbl.config(text=f'{date}  {c_time}')
    dt_lbl.after(1000,clock)

#parent window

win=Tk()
win.title(" 🚗 AVAILABLE CARS 🚓 ")
win.geometry('1200x600+0+0')
win.resizable(1,1)
win.configure(bg="black")
"""img=PhotoImage(file="./image/img.png")               #image insertion
label=Label(win,image=img,bg="black")
label.place(x=180,y=20,relwidth=1,relheight=1)"""

#win.state("zoomed")                                                                          #fullsceen

#Time and Date
dt_lbl=Label(win,font=('times new roman',14,'italic'),bg="light gray")
dt_lbl.place(x=1015,y=565)
clock()

#heading

title='AVAILABLE SHOWROOMS'
lbl=Label(win,text=title,bg="black", fg="red", font=('Times',28,'bold'))
lbl.place(x=575,y=10)

#showroom details
txt1='Showroom ID: 001 \nShowroom Name: Ford Showroom \nCity: CityA \nState: StateA Pincode: 12345 \nPhone: 123-456-7890 \n Email: ford@example.com'
lbl1=Label(win,text=txt1,bg="black", fg="red",font=('Times',14,'bold'))
lbl1.place(x=400,y=100)

txt2='Showroom ID: 001 \nShowroom Name: Ford Showroom \nCity: CityA \nState: StateA Pincode: 12345 \nPhone: 123-456-7890 \n Email: ford@example.com'
lbl2=Label(win,text=txt2,bg="black", fg="red",font=('Times',14,'bold'))
lbl2.place(x=800,y=100)

txt3='Showroom ID: 001 \nShowroom Name: Ford Showroom \nCity: CityA \nState: StateA Pincode: 12345 \nPhone: 123-456-7890 \n Email: ford@example.com'
lbl3=Label(win,text=txt3,bg="black", fg="red",font=('Times',14,'bold'))
lbl3.place(x=400,y=300)

txt4='Showroom ID: 001 \nShowroom Name: Ford Showroom \nCity: CityA \nState: StateA Pincode: 12345 \nPhone: 123-456-7890 \n Email: ford@example.com'
lbl4=Label(win,text=txt4,bg="black", fg="red",font=('Times',14,'bold'))
lbl4.place(x=800,y=300)

bd=Frame(win,bg='black')
bd.place(x=0,y=0,width=80,height=600)

lf1=Frame(win,bg='black')
lf1.place(x=80,y=0,width=250,height=600)
lf=Frame(win,bg='red')
lf.place(x=80,y=60,width=250,height=600)

avS_btn=Button(lf,text='FORD',width=20,command=Ford)
avS_btn.grid(row=1,column=1,pady=40,padx=20)
cuA_btn=Button(lf,text='SUZUKI',width=20,command=Suzuki)
cuA_btn.grid(row=2,column=1,pady=40,padx=20)
adL_btn=Button(lf,text='TOYOTA',width=20,command=Toyota)
adL_btn.grid(row=3,column=1,pady=40,padx=20)
mmD_btn=Button(lf,text='TATA',width=20,command=Tata)
mmD_btn.grid(row=4,column=1,pady=40,padx=20)
#shC_btn=Button(lf,text='Search Cars',width=20,command=car)
#shC_btn.grid(row=5,column=1,pady=20,padx=20)


win.mainloop()