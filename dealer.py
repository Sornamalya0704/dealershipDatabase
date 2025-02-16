import psycopg2
from tkinter import*
from tkinter import messagebox
from tkinter import ttk

def user_entry(event):
    if userEntry.get()=='Username':
        userEntry.delete(0,END)

def pass_entry(event):
    if passEntry.get()=='Password':
        passEntry.delete(0,END)

def update_profile():      
    window=Tk()
    window.title("My Profile")
    window.geometry('880x600+320+0')
    window.resizable(0,0)
    lbl1=Label(window,bg='light blue')
    lbl1.place(x=0,y=0,relwidth=1,relheight=1)
    
    heading=Label(window,text='MY PROFILE',font=('Arial',20,'bold'),bg='light blue',fg='navy')
    heading.place(x=340,y=80)
    idLabel=Label(window,text='Dealer Id',font=('Times New Roman',14,'bold'),bg='light blue',fg='black')
    idLabel.place(x=200,y=140)
    nameLabel=Label(window,text='Name',font=('Times New Roman',14,'bold'),bg='light blue',fg='black')
    nameLabel.place(x=200,y=200)
    phoneLabel=Label(window,text='Phone number',font=('Times New Roman',14,'bold'),bg='light blue',fg='black')
    phoneLabel.place(x=200,y=260)
    emailLabel=Label(window,text='Email Id',font=('Times New Roman',14,'bold'),bg='light blue',fg='black')
    emailLabel.place(x=200,y=320)
    """roomLabel=Label(window,text='Showroom name',font=('Times New Roman',14,'bold'),bg='light blue',fg='black')
    roomLabel.place(x=200,y=380)"""
    statusLabel=Label(window,text='Status',font=('Times New Roman',14,'bold'),bg='light blue',fg='black')
    statusLabel.place(x=200,y=380)

    id=Label(window,text=dealer_id,font=('Times New Roman',14),bg='light blue',fg='black')
    id.place(x=500,y=140)
    conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
    cur=conn.cursor()
    query7="SELECT DISTINCT ON (DEALER_ID) DEALER_ID,DEALER_NAME,PHONE_NUMBER,EMAIL_ID,STATUS FROM DEALER NATURAL JOIN DEALER_PHONE NATURAL JOIN DEALER_EMAIL WHERE DEALER_ID=%s"
    cur.execute(query7,(dealer_id,))
    deal=cur.fetchall()
    name=Label(window,text=deal[0][1],font=('Times New Roman',14),bg='light blue',fg='black')
    name.place(x=500,y=200)
    phone=Label(window,text=deal[0][2],font=('Times New Roman',14),bg='light blue',fg='black')
    phone.place(x=500,y=260)
    email=Label(window,text=deal[0][3],font=('Times New Roman',14),bg='light blue',fg='black')
    email.place(x=500,y=320)
    """room=Label(window,text=deal[0][4],font=('Times New Roman',14),bg='light blue',fg='black')
    room.place(x=500,y=380)"""
    status=Label(window,text=deal[0][4],font=('Times New Roman',14),bg='light blue',fg='black')
    status.place(x=500,y=380)
    
    conn.commit()
    conn.close()
    window.mainloop()
    return
