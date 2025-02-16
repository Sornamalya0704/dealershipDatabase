import psycopg2
from tkinter import*
win=Tk()
win.title(" 🚗 AVAILABLE CAR SHOWROOM 🚓 ")
win.geometry('1200x600+0+0')
win.resizable(1,1)
win.configure(bg="black")
"""img=PhotoImage(file=".\image\img.png")           
label=Label(win,image=img,bg="black")
label.place(x=180,y=20,relwidth=1,relheight=1)"""

title='AVAILABLE SHOWROOMS'
lbl=Label(win,text=title,bg="black", fg="red", font=('Times',28,'bold'))
lbl.place(x=575,y=10)
#showroom details
conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
cur=conn.cursor()
cur.execute("SELECT DISTINCT ON(SHOWROOM_ID)* FROM SHOWROOM NATURAL JOIN SHOWROOM_PHONE NATURAL JOIN SHOWROOM_EMAIL")
row=cur.fetchall()
conn.close()
txt1=f'Showroom ID: {row[0][0]} \n {row[0][1]} \nCity: {row[0][3]} \nState: {row[0][2]} Pincode: {row[0][4]} \nPhone: {row[0][5]} \n Email: {row[0][6]}'
lbl1=Label(win,text=txt1,bg="black", fg="red",font=('Times',14,'bold'))
lbl1.place(x=400,y=100)

txt2=f'Showroom ID: {row[1][0]} \n {row[1][1]} \nCity: {row[1][3]} \nState: {row[1][2]} Pincode: {row[1][4]} \nPhone: {row[1][5]} \n Email: {row[1][6]}'
lbl2=Label(win,text=txt2,bg="black", fg="red",font=('Times',14,'bold'))
lbl2.place(x=800,y=100)

txt3=f'Showroom ID: {row[2][0]} \n {row[2][1]} \nCity: {row[2][3]} \nState: {row[2][2]} Pincode: {row[2][4]} \nPhone: {row[2][5]} \n Email: {row[2][6]}'
lbl3=Label(win,text=txt3,bg="black", fg="red",font=('Times',14,'bold'))
lbl3.place(x=400,y=300)

txt4=txt1=f'Showroom ID: {row[3][0]} \n {row[3][1]} \nCity: {row[3][3]} \nState: {row[3][2]} Pincode: {row[3][4]} \nPhone: {row[3][5]} \n Email: {row[3][6]}'
lbl4=Label(win,text=txt4,bg="black", fg="red",font=('Times',14,'bold'))
lbl4.place(x=800,y=300)

bd=Frame(win,bg='black')
bd.place(x=0,y=0,width=80,height=600)

lf1=Frame(win,bg='black')
lf1.place(x=80,y=0,width=250,height=600)
lf=Frame(win,bg='red')
lf.place(x=80,y=60,width=250,height=600)

avS_btn=Button(lf,text='FORD',width=20)
avS_btn.grid(row=1,column=1,pady=40,padx=20)
cuA_btn=Button(lf,text='SUZUKI',width=20)
cuA_btn.grid(row=2,column=1,pady=40,padx=20)
adL_btn=Button(lf,text='TOYOTA',width=20)
adL_btn.grid(row=3,column=1,pady=40,padx=20)
mmD_btn=Button(lf,text='TATA',width=20)
mmD_btn.grid(row=4,column=1,pady=40,padx=20)

win.mainloop()