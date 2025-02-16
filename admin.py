import psycopg2
from tkinter import*
from tkinter import ttk
from tkinter import messagebox

def user_entry(event):
    if userEntry.get()=='Username':
        userEntry.delete(0,END)

def pass_entry(event):
    if passEntry.get()=='Password':
        passEntry.delete(0,END)

def update_profile():
    def update():
        def save():
            conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
            cur=conn.cursor()
            v=admin_id
            v1=nameE.get()
            v2=phoneE.get()
            v3=emailE.get()
            query="UPDATE DEALER SET DEALER_NAME=%s WHERE DEALER_ID=%s"
            cur.execute(query,(v1,v))
            query="UPDATE DEALER_PHONE SET PHONE_NUMBER=%s WHERE DEALER_ID=%s"
            cur.execute(query,(v2,v))
            query="UPDATE DEALER_EMAIL SET EMAIL_ID=%s WHERE DEALER_ID=%s"
            cur.execute(query,(v3,v))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Profile Updated")
            return
        up=Toplevel()
        up.title("Update Profile")
        up.geometry('880x600+320+0')
        up.resizable(0,0)
        lbl1=Label(up,bg='light blue')
        lbl1.place(x=0,y=0,relwidth=1,relheight=1)
        heading=Label(up,text='MY PROFILE',font=('Arial',20,'bold'),bg='light blue',fg='navy')
        heading.place(x=340,y=80)
        idLabel=Label(up,text='Admin Id',font=('Times New Roman',14,'bold'),bg='light blue',fg='black')
        idLabel.place(x=200,y=140)
        nameLabel=Label(up,text='Name',font=('Times New Roman',14,'bold'),bg='light blue',fg='black')
        nameLabel.place(x=200,y=200)
        phoneLabel=Label(up,text='Phone number',font=('Times New Roman',14,'bold'),bg='light blue',fg='black')
        phoneLabel.place(x=200,y=260)
        emailLabel=Label(up,text='Email Id',font=('Times New Roman',14,'bold'),bg='light blue',fg='black')
        emailLabel.place(x=200,y=320)
        
        id=Entry(up,font=('Times New Roman',14),fg='black')
        id.place(x=500,y=140)
        id.insert(0,admin_id)
        id.config(state=DISABLED,fg='black')
        nameE=Entry(up,font=('Times New Roman',14),fg='black')
        nameE.place(x=500,y=200)
        phoneE=Entry(up,font=('Times New Roman',14),fg='black')
        phoneE.place(x=500,y=260)
        emailE=Entry(up,font=('Times New Roman',14),fg='black')
        emailE.place(x=500,y=320)
        update=Button(up,text='Update',font=('Times New Roman',11,'bold'),bd=0,
                   bg='firebrick2',activebackground='black',cursor='hand2',activeforeground='red',width=27,height=1,command=save)
        update.place(x=300,y=400)
       






    window=Toplevel()
    window.title("My Profile")
    window.geometry('880x600+320+0')
    window.resizable(0,0)
    lbl1=Label(window,bg='light blue')
    lbl1.place(x=0,y=0,relwidth=1,relheight=1)
    
    heading=Label(window,text='MY PROFILE',font=('Arial',20,'bold'),bg='light blue',fg='navy')
    heading.place(x=340,y=80)
    idLabel=Label(window,text='Admin Id',font=('Times New Roman',14,'bold'),bg='light blue',fg='black')
    idLabel.place(x=200,y=140)
    nameLabel=Label(window,text='Name',font=('Times New Roman',14,'bold'),bg='light blue',fg='black')
    nameLabel.place(x=200,y=200)
    phoneLabel=Label(window,text='Phone number',font=('Times New Roman',14,'bold'),bg='light blue',fg='black')
    phoneLabel.place(x=200,y=260)
    emailLabel=Label(window,text='Email Id',font=('Times New Roman',14,'bold'),bg='light blue',fg='black')
    emailLabel.place(x=200,y=320)
    roomLabel=Label(window,text='Showroom name',font=('Times New Roman',14,'bold'),bg='light blue',fg='black')
    roomLabel.place(x=200,y=380)
    statusLabel=Label(window,text='Status',font=('Times New Roman',14,'bold'),bg='light blue',fg='black')
    statusLabel.place(x=200,y=440)
    update=Button(window,text='Update Profile',font=('Times New Roman',11,'bold'),bd=0,
                   bg='firebrick2',activebackground='black',cursor='hand2',activeforeground='red',width=27,height=1,command=update)
    update.place(x=300,y=520)

    id=Label(window,text=admin_id,font=('Times New Roman',14),bg='light blue',fg='black')
    id.place(x=500,y=140)
    conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
    cur=conn.cursor()
    query="SELECT DISTINCT ON (ADMIN_ID) ADMIN_ID,ADMIN_NAME,PHONE_NUMBER,EMAIL_ID,SHOWROOM_NAME,STATUS FROM ADMIN NATURAL JOIN ADMIN_PHONE NATURAL JOIN ADMIN_EMAIL NATURAL JOIN SHOWROOM WHERE ADMIN_ID=%s"
    cur.execute(query,(admin_id,))
    admin=cur.fetchall()
    name=Label(window,text=admin[0][1],font=('Times New Roman',14),bg='light blue',fg='black')
    name.place(x=500,y=200)
    phone=Label(window,text=admin[0][2],font=('Times New Roman',14),bg='light blue',fg='black')
    phone.place(x=500,y=260)
    email=Label(window,text=admin[0][3],font=('Times New Roman',14),bg='light blue',fg='black')
    email.place(x=500,y=320)
    room=Label(window,text=admin[0][4],font=('Times New Roman',14),bg='light blue',fg='black')
    room.place(x=500,y=380)
    status=Label(window,text=admin[0][5],font=('Times New Roman',14),bg='light blue',fg='black')
    status.place(x=500,y=440)
    
    conn.commit()
    conn.close()
    window.mainloop()