def add_cars():
    add=Tk()
    add.title("ADD CARS")
    add.geometry('880x600+320+0')
    add.resizable(0,0)
    lbl=Label(add,bg='light cyan')
    lbl.place(x=0,y=0,relwidth=1,relheight=1)
    heading=Label(add,text='ADD CAR',font=('Arial',20,'bold'),bg='light cyan',fg='navy')
    heading.place(x=245,y=20)
    serialLabel=Label(add,text='Serial number',font=('Times New Roman',10,'italic'),bg='light cyan',fg='black')
    serialLabel.place(x=200,y=80)
    serialEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    serialEntry.place(x=200,y=100)

    brandLabel=Label(add,text='Brand',font=('Times New Roman',10,'italic'),bg='light cyan',fg='black')
    brandLabel.place(x=200,y=130)
    brandEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    brandEntry.place(x=200,y=150)

    modelLabel=Label(add,text='Model',font=('Times New Roman',10,'italic'),bg='light cyan',fg='black')
    modelLabel.place(x=200,y=180)
    modelEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    modelEntry.place(x=200,y=200)

    saleLabel=Label(add,text='For sale',font=('Times New Roman',10,'italic'),bg='light cyan',fg='black')
    saleLabel.place(x=200,y=230)
    saleEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    saleEntry.place(x=200,y=250)

    colourLabel=Label(add,text='Colour',font=('Times New Roman',10,'italic'),bg='light cyan',fg='black')
    colourLabel.place(x=200,y=280)
    colourEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    colourEntry.place(x=200,y=300)

    yearLabel=Label(add,text='Year',font=('Times New Roman',10,'italic'),bg='light cyan',fg='black')
    yearLabel.place(x=200,y=330)
    yearEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    yearEntry.place(x=200,y=350)

    priceLabel=Label(add,text='Price',font=('Times New Roman',10,'italic'),bg='light cyan',fg='black')
    priceLabel.place(x=200,y=380)
    priceEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    priceEntry.place(x=200,y=400)

    comfortLabel=Label(add,text='Comfortness',font=('Times New Roman',10,'italic'),bg='light cyan',fg='black')
    comfortLabel.place(x=200,y=430)
    comfortEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    comfortEntry.place(x=200,y=450)

    reliableLabel=Label(add,text='Reliability',font=('Times New Roman',10,'italic'),bg='light cyan',fg='black')
    reliableLabel.place(x=200,y=480)
    reliableEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    reliableEntry.place(x=200,y=500)

    conditionLabel=Label(add,text='Condition',font=('Times New Roman',10,'italic'),bg='light cyan',fg='black')
    conditionLabel.place(x=500,y=80)
    conditionEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    conditionEntry.place(x=500,y=100)

    fuelLabel=Label(add,text='Fuel type',font=('Times New Roman',10,'italic'),bg='light cyan',fg='black')
    fuelLabel.place(x=500,y=130)
    fuelEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    fuelEntry.place(x=500,y=150)

    mileLabel=Label(add,text='Mileage',font=('Times New Roman',10,'italic'),bg='light cyan',fg='black')
    mileLabel.place(x=500,y=180)
    mileEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    mileEntry.place(x=500,y=200)

    engineLabel=Label(add,text='Engine capacity',font=('Times New Roman',10,'italic'),bg='light cyan',fg='black')
    engineLabel.place(x=500,y=230)
    engineEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    engineEntry.place(x=500,y=250)

    performLabel=Label(add,text='Performance',font=('Times New Roman',10,'italic'),bg='light cyan',fg='black')
    performLabel.place(x=500,y=280)
    performEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    performEntry.place(x=500,y=300)

    entertainLabel=Label(add,text='Entertainment',font=('Times New Roman',10,'italic'),bg='light cyan',fg='black')
    entertainLabel.place(x=500,y=330)
    entertainEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    entertainEntry.place(x=500,y=350)

    navigateLabel=Label(add,text='Navigation',font=('Times New Roman',10,'italic'),bg='light cyan',fg='black')
    navigateLabel.place(x=500,y=380)
    navigateEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    navigateEntry.place(x=500,y=400)

    safeLabel=Label(add,text='Safety',font=('Times New Roman',10,'italic'),bg='light cyan',fg='black')
    safeLabel.place(x=500,y=430)
    safeEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    safeEntry.place(x=500,y=450)

    def adding():
        if serialEntry.get()=='' or brandEntry.get()=='' or modelEntry.get()=='' or saleEntry.get()=='' or colourEntry.get()=='' or yearEntry.get()=='' or priceEntry.get()=='' or comfortEntry.get()=='' or reliableEntry.get()=='' or conditionEntry.get()=='' or fuelEntry.get()=='' or mileEntry.get()=='' or engineEntry.get()=='' or performEntry.get()=='' or entertainEntry.get()=='' or navigateEntry.get()=='' or safeEntry.get()=='':
            messagebox.showerror("Error","Required all fields")
        else:
            conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
            cur=conn.cursor()
            cur.execute("SELECT COUNT(*) FROM DEALER")
            res=cur.fetchone()
            ress=str(res[0]+1)
            mark="CAR"
            id=mark+ress
            dealer_id
            query3="SELECT SHOWROOM_ID FROM ADMIN WHERE ADMIN_ID=(SELECT ADMIN_ID FROM DEALER WHERE DEALER_ID=%s)"
            cur.execute(query3,(dealer_id,))
            dat=cur.fetchone()
            global showroom_id
            showroom_id=dat[0]
            query1="INSERT INTO CAR(CAR_ID,SERIAL_NUM,BRAND,MODEL,FOR_SALE,COLOUR,YEAR,PRICE,SHOWROOM_ID) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(query1,(id,serialEntry.get(),brandEntry.get(),modelEntry.get(),saleEntry.get(),colourEntry.get(),yearEntry.get(),priceEntry.get(),showroom_id))
            query2="INSERT INTO FEATURES(CAR_ID,COMFORTNESS,RELIABILITY,CONDITION,FUEL_TYPE,MILEAGE,ENGINE_CAPACITY,PERFORMANCE,ENTERTAINMENT,NAVIGATION,SAFETY) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(query2,(id,comfortEntry.get(),reliableEntry.get(),conditionEntry.get(),fuelEntry.get(),mileEntry.get(),engineEntry.get(),performEntry.get(),entertainEntry.get(),navigateEntry.get(),safeEntry.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Car added succesfully")
            add.destroy()
    but=Button(add,text='Add Car',width=20,bg='navy',fg='black',command=adding)
    but.place(x=525,y=500)

    add.mainloop()
    return
def dealer_activity():
    def populate_treeview():
        conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
        cur=conn.cursor()
        query1="SELECT SHOWROOM_ID FROM ADMIN WHERE ADMIN_ID=(SELECT ADMIN_ID FROM DEALER WHERE DEALER_ID=%s)"
        cur.execute(query1,(dealer_id,))
        ans=cur.fetchone()
        print(ans[0])
        showroom_id=ans
        query="SELECT SERIAL_NUM,MODEL,COLOUR,PRICE,FOR_SALE FROM CAR WHERE SHOWROOM_ID=%s"
        cur.execute(query,(showroom_id,))
        data = cur.fetchall()
        """ tree.delete(*tree.get_children()) # Clear the Treeview"""
        for row in data:
            tree.insert("", "end", values=row)
        conn.commit()
        conn.close()
# Function to update the selected record in the database
    def update_record():
        if sno_entry.get()!="":
            model = model_entry.get()
            colour = colour_entry.get()
            for_sale = sale_Entry.get()
            serial = sno_entry.get()

            conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
            cur=conn.cursor()
            query2="UPDATE CAR SET MODEL=%s, COLOUR=%s ,FOR_SALE=%s WHERE SERIAL_NUM=%s"
            cur.execute(query2,(model, colour, for_sale,serial))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Updated Successfully",parent=vity)

        # Clear the entry fields and update the Treeview
            model_entry.delete(0, "end")
            sale_Entry.delete(0, "end")
            sno_entry.delete(0, "end")
            colour_entry.delete(0, "end")
            for item in tree.get_children():
                tree.delete(item)
            populate_treeview()

# Function to delete the selected record from the database
    def delete_record():
        if sno_entry.get()!="":
            car_number=sno_entry.get()
            conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
            cur=conn.cursor()
            query="SELECT CAR_ID FROM CAR WHERE SERIAL_NUM=%s"
            cur.execute(query,(car_number,))
            car=cur.fetchone()
            car_id=car[0]
            cur.execute("DELETE FROM FEATURES WHERE CAR_ID=%s", (car_id,))
            cur.execute("DELETE FROM CAR WHERE CAR_ID=%s", (car_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Dealer Deleted Successfully",parent=vity)

        # Clear the entry fields and update the Treeview
            sno_entry.delete(0, "end")
            colour_entry.delete(0, "end")
            sale_Entry.delete(0, "end")
            model_entry.delete(0, "end")
            for item in tree.get_children():
                tree.delete(item)
            populate_treeview()
    vity=Tk()
    vity.title("DEALER ACTIVITY")
    vity.geometry('880x600+320+0')
    vity.resizable(0,0)
    lbl=Label(vity,bg='light blue')
    lbl.place(x=0,y=0,relwidth=1,relheight=1)
    

# Create and populate the SQLite database

# Create and configure the Treeview widget  
    tree = ttk.Treeview(vity, columns=("SERIAL_NUMBER","MODEL","COLOUR","PRICE","FOR_SALE"), show="headings")
    tree.heading("SERIAL_NUMBER", text="SERIAL NUMBER")
    tree.heading("MODEL", text="MODEL")
    tree.heading("COLOUR", text="COLOUR")
    tree.heading("PRICE", text="PRICE")
    tree.heading("FOR_SALE", text="FOR_SALE")
    tree.place(x=20,y=10)

# Create Entry widgets for data input
    name_label = Label(vity, text="SERIAL NUMBER:",bg="light blue")
    name_label.place(x=80,y=300)
    sno_entry = Entry(vity)
    sno_entry.place(x=300,y=300)

    age_label = Label(vity, text="MODEL:",bg="light blue")
    age_label.place(x=80,y=340)
    model_entry = Entry(vity)
    model_entry.place(x=300,y=340)

    city_label = Label(vity, text="COLOUR:",bg="light blue")
    city_label.place(x=80,y=380)
    colour_entry = Entry(vity)
    colour_entry.place(x=300,y=380)
    Label(vity,text="FOR_SALE:",bg="light blue").place(x=80,y=420)
    sale_Entry=Entry(vity)
    sale_Entry.place(x=300,y=420)

# Create buttons for database operations

    update_button = Button(vity, text="Update", command=update_record)
    update_button.place(x=600,y=340)

    delete_button = Button(vity, text="Delete", command=delete_record)
    delete_button.place(x=600,y=390)
    populate_treeview()
# Start the Tkinter main loop
    vity.mainloop()
    return
def login():
    if userEntry.get()==(''or'Username') or passEntry.get()==(''or'Password'):
        messagebox.showerror("Error","All Fields are required")
    else:
        conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
        cur=conn.cursor()
        query="SELECT * FROM DEALER WHERE USERNAME=%s AND PASSWORD=%s"
        cur.execute(query,(userEntry.get(),passEntry.get()))
        row=cur.fetchone()
        username=row[1]
        global dealer_id
        dealer_id=row[0]
        conn.commit()
        conn.close()
        if row==None:
            messagebox.showerror("Error","Invalid username or password")
        else:
            ler=Tk()
            ler.title("MM DEALER")
            ler.geometry('880x600+320+0')
            ler.resizable(0,0)
            lbl=Label(ler,bg='light cyan')
            lbl.place(x=0,y=0,relwidth=1,relheight=1)
            messagebox.showinfo("Welcome","Login is successful",parent=ler)
            dea.destroy()
            w="Welcome "
            s=w+username
            heading=Label(ler,text=s,font=('Arial',20,'bold'),bg='light cyan',fg='navy')
            heading.place(x=40,y=80)
            add=Button(ler,text='Add Cars',width=20,height=5,bg='cadet blue',activebackground='grey',command=add_cars)
            add.place(x=100,y=200)
            activity=Button(ler,text='Activity',width=20,height=5,bg='cadet blue',activebackground='grey',command=dealer_activity)
            activity.place(x=300,y=200)
            profile=Button(ler,text='My profile',width=20,height=5,bg='cadet blue',activebackground='grey',command=update_profile)
            profile.place(x=500,y=200)
            ler.mainloop()
    return

def forget_password():
    def reset_password():
        if userEntry.get()=='' or passEntry.get()=='' or passEntry1.get()=='' or phoneEntry.get()=='':
            messagebox.showerror('Error','All Fields Are Required',parent=window)
        elif passEntry.get()!=passEntry1.get():
            messagebox.showerror('Error','Password mismatch',parent=window)
        else:
            conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
            cur=conn.cursor()
            query="SELECT * FROM DEALER NATURAL JOIN DEALER_PHONE WHERE USERNAME=%s AND PHONE_NUMBER=%s"
            cur.execute(query,(userEntry.get(),phoneEntry.get()))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect username or phone number',parent=window)
            else:
                query="UPDATE DEALER SET PASSWORD=%s WHERE USERNAME=%s"
                cur.execute(query,(passEntry.get(),userEntry.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo('Success','Password is reset, Please login with new password',parent=window)
                window.destroy()
        return
    window=Toplevel()
    window.title("Change Password")
    window.geometry('300x600+320+0')
    window.resizable(0,0)
    lbl1=Label(window,bg='light cyan')
    lbl1.place(x=0,y=0,relwidth=1,relheight=1)

    heading=Label(window,text='RESET PASSWORD',font=('Arial',20,'bold'),bg='light cyan',fg='navy')
    heading.place(x=20,y=80)

    userLabel=Label(window,text='Username*',font=('Times New Roman',10,'italic'),bg='light cyan',fg='black')
    userLabel.place(x=20,y=140)
    userEntry=Entry(window,width=25,font=('Times New Roman',11,'bold'),bd=0,bg='light cyan')
    userEntry.place(x=20,y=160)
    f1=Frame(window,width=250,height=2,bg='black')
    f1.place(x=20,y=180)

    passLabel=Label(window,text='Password*',font=('Times New Roman',10,'italic'),bg='light cyan',fg='black')
    passLabel.place(x=20,y=200)
    passEntry=Entry(window,width=25,font=('Times New Roman',11,'bold'),bd=0,bg='light cyan')
    passEntry.place(x=20,y=220)
    f2=Frame(window,width=250,height=2,bg='black')
    f2.place(x=20,y=240)

    passLabel1=Label(window,text='Confirm Password*',font=('Times New Roman',10,'italic'),bg='light cyan',fg='black')
    passLabel1.place(x=20,y=260)
    passEntry1=Entry(window,width=25,font=('Times New Roman',11,'bold'),bd=0,bg='light cyan')
    passEntry1.place(x=20,y=280)
    f4=Frame(window,width=250,height=2,bg='black')
    f4.place(x=20,y=300)

    phoneLabel=Label(window,text='Phone number*',font=('Times New Roman',10,'italic'),bg='light cyan',fg='black')
    phoneLabel.place(x=20,y=320)
    phoneEntry=Entry(window,width=25,font=('Times New Roman',11,'bold'),bd=0,bg='light cyan')
    phoneEntry.place(x=20,y=340)
    f3=Frame(window,width=250,height=2,bg='black')
    f3.place(x=20,y=360)
    
    submitButton=Button(window,text='SUBMIT',font=('Times New Roman',11,'bold'),bd=0,
                   bg='navy',activebackground='gray',cursor='hand2',activeforeground='white',width=27,height=1,command=reset_password)
    submitButton.place(x=20,y=400)
    return

dea=Tk()
dea.title("MM DEALERS")
dea.geometry('880x600+320+0')
dea.resizable(0,0)
lbl=Label(dea,bg='light cyan')
lbl.place(x=0,y=0,relwidth=1,relheight=1)

img=PhotoImage(file="C:/Users/SORNAMALYA SIVAKUMAR/Downloads/acc-removebg-preview.png")
label=Label(dea,image=img,bg='light cyan')
label.place(x=100,y=0,relwidth=1,relheight=1)

heading=Label(dea,text='DEALER LOGIN',font=('Arial',20,'bold'),bg='light cyan',fg='navy')
heading.place(x=40,y=80)

userEntry=Entry(dea,width=25,font=('Times New Roman',11,'bold'),bd=0,bg='light cyan')
userEntry.place(x=20,y=160)
userEntry.insert(0,'Username')
userEntry.bind('<FocusIn>',user_entry)
f1=Frame(dea,width=250,height=2,bg='black')
f1.place(x=10,y=180)

passEntry=Entry(dea,width=25,font=('Times New Roman',11,'bold'),bd=0,bg='light cyan')
passEntry.place(x=20,y=220)
passEntry.insert(0,'Password')
passEntry.bind('<FocusIn>',pass_entry)
f2=Frame(dea,width=250,height=2,bg='black')
f2.place(x=10,y=240)

forgetButton=Button(dea,text='Forgot Password',bd=0,bg='light cyan',activebackground='light cyan',
                    cursor='hand2',font=('Times New Roman',11,'bold'),fg='red',activeforeground='black',command=forget_password)
forgetButton.place(x=20,y=260)

loginButton=Button(dea,text='Login',font=('Times New Roman',11,'bold'),bd=0,
                   bg='navy',activebackground='grey',width=20,cursor='hand2',activeforeground='white',command=login)
loginButton.place(x=40,y=300)

dea.mainloop()