def add_dealer():
    add=Tk()
    add.title("ADD DEALERS")
    add.geometry('880x600+320+0')
    add.resizable(0,0)
    lbl=Label(add,bg='light blue')
    lbl.place(x=0,y=0,relwidth=1,relheight=1)
    heading=Label(add,text='ADD DEALER',font=('Arial',20,'bold'),bg='light blue',fg='navy')
    heading.place(x=245,y=20)
    nameLabel=Label(add,text='Dealer Name*',font=('Times New Roman',10,'italic'),bg='light blue',fg='black')
    nameLabel.place(x=200,y=80)
    nameEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    nameEntry.place(x=200,y=100)

    userLabel=Label(add,text='Username*',font=('Times New Roman',10,'italic'),bg='light blue',fg='black')
    userLabel.place(x=200,y=140)
    userEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    userEntry.place(x=200,y=160)

    passLabel=Label(add,text='Password*',font=('Times New Roman',10,'italic'),bg='light blue',fg='black')
    passLabel.place(x=200,y=200)
    passEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    passEntry.place(x=200,y=220)

    status=Label(add,text='Status*',font=('Times New Roman',10,'italic'),bg='light blue',fg='black')
    status.place(x=200,y=260)
    statusEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    statusEntry.place(x=200,y=280)

    phoneLabel=Label(add,text='Phone Number 1*',font=('Times New Roman',10,'italic'),bg='light blue',fg='black')
    phoneLabel.place(x=200,y=320)
    phoneEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    phoneEntry.place(x=200,y=340)

    phoneLabel2=Label(add,text='Phone Number 2',font=('Times New Roman',10,'italic'),bg='light blue',fg='black')
    phoneLabel2.place(x=200,y=380)
    phoneEntry2=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    phoneEntry2.place(x=200,y=400)

    phoneLabel3=Label(add,text='Phone Number 3',font=('Times New Roman',10,'italic'),bg='light blue',fg='black')
    phoneLabel3.place(x=200,y=440)
    phoneEntry3=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    phoneEntry3.place(x=200,y=460)

    emailLabel=Label(add,text='Email Id 1*',font=('Times New Roman',10,'italic'),bg='light blue',fg='black')
    emailLabel.place(x=200,y=500)
    emailEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    emailEntry.place(x=200,y=520)

    emailLabel2=Label(add,text='Email Id 2',font=('Times New Roman',10,'italic'),bg='light blue',fg='black')
    emailLabel2.place(x=500,y=80)
    emailEntry2=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    emailEntry2.place(x=500,y=100)

    cityLabel=Label(add,text='City*',font=('Times New Roman',10,'italic'),bg='light blue',fg='black')
    cityLabel.place(x=500,y=140)
    cityEntry=Entry(add,width=25,font=('Times New Roman',11,'bold'),bd=0)
    cityEntry.place(x=500,y=160)

    def adding():
        if nameEntry.get()=='' or userEntry.get()=='' or passEntry.get()=='' or cityEntry.get()=='' or statusEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='':
            messagebox.showerror("Error","Required all fields")
        else:
            conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
            cur=conn.cursor()
            cur.execute("SELECT COUNT(*) FROM DEALER")
            res=cur.fetchone()
            ress=str(res[0]+1)
            mark="DEA"
            id=mark+ress
            query1="INSERT INTO DEALER(DEALER_ID,DEALER_NAME,USERNAME,PASSWORD,CITY,ADMIN_ID,STATUS) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(query1,(id,nameEntry.get(),userEntry.get(),passEntry.get(),cityEntry.get(),admin_id,statusEntry.get()))
            query2="INSERT INTO DEALER_PHONE(DEALER_ID,PHONE_NUMBER) VALUES(%s,%s)"
            cur.execute(query2,(id,phoneEntry.get()))
            query3="INSERT INTO DEALER_EMAIL(DEALER_ID,EMAIL_ID) VALUES(%s,%s)"
            cur.execute(query3,(id,emailEntry.get()))
            if phoneEntry2.get()!='':
                query4="INSERT INTO DEALER_PHONE(DEALER_ID,PHONE_NUMBER) VALUES(%s,%s)"
                cur.execute(query4,(id,phoneEntry2.get()))
            if phoneEntry3.get()!='':
                query5="INSERT INTO DEALER_PHONE(DEALER_ID,PHONE_NUMBER) VALUES(%s,%s)"
                cur.execute(query5,(id,phoneEntry3.get()))
            if emailEntry2.get()!='':
                query6="INSERT INTO DEALER_EMAIL(DEALER_ID,EMAIL_ID) VALUES(%s,%s)"
                cur.execute(query6,(id,emailEntry2.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Dealer added succesfully")
            add.destroy()
    but=Button(add,text='Add Dealer',width=20,bg='navy',fg='black',command=adding)
    but.place(x=525,y=400)

    add.mainloop()

def admin_activity():
    def populate_treeview():
        conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
        cur=conn.cursor()
        query="SELECT DEALER_ID,DEALER_NAME,CITY,STATUS FROM DEALER WHERE ADMIN_ID=%s"
        cur.execute(query,(admin_id,))
        data = cur.fetchall()
        """ tree.delete(*tree.get_children()) # Clear the Treeview"""
        for row in data:
            tree.insert("", "end", values=row)
        conn.commit()
        conn.close()
# Function to update the selected record in the database
    def update_record():
        if id_entry.get()!="":
            name = name_entry.get()
            id = id_entry.get()
            city = city_entry.get()
            status = status_Entry.get()

            conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
            cur=conn.cursor()
            query2="UPDATE DEALER SET DEALER_NAME=%s, CITY=%s ,STATUS=%s WHERE DEALER_ID=%s"
            cur.execute(query2,(name, city, status ,id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Updated Successfully",parent=vity)

        # Clear the entry fields and update the Treeview
            name_entry.delete(0, "end")
            status_Entry.delete(0, "end")
            city_entry.delete(0, "end")
            status_Entry.delete(0, "end")
            for item in tree.get_children():
                tree.delete(item)
            populate_treeview()

# Function to delete the selected record from the database
    def delete_record():
        if id_entry.get()!="":
            id=id_entry.get()
            conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
            cur=conn.cursor()
            cur.execute("DELETE FROM DEALER_PHONE WHERE DEALER_ID=%s", (id,))
            cur.execute("DELETE FROM DEALER_EMAIL WHERE DEALER_ID=%s", (id,))
            cur.execute("DELETE FROM DEALER WHERE DEALER_ID=%s", (id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Dealer Deleted Successfully",parent=vity)

        # Clear the entry fields and update the Treeview
            name_entry.delete(0, "end")
            id_entry.delete(0, "end")
            status_Entry.delete(0, "end")
            city_entry.delete(0, "end")
            for item in tree.get_children():
                tree.delete(item)
            populate_treeview()
    vity=Tk()
    vity.title("ADMIN ACTIVITY")
    vity.geometry('880x600+320+0')
    vity.resizable(0,0)
    lbl=Label(vity,bg='light blue')
    lbl.place(x=0,y=0,relwidth=1,relheight=1)
    

# Create and populate the SQLite database

# Create and configure the Treeview widget  
    tree = ttk.Treeview(vity, columns=("DEALER_ID", "DEALER_NAME", "CITY", "STATUS"), show="headings")
    tree.heading("DEALER_ID", text="DEALER ID")
    tree.heading("DEALER_NAME", text="DEALER NAME")
    tree.heading("CITY", text="CITY")
    tree.heading("STATUS", text="STATUS")
    tree.place(x=20,y=10)

# Create Entry widgets for data input
    name_label = Label(vity, text="DEALER ID:",bg="light blue")
    name_label.place(x=80,y=300)
    id_entry = Entry(vity)
    id_entry.place(x=300,y=300)

    age_label = Label(vity, text="DEALER NAME:",bg="light blue")
    age_label.place(x=80,y=340)
    name_entry = Entry(vity)
    name_entry.place(x=300,y=340)

    city_label = Label(vity, text="CITY:",bg="light blue")
    city_label.place(x=80,y=380)
    city_entry = Entry(vity)
    city_entry.place(x=300,y=380)
    Label(vity,text="STATUS:",bg="light blue").place(x=80,y=420)
    status_Entry=Entry(vity)
    status_Entry.place(x=300,y=420)

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
        query="SELECT * FROM ADMIN WHERE USERNAME=%s AND PASSWORD=%s"
        cur.execute(query,(userEntry.get(),passEntry.get()))
        row=cur.fetchone()
        username=row[1]
        global admin_id
        admin_id=row[0]
        conn.commit()
        conn.close()
        if row==None:
            messagebox.showerror("Error","Invalid username or password")
        else:
            adm.destroy()
            min=Tk()
            min.title("MM ADMINISTRATOR")
            min.geometry('880x600+320+0')
            min.resizable(0,0)
            lbl=Label(min,bg='light blue')
            lbl.place(x=0,y=0,relwidth=1,relheight=1)
            messagebox.showinfo("Welcome","Login is successful",parent=min)
            w="Welcome "
            s=w+username
            heading=Label(min,text=s,font=('Arial',20,'bold'),bg='light blue',fg='navy')
            heading.place(x=40,y=80)
            add=Button(min,text='Add Dealer',width=20,height=5,bg='cornflower blue',activebackground='grey',command=add_dealer)
            add.place(x=100,y=200)
            activity=Button(min,text='Activity',width=20,height=5,bg='cornflower blue',activebackground='grey',command=admin_activity)
            activity.place(x=300,y=200)
            profile=Button(min,text='My profile',width=20,height=5,bg='cornflower blue',activebackground='grey',command=update_profile)
            profile.place(x=500,y=200)
            min.mainloop()
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
            query="SELECT * FROM ADMIN NATURAL JOIN ADMIN_PHONE WHERE USERNAME=%s AND PHONE_NUMBER=%s"
            cur.execute(query,(userEntry.get(),phoneEntry.get()))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect username or phone number',parent=window)
            else:
                query="UPDATE ADMIN SET PASSWORD=%s WHERE USERNAME=%s"
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
    lbl1=Label(window,bg='light blue')
    lbl1.place(x=0,y=0,relwidth=1,relheight=1)

    heading=Label(window,text='RESET PASSWORD',font=('Arial',20,'bold'),bg='light blue',fg='navy')
    heading.place(x=20,y=80)

    userLabel=Label(window,text='Username*',font=('Times New Roman',10,'italic'),bg='light blue',fg='black')
    userLabel.place(x=20,y=140)
    userEntry=Entry(window,width=25,font=('Times New Roman',11,'bold'),bd=0,bg='light blue')
    userEntry.place(x=20,y=160)
    f1=Frame(window,width=250,height=2,bg='black')
    f1.place(x=20,y=180)

    passLabel=Label(window,text='Password*',font=('Times New Roman',10,'italic'),bg='light blue',fg='black')
    passLabel.place(x=20,y=200)
    passEntry=Entry(window,width=25,font=('Times New Roman',11,'bold'),bd=0,bg='light blue')
    passEntry.place(x=20,y=220)
    f2=Frame(window,width=250,height=2,bg='black')
    f2.place(x=20,y=240)

    passLabel1=Label(window,text='Confirm Password*',font=('Times New Roman',10,'italic'),bg='light blue',fg='black')
    passLabel1.place(x=20,y=260)
    passEntry1=Entry(window,width=25,font=('Times New Roman',11,'bold'),bd=0,bg='light blue')
    passEntry1.place(x=20,y=280)
    f4=Frame(window,width=250,height=2,bg='black')
    f4.place(x=20,y=300)

    phoneLabel=Label(window,text='Phone number*',font=('Times New Roman',10,'italic'),bg='light blue',fg='black')
    phoneLabel.place(x=20,y=320)
    phoneEntry=Entry(window,width=25,font=('Times New Roman',11,'bold'),bd=0,bg='light blue')
    phoneEntry.place(x=20,y=340)
    f3=Frame(window,width=250,height=2,bg='black')
    f3.place(x=20,y=360)
    
    submitButton=Button(window,text='SUBMIT',font=('Times New Roman',11,'bold'),bd=0,
                   bg='navy',activebackground='gray',cursor='hand2',activeforeground='white',width=27,height=1,command=reset_password)
    submitButton.place(x=20,y=400)
    return

    
adm=Tk()
adm.title("ADMIN LOGIN")
adm.geometry('880x600+320+0')
adm.resizable(0,0)
lbl=Label(adm,bg='light blue')
lbl.place(x=0,y=0,relwidth=1,relheight=1)

img=PhotoImage(file="C:/Users/SORNAMALYA SIVAKUMAR/Downloads/acc-removebg-preview.png")
label=Label(adm,image=img,bg='light blue')
label.place(x=100,y=0,relwidth=1,relheight=1)

heading=Label(adm,text='ADMIN LOGIN',font=('Arial',20,'bold'),bg='light blue',fg='navy')
heading.place(x=40,y=80)

userEntry=Entry(adm,width=25,font=('Times New Roman',11,'bold'),bd=0,bg='light blue')
userEntry.place(x=20,y=160)
userEntry.insert(0,'Username')
userEntry.bind('<FocusIn>',user_entry)
f1=Frame(adm,width=250,height=2,bg='black')
f1.place(x=10,y=180)

passEntry=Entry(adm,width=25,font=('Times New Roman',11,'bold'),bd=0,bg='light blue')
passEntry.place(x=20,y=220)
passEntry.insert(0,'Password')
passEntry.bind('<FocusIn>',pass_entry)
f2=Frame(adm,width=250,height=2,bg='black')
f2.place(x=10,y=240)

forgetButton=Button(adm,text='Forgot Password',bd=0,bg='light blue',activebackground='light blue',
                    cursor='hand2',font=('Times New Roman',11,'bold'),fg='red',activeforeground='black',command=forget_password)
forgetButton.place(x=20,y=260)

loginButton=Button(adm,text='Login',font=('Times New Roman',11,'bold'),bd=0,
                   bg='navy',activebackground='grey',width=20,cursor='hand2',activeforeground='white',command=login)
loginButton.place(x=40,y=300)

adm.mainloop()