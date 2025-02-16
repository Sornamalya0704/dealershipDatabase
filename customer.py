import psycopg2
from tkinter import*
from datetime import date
from tkinter import ttk
from tkinter import messagebox

def user_entry(event):
    if userEntry.get()=='Username':
        userEntry.delete(0,END)

def pass_entry(event):
    if passEntry.get()=='Password':
        passEntry.delete(0,END)

def buy_buy():
    buy=Tk()
    buy.title("Search car to buy")
    buy.geometry('880x600+320+0')
    buy.resizable(0,0)
    lbl=Label(buy,bg='light pink')
    lbl.place(x=0,y=0,relwidth=1,relheight=1)
    heading=Label(buy,text='SEARCH CARS',font=('Arial',20,'bold'),bg='light pink',fg='firebrick1')
    heading.place(x=300,y=40)
    search=Label(buy,text='SELECT THE FILTER :',font=("Times new roman",14),bg='light pink')
    search.place(x=50,y=100)
    n=StringVar()
    filterChoosen=ttk.Combobox(buy,width=25,height=5,textvariable=n)
    filterChoosen['values']=('BRAND','MODEL','COLOUR','YEAR','PRICE','COMFORTNESS','FUEL_TYPE','MILEAGE','ENGINE_CAPACITY','PERFORMANCE')
    filterChoosen['state']='readonly'
    filterChoosen.place(x=300,y=100)
    b=StringVar()
    brands=ttk.Combobox(buy,width=25,textvariable=b)
    def details():
        serial_no1=Label(buy,text='Car serial number',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
        serial_no1.place(x=80,y=160)
        brand1=Label(buy,text='Brand name',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
        brand1.place(x=80,y=180)
        model1=Label(buy,text='Model number',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
        model1.place(x=80,y=200)
        sale1=Label(buy,text='For sale',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
        sale1.place(x=80,y=220)
        colour1=Label(buy,text='Colour',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
        colour1.place(x=80,y=240)
        year1=Label(buy,text='Year',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
        year1.place(x=80,y=260)
        price1=Label(buy,text='Price',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
        price1.place(x=80,y=280)
        comfort1=Label(buy,text='Comfortness',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
        comfort1.place(x=80,y=300)
        reliability1=Label(buy,text='Reliability',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
        reliability1.place(x=80,y=320)
        condition1=Label(buy,text='Condition',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
        condition1.place(x=80,y=340)
        fuel1=Label(buy,text='Fuel type',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
        fuel1.place(x=80,y=360)
        mileage1=Label(buy,text='Mileage',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
        mileage1.place(x=80,y=380)
        engine1=Label(buy,text='Engine capacity',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
        engine1.place(x=80,y=400)
        performance1=Label(buy,text='Performance',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
        performance1.place(x=80,y=420)
        environment1=Label(buy,text='Environment',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
        environment1.place(x=80,y=440)
        navigate1=Label(buy,text='Navigation',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
        navigate1.place(x=80,y=460)
        safe1=Label(buy,text='Safety',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
        safe1.place(x=80,y=480)

    
    def buy_details(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17):
        serial=Label(buy,text=d1,font=('Times New Roman',14),bg='light pink',fg='black')
        serial.place(x=380,y=160)
        brand=Label(buy,text=d2,font=('Times New Roman',14),bg='light pink',fg='black')
        brand.place(x=380,y=180)
        model=Label(buy,text=d3,font=('Times New Roman',14),bg='light pink',fg='black')
        model.place(x=380,y=200)
        sale=Label(buy,text=d4,font=('Times New Roman',14),bg='light pink',fg='black')
        sale.place(x=380,y=220)
        colour=Label(buy,text=d5,font=('Times New Roman',14),bg='light pink',fg='black')
        colour.place(x=380,y=240)
        year=Label(buy,text=d6,font=('Times New Roman',14),bg='light pink',fg='black')
        year.place(x=380,y=260)
        price=Label(buy,text=d7,font=('Times New Roman',14),bg='light pink',fg='black')
        price.place(x=380,y=280)
        comfort=Label(buy,text=d8,font=('Times New Roman',14),bg='light pink',fg='black')
        comfort.place(x=380,y=300)
        reliable=Label(buy,text=d9,font=('Times New Roman',14),bg='light pink',fg='black')
        reliable.place(x=380,y=320)
        condition=Label(buy,text=d10,font=('Times New Roman',14),bg='light pink',fg='black')
        condition.place(x=380,y=340)
        fuel=Label(buy,text=d11,font=('Times New Roman',14),bg='light pink',fg='black')
        fuel.place(x=380,y=360)
        mile=Label(buy,text=d12,font=('Times New Roman',14),bg='light pink',fg='black')
        mile.place(x=380,y=380)
        engine=Label(buy,text=d13,font=('Times New Roman',14),bg='light pink',fg='black')
        engine.place(x=380,y=400)
        perform=Label(buy,text=d14,font=('Times New Roman',14),bg='light pink',fg='black')
        perform.place(x=380,y=420)
        ev=Label(buy,text=d15,font=('Times New Roman',14),bg='light pink',fg='black')
        ev.place(x=380,y=440)
        navi=Label(buy,text=d16,font=('Times New Roman',14),bg='light pink',fg='black')
        navi.place(x=380,y=460)
        safe=Label(buy,text=d17,font=('Times New Roman',14),bg='light pink',fg='black')
        safe.place(x=380,y=480)
    def fetch_details():
        details()
    
        n=0
        conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
        cur=conn.cursor()
        if filterChoosen.get()=='BRAND':
            query1="SELECT COUNT(*) FROM CAR NATURAL JOIN FEATURES WHERE BRAND=%s AND FOR_SALE=%s"
            cur.execute(query1,(brands.get(),'Y'))
            num=cur.fetchone()
            number=num[0]
            query2="SELECT SERIAL_NUM,BRAND,MODEL,FOR_SALE,COLOUR,YEAR,PRICE,COMFORTNESS,RELIABILITY,CONDITION,FUEL_TYPE,MILEAGE,ENGINE_CAPACITY,PERFORMANCE,ENTERTAINMENT,NAVIGATION,SAFETY FROM CAR NATURAL JOIN FEATURES WHERE BRAND=%s AND FOR_SALE=%s"
            cur.execute(query2,(brands.get(),'Y'))
            buys=cur.fetchall()
        if filterChoosen.get()=='MODEL':
            query1="SELECT COUNT(*) FROM CAR NATURAL JOIN FEATURES WHERE MODEL=%s AND FOR_SALE=%s"
            cur.execute(query1,(brands.get(),'Y'))
            num=cur.fetchone()
            number=num[0]
            query2="SELECT SERIAL_NUM,BRAND,MODEL,FOR_SALE,COLOUR,YEAR,PRICE,COMFORTNESS,RELIABILITY,CONDITION,FUEL_TYPE,MILEAGE,ENGINE_CAPACITY,PERFORMANCE,ENTERTAINMENT,NAVIGATION,SAFETY FROM CAR NATURAL JOIN FEATURES WHERE MODEL=%s AND FOR_SALE=%s"
            cur.execute(query2,(brands.get(),'Y'))
            buys=cur.fetchall()
        if filterChoosen.get()=='COLOUR':
            query1="SELECT COUNT(*) FROM CAR NATURAL JOIN FEATURES WHERE COLOUR=%s AND FOR_SALE=%s"
            cur.execute(query1,(brands.get(),'Y'))
            num=cur.fetchone()
            number=num[0]
            query2="SELECT SERIAL_NUM,BRAND,MODEL,FOR_SALE,COLOUR,YEAR,PRICE,COMFORTNESS,RELIABILITY,CONDITION,FUEL_TYPE,MILEAGE,ENGINE_CAPACITY,PERFORMANCE,ENTERTAINMENT,NAVIGATION,SAFETY FROM CAR NATURAL JOIN FEATURES WHERE COLOUR=%s AND FOR_SALE=%s"
            cur.execute(query2,(brands.get(),'Y'))
            buys=cur.fetchall()
        if filterChoosen.get()=='YEAR':
            query1="SELECT COUNT(*) FROM CAR NATURAL JOIN FEATURES WHERE YEAR=%s AND FOR_SALE=%s"
            cur.execute(query1,(brands.get(),'Y'))
            num=cur.fetchone()
            number=num[0]
            query2="SELECT SERIAL_NUM,BRAND,MODEL,FOR_SALE,COLOUR,YEAR,PRICE,COMFORTNESS,RELIABILITY,CONDITION,FUEL_TYPE,MILEAGE,ENGINE_CAPACITY,PERFORMANCE,ENTERTAINMENT,NAVIGATION,SAFETY FROM CAR NATURAL JOIN FEATURES WHERE YEAR=%s AND FOR_SALE=%s"
            cur.execute(query2,(brands.get(),'Y'))
            buys=cur.fetchall()
        if filterChoosen.get()=='PRICE':
            query1="SELECT COUNT(*) FROM CAR NATURAL JOIN FEATURES WHERE PRICE=%s AND FOR_SALE=%s"
            cur.execute(query1,(brands.get(),'Y'))
            num=cur.fetchone()
            number=num[0]
            query2="SELECT SERIAL_NUM,BRAND,MODEL,FOR_SALE,COLOUR,YEAR,PRICE,COMFORTNESS,RELIABILITY,CONDITION,FUEL_TYPE,MILEAGE,ENGINE_CAPACITY,PERFORMANCE,ENTERTAINMENT,NAVIGATION,SAFETY FROM CAR NATURAL JOIN FEATURES WHERE PRICE=%s AND FOR_SALE=%s"
            cur.execute(query2,(brands.get(),'Y'))
            buys=cur.fetchall()
        if filterChoosen.get()=='COMFORTNESS':
            query1="SELECT COUNT(*) FROM CAR NATURAL JOIN FEATURES WHERE COMFORTNESS=%s AND FOR_SALE=%s"
            cur.execute(query1,(brands.get(),'Y'))
            num=cur.fetchone()
            number=num[0]
            query2="SELECT SERIAL_NUM,BRAND,MODEL,FOR_SALE,COLOUR,YEAR,PRICE,COMFORTNESS,RELIABILITY,CONDITION,FUEL_TYPE,MILEAGE,ENGINE_CAPACITY,PERFORMANCE,ENTERTAINMENT,NAVIGATION,SAFETY FROM CAR NATURAL JOIN FEATURES WHERE COMFORTNESS=%s AND FOR_SALE=%s"
            cur.execute(query2,(brands.get(),'Y'))
            buys=cur.fetchall()
        if filterChoosen.get()=='FUEL_TYPE':
            query1="SELECT COUNT(*) FROM CAR NATURAL JOIN FEATURES WHERE FUEL_TYPE=%s AND FOR_SALE=%s"
            cur.execute(query1,(brands.get(),'Y'))
            num=cur.fetchone()
            number=num[0]
            query2="SELECT SERIAL_NUM,BRAND,MODEL,FOR_SALE,COLOUR,YEAR,PRICE,COMFORTNESS,RELIABILITY,CONDITION,FUEL_TYPE,MILEAGE,ENGINE_CAPACITY,PERFORMANCE,ENTERTAINMENT,NAVIGATION,SAFETY FROM CAR NATURAL JOIN FEATURES WHERE FUEL_TYPE=%s AND FOR_SALE=%s"
            cur.execute(query2,(brands.get(),'Y'))
            buys=cur.fetchall()
        if filterChoosen.get()=='MILEAGE':
            query1="SELECT COUNT(*) FROM CAR NATURAL JOIN FEATURES WHERE MILEAGE=%s AND FOR_SALE=%s"
            cur.execute(query1,(brands.get(),'Y'))
            num=cur.fetchone()
            number=num[0]
            query2="SELECT SERIAL_NUM,BRAND,MODEL,FOR_SALE,COLOUR,YEAR,PRICE,COMFORTNESS,RELIABILITY,CONDITION,FUEL_TYPE,MILEAGE,ENGINE_CAPACITY,PERFORMANCE,ENTERTAINMENT,NAVIGATION,SAFETY FROM CAR NATURAL JOIN FEATURES WHERE MILEAGE=%s AND FOR_SALE=%s"
            cur.execute(query2,(brands.get(),'Y'))
            buys=cur.fetchall()
        if filterChoosen.get()=='ENGINE_CAPACITY':
            query1="SELECT COUNT(*) FROM CAR NATURAL JOIN FEATURES WHERE ENGINE_CAPACITY=%s AND FOR_SALE=%s"
            cur.execute(query1,(brands.get(),'Y'))
            num=cur.fetchone()
            number=num[0]
            query2="SELECT SERIAL_NUM,BRAND,MODEL,FOR_SALE,COLOUR,YEAR,PRICE,COMFORTNESS,RELIABILITY,CONDITION,FUEL_TYPE,MILEAGE,ENGINE_CAPACITY,PERFORMANCE,ENTERTAINMENT,NAVIGATION,SAFETY FROM CAR NATURAL JOIN FEATURES WHERE ENGINE_CAPACITY=%s AND FOR_SALE=%s"
            cur.execute(query2,(brands.get(),'Y'))
            buys=cur.fetchall()
        if filterChoosen.get()=='PERFORMANCE':
            query1="SELECT COUNT(*) FROM CAR NATURAL JOIN FEATURES WHERE PERFORMANCE=%s AND FOR_SALE=%s"
            cur.execute(query1,(brands.get(),'Y'))
            num=cur.fetchone()
            number=num[0]
            query2="SELECT SERIAL_NUM,BRAND,MODEL,FOR_SALE,COLOUR,YEAR,PRICE,COMFORTNESS,RELIABILITY,CONDITION,FUEL_TYPE,MILEAGE,ENGINE_CAPACITY,PERFORMANCE,ENTERTAINMENT,NAVIGATION,SAFETY FROM CAR NATURAL JOIN FEATURES WHERE PERFORMANCE=%s AND FOR_SALE=%s"
            cur.execute(query2,(brands.get(),'Y'))
            buys=cur.fetchall()
        conn.commit()
        conn.close()
        buy_details(buys[n][0],buys[n][1],buys[n][2],buys[n][3],buys[n][4],buys[n][5],buys[n][6],buys[n][7],buys[n][8],buys[n][9],buys[n][10],buys[n][11],buys[n][12],buys[n][13],buys[n][14],buys[n][15],buys[n][16])
        def write(n):
            buy_details("                              ","                              ","                              ",
                    "                              ","                              ","                              ",
                    "                              ","                              ","                              ",
                    "                              ","                              ","                              ",
                    "                              ","                              ","                              ",
                    "                              ","                              ")
            buy_details(buys[n][0],buys[n][1],buys[n][2],buys[n][3],buys[n][4],buys[n][5],buys[n][6],buys[n][7],buys[n][8],buys[n][9],buys[n][10],buys[n][11],buys[n][12],buys[n][13],buys[n][14],buys[n][15],buys[n][16])
            
        
        def next():
            nonlocal n
            n+=1
            if n==number:
                n=0
            write(n)
        global carserial
        carserial=buys[n][0]
        next=Button(buy,text='Next >>',width=10,bg='pink',fg='black',activebackground='grey',command=next)
        next.place(x=525,y=450)
        buy_but=Button(buy,text='BUY CAR',width=15,bg='green',activebackground='grey',command=buy_car)
        buy_but.place(x=630,y=450)
    filterChoosen.current()
    def filter():
        if filterChoosen.get()=='BRAND':
            conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
            cur=conn.cursor()
            cur.execute("SELECT DISTINCT ON(BRAND) BRAND FROM CAR")
            res=cur.fetchall()
            conn.close()
            brands['values']=res
            brands.place(x=500,y=100)
            brands.current()
        if filterChoosen.get()=='MODEL':
            conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
            cur=conn.cursor()
            cur.execute("SELECT DISTINCT ON(MODEL) MODEL FROM CAR")
            res=cur.fetchall()
            conn.close()
            brands['values']=res
            brands.place(x=500,y=100)
            brands.current()
        if filterChoosen.get()=='COLOUR':
            conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
            cur=conn.cursor()
            cur.execute("SELECT DISTINCT ON(COLOUR) COLOUR FROM CAR")
            res=cur.fetchall()
            conn.close()
            brands['values']=res
            brands.place(x=500,y=100)
            brands.current()
        if filterChoosen.get()=='YEAR':
            conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
            cur=conn.cursor()
            cur.execute("SELECT DISTINCT ON(YEAR) YEAR FROM CAR")
            res=cur.fetchall()
            conn.close()
            brands['values']=res
            brands.place(x=500,y=100)
            brands.current()
        if filterChoosen.get()=='PRICE':
            conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
            cur=conn.cursor()
            cur.execute("SELECT DISTINCT ON(PRICE) PRICE FROM CAR")
            res=cur.fetchall()
            conn.close()
            brands['values']=res
            brands.place(x=500,y=100)
            brands.current()
        if filterChoosen.get()=='COMFORTNESS':
            conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
            cur=conn.cursor()
            cur.execute("SELECT DISTINCT ON(COMFORTNESS) COMFORTNESS FROM FEATURES")
            res=cur.fetchall()
            conn.close()
            brands['values']=res
            brands.place(x=500,y=100)
            brands.current()
        if filterChoosen.get()=='FUEL_TYPE':
            conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
            cur=conn.cursor()
            cur.execute("SELECT DISTINCT ON(FUEL_TYPE) FUEL_TYPE FROM FEATURES")
            res=cur.fetchall()
            conn.close()
            brands['values']=res
            brands.place(x=500,y=100)
            brands.current()
        if filterChoosen.get()=='MILEAGE':
            conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
            cur=conn.cursor()
            cur.execute("SELECT DISTINCT ON(MILEAGE) MILEAGE FROM FEATURES")
            res=cur.fetchall()
            conn.close()
            brands['values']=res
            brands.place(x=500,y=100)
            brands.current()
        if filterChoosen.get()=='ENGINE_CAPACITY':
            conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
            cur=conn.cursor()
            cur.execute("SELECT DISTINCT ON(ENGINE_CAPACITY) ENGINE_CAPACITY FROM FEATURES")
            res=cur.fetchall()
            conn.close()
            brands['values']=res
            brands.place(x=500,y=100)
            brands.current()
        if filterChoosen.get()=='PERFORMANCE':
            conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
            cur=conn.cursor()
            cur.execute("SELECT DISTINCT ON(PERFORMANCE) PERFORMANCE FROM FEATURES")
            res=cur.fetchall()
            conn.close()
            brands['values']=res
            brands.place(x=500,y=100)
            brands.current()
        filt=Button(buy,text=">",height=1,bg='grey',activebackground='light blue',command=fetch_details)
        filt.place(x=670,y=100)
        return
    filt=Button(buy,text=">",height=1,bg='grey',activebackground='light blue',command=filter)
    filt.place(x=470,y=100)
    def buy_car():
        window=Toplevel()
        window.title("SALES INVOICE")
        window.geometry('880x600+320+0')
        window.resizable(0,0)
        lbl=Label(window,bg='light pink')
        lbl.place(x=0,y=0,relwidth=1,relheight=1)
        def insurance():
            conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
            cur=conn.cursor()
            cur.execute("SELECT COUNT(*) FROM INSURANCE")
            res=cur.fetchone()
            ress=str(res[0]+1)
            mark="INS"
            id=mark+ress
            ser=carserial
            query="SELECT PRICE FROM CAR WHERE SERIAL_NUM=%s AND FOR_SALE=%s"
            cur.execute(query,(ser,'Y'))
            price=cur.fetchone()
            amnt=price[0]
            amt=int(amnt)*0.1
            query="SELECT * FROM INSURANCE WHERE CUSTOMER_ID=%s AND CARSERIAL_NUM=%s"
            cur.execute(query,(customer_id,carserial))
            det=cur.fetchone()
            if det==None:
                query1="INSERT INTO INSURANCE(INSURANCE_ID,CUSTOMER_ID,INSURANCE_AMOUNT,CARSERIAL_NUM) VALUES (%s,%s,%s,%s)"
                cur.execute(query1,(id,customer_id,amt,carserial))
                messagebox.showinfo('success','Insurance claimed successfully',parent=window)
            else:
                messagebox.showerror('warning','You have already claimed insurance for this car',parent=window)
            conn.commit()
            conn.close()
            return
        def invoice():
            def payment():
                def pay_car():
                    rupee=paying4.get()
                    rupee=int(rupee)
                    if rupee=='':
                        messagebox.showerror('Error','Amount is not entered for payment',parent=window)
                    elif rupee>amount_to_pay:
                        messagebox.showwarning('Warning','Check the amount entered',parent=window)
                    elif rupee<amount_to_pay/2:
                        messagebox.showinfo('Insufficient','Amount should be more than this!',parent=window)
                    else:
                        conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
                        cur=conn.cursor()
                        bal=amount_to_pay-rupee
                        query1="INSERT INTO PAYMENT(PAYMENT_ID,AMOUNT_PAID,BALANCE,PAYMENT_DATE,INVOICE_ID) VALUES (%s,%s,%s,%s,%s)"
                        cur.execute(query1,(payment_id,rupee,bal,cur_date,i_invoice_id))
                        if bal==0:
                            query2="UPDATE CAR SET FOR_SALE='N' WHERE SERIAL_NUM=%s AND FOR_SALE=%s"
                            cur.execute(query2,(carserial,'Y'))
                            messagebox.showinfo('Congrats','Payment Successful\nPick your car from our showroom!',parent=buy)
                        else:
                            messagebox.showinfo('Success','Payment successful!!')
                        conn.commit()
                        conn.close()
                    return
                pay=Label(window,text="                       ",width=20,height=5,bg='light pink',fg='black')
                pay.place(x=500,y=380)
                invoi_id.destroy()
                invoi_id1.destroy()
                cust_id.destroy()
                cust_id1.destroy()
                seri.destroy()
                seri1.destroy()
                insure.destroy()
                insure1.destroy()
                price.destroy()
                price1.destroy()
                day.destroy()
                day1.destroy()
                amount.destroy()
                amount1.destroy()
                pay_id3=Label(window,text='PAYMENT ID',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
                pay_id3.place(x=100,y=160)
                invoi_id3=Label(window,text='INVOICE ID',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
                invoi_id3.place(x=100,y=180)
                cust_id3=Label(window,text='CUSTOMER ID',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
                cust_id3.place(x=100,y=200)
                seri3=Label(window,text='CAR SERIAL NUMBER',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
                seri3.place(x=100,y=220)
                insure3=Label(window,text='INSURANCE AMOUNT',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
                insure3.place(x=100,y=240)
                price3=Label(window,text='PRICE OF THE CAR',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
                price3.place(x=100,y=260)
                day3=Label(window,text='PAYMENT DATE',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
                day3.place(x=100,y=280)
                amount3=Label(window,text='AMOUNT TO PAY',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
                amount3.place(x=100,y=300)
                paying3=Label(window,text='AMOUNT PAYING',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
                paying3.place(x=100,y=320)
                conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
                cur=conn.cursor()
                cur.execute("SELECT COUNT(*) FROM PAYMENT")
                set=cur.fetchone()
                pinv=str(set[0]+1)
                mark="PAY"
                payment_id=mark+pinv
                cur_date=date.today()
                conn.close()
                pay_id4=Label(window,text=payment_id,font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
                pay_id4.place(x=500,y=160)
                invoi_id4=Label(window,text=i_invoice_id,font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
                invoi_id4.place(x=500,y=180)
                cust_id4=Label(window,text=i_customer_id,font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
                cust_id4.place(x=500,y=200)
                seri4=Label(window,text=i_car_serial,font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
                seri4.place(x=500,y=220)
                insure4=Label(window,text=i_insurance,font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
                insure4.place(x=500,y=240)
                price4=Label(window,text=i_price,font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
                price4.place(x=500,y=260)
                day4=Label(window,text=cur_date,font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
                day4.place(x=500,y=280)
                amount4=Label(window,text=amount_to_pay,font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
                amount4.place(x=500,y=300)
                paying4=Entry(window,font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
                paying4.place(x=500,y=320)
                paying4.insert(0,amount_to_pay)
                purchase=Button(window,font=('Times New Roman',14),text="Pay",bg='green',fg='black',activebackground='gold',command=pay_car)
                purchase.place(x=500,y=380)
                return
            conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
            cur=conn.cursor()
            cur.execute("SELECT COUNT(*) FROM SALES_INVOICE")
            sal=cur.fetchone()
            inv=str(sal[0]+1)
            mark="INV"
            invoice=mark+inv
            cur_date=date.today()
            query1="SELECT INSURANCE_AMOUNT FROM INSURANCE WHERE CUSTOMER_ID=%s AND CARSERIAL_NUM=%s"
            cur.execute(query1,(customer_id,carserial))
            data=cur.fetchone()
            if data!=None:
                query6="SELECT INVOICE_ID FROM SALES_INVOICE WHERE CUSTOMER_ID=%s AND CAR_SERIALNO=%s"
                cur.execute(query6,(customer_id,carserial))
                datas=cur.fetchone()
                if datas==None:
                    insurance_amount=data[0]
                    query3="INSERT INTO SALES_INVOICE(INVOICE_ID,CUSTOMER_ID,CAR_SERIALNO,INSURANCE_AMOUNT,SALE_DATE) VALUES (%s,%s,%s,%s,%s)"
                    cur.execute(query3,(invoice,customer_id,carserial,insurance_amount,cur_date))
                    conn.commit()
            else:
                messagebox.showinfo('To Know','We will assist you to claim insurance',parent=window)            
            query2="SELECT INVOICE_ID,CUSTOMER_ID,CAR_SERIALNO,INSURANCE_AMOUNT,SALE_DATE FROM SALES_INVOICE WHERE CUSTOMER_ID=%s AND CAR_SERIALNO=%s"
            cur.execute(query2,(customer_id,carserial))
            bill=cur.fetchall()
            i_invoice_id=bill[0][0]
            i_customer_id=bill[0][1]
            i_car_serial=bill[0][2]
            i_insurance=bill[0][3]
            i_date=bill[0][4]
            query4="SELECT PRICE FROM CAR WHERE SERIAL_NUM=%s AND FOR_SALE=%s"
            cur.execute(query4,(carserial,'Y'))
            price=cur.fetchall()
            i_price=price[0][0]
            query6="SELECT COUNT(*) FROM PAYMENT WHERE INVOICE_ID=%s AND INVOICE_ID=%s"
            cur.execute(query6,(i_invoice_id,i_invoice_id))
            var=cur.fetchone()
            if var==None:
                amount_to_pay=int(i_price)-int(i_insurance)
            else:
                query1="SELECT BALANCE FROM PAYMENT WHERE INVOICE_ID=%s AND INVOICE_ID=%s"
                cur.execute(query1,(i_invoice_id,i_invoice_id))
                bala=cur.fetchone()
                if bala!=None:
                    amount_to_pay=bala[0]
                else:
                    amount_to_pay=int(i_price)-int(i_insurance)

            conn.commit()
            conn.close()
            
            invoi_id=Label(window,text='INVOICE ID',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
            invoi_id.place(x=100,y=160)
            cust_id=Label(window,text='CUSTOMER ID',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
            cust_id.place(x=100,y=180)
            seri=Label(window,text='CAR SERIAL NUMBER',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
            seri.place(x=100,y=200)
            insure=Label(window,text='INSURANCE AMOUNT',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
            insure.place(x=100,y=220)
            price=Label(window,text='PRICE OF THE CAR',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
            price.place(x=100,y=240)
            day=Label(window,text='INVOICE DATE',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
            day.place(x=100,y=260)
            amount=Label(window,text='AMOUNT TO PAY',font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
            amount.place(x=100,y=280)
            

            invoi_id1=Label(window,text=i_invoice_id,font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
            invoi_id1.place(x=500,y=160)
            cust_id1=Label(window,text=i_customer_id,font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
            cust_id1.place(x=500,y=180)
            seri1=Label(window,text=i_car_serial,font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
            seri1.place(x=500,y=200)
            insure1=Label(window,text=i_insurance,font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
            insure1.place(x=500,y=220)
            price1=Label(window,text=i_price,font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
            price1.place(x=500,y=240)
            day1=Label(window,text=i_date,font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
            day1.place(x=500,y=260)
            amount1=Label(window,text=amount_to_pay,font=('Times New Roman',14,'bold'),bg='light pink',fg='black')
            amount1.place(x=500,y=280)
            pay=Button(window,text="Proceed Payment",width=15,bg='green',fg='black',command=payment)
            pay.place(x=500,y=380)

            return
        insu=Button(window,text="Claim Insurance",width=15,bg='pink',fg='black',command=insurance)
        insu.place(x=100,y=80)
        proceed=Button(window,text="Sales Invoice",width=15,bg='pink',fg='black',command=invoice)
        proceed.place(x=500,y=80)
    buy.mainloop()
    return

def purchased_buys():
    print(customer_id)
    pur=Tk()
    pur.title("MY CAR DETAILS")
    pur.geometry('880x600+330+10')
    pur.resizable(0,0)
    lbl=Label(pur,bg='light pink')
    lbl.place(x=0,y=0,relwidth=1,relheight=1)
    heading=Label(pur,text='Purchased Cars',font=('Arial',20,'bold'),bg='light pink',fg='firebrick1')
    heading.place(x=300,y=40)
    conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
    cur=conn.cursor()
    query="SELECT COUNT(*) FROM SALES_INVOICE WHERE CUSTOMER_ID=%s AND CUSTOMER_ID=%s"
    cur.execute(query,(customer_id,customer_id))
    row=cur.fetchone()
    num=row[0]
    if num==0:
        messagebox.showinfo('Not bought yet','We will help you to buy a new car')
    else:
        query1="SELECT INVOICE_ID,CAR_SERIALNO FROM SALES_INVOICE WHERE CUSTOMER_ID=%s AND CUSTOMER_ID=%s"
        cur.execute(query1,(customer_id,customer_id))
        var=cur.fetchall()
        voice_id=var[0][0]
        query2="SELECT PAYMENT_DATE FROM PAYMENT WHERE INVOICE_ID=%s AND BALANCE=%s"
        cur.execute(query2,(voice_id,0))
        vari=cur.fetchall()
        if vari==None:
            messagebox.showinfo('Not yet bought','We will help you to buy a new car',parent=cus)
        else:
            purchase_date=vari[0][0]
            car_serial=var[0][1]
            query3="SELECT BRAND,MODEL,COLOUR,YEAR,PRICE FROM CAR WHERE SERIAL_NUM=%s AND SERIAL_NUM=%s"
            cur.execute(query3,(car_serial,car_serial))
            det=cur.fetchall()
            brand=det[0][0]
            model=det[0][1]
            colour=det[0][2]
            year=det[0][3]
            price=det[0][4]
            print(voice_id,car_serial,purchase_date,brand,model,colour,year,price)
            Label(pur,text='INVOICE ID',font=('Times New Roman',18),bg='light pink',fg='black').place(x=20,y=180)
            Label(pur,text='PURCHASE DATE',font=('Times New Roman',18),bg='light pink',fg='black').place(x=20,y=220)
            Label(pur,text='CAR SERIAL NUMBER',font=('Times New Roman',18),bg='light pink',fg='black').place(x=20,y=260)
            Label(pur,text='BRAND',font=('Times New Roman',18),bg='light pink',fg='black').place(x=20,y=300)
            Label(pur,text='MODEL',font=('Times New Roman',18),bg='light pink',fg='black').place(x=20,y=340)
            Label(pur,text='COLOUR',font=('Times New Roman',18),bg='light pink',fg='black').place(x=20,y=380)
            Label(pur,text='YEAR',font=('Times New Roman',18),bg='light pink',fg='black').place(x=20,y=420)
            Label(pur,text='PRICE',font=('Times New Roman',18),bg='light pink',fg='black').place(x=20,y=460)
            Label(pur,text='PAYMENT STATUS',font=('Times New Roman',18),bg='light pink',fg='black').place(x=20,y=500)
            Label(pur,text=voice_id,font=('Times New Roman',18),bg='light pink',fg='black').place(x=420,y=180)
            Label(pur,text=purchase_date,font=('Times New Roman',18),bg='light pink',fg='black').place(x=420,y=220)
            Label(pur,text=car_serial,font=('Times New Roman',18),bg='light pink',fg='black').place(x=420,y=260)
            Label(pur,text=brand,font=('Times New Roman',18),bg='light pink',fg='black').place(x=420,y=300)
            Label(pur,text=model,font=('Times New Roman',18),bg='light pink',fg='black').place(x=420,y=340)
            Label(pur,text=colour,font=('Times New Roman',18),bg='light pink',fg='black').place(x=420,y=380)
            Label(pur,text=year,font=('Times New Roman',18),bg='light pink',fg='black').place(x=420,y=420)
            Label(pur,text=price,font=('Times New Roman',18),bg='light pink',fg='black').place(x=420,y=460)
            Label(pur,text='PAID',font=('Times New Roman',18),bg='light pink',fg='black').place(x=420,y=500)

    conn.commit()
    conn.close()
    return

def sign_up():
    
    sign_win=Tk()
    sign_win.title("CREATE ACCOUNT")
    sign_win.geometry('880x600+330+10')
    sign_win.resizable(0,0)
    lbl=Label(sign_win,bg='light pink')
    lbl.place(x=0,y=0,relwidth=1,relheight=1)
    
    heading=Label(sign_win,text='CREATE CUSTOMER ACCOUNT',font=('Arial',20,'bold'),bg='light pink',fg='firebrick1')
    heading.place(x=245,y=20)
    nameLabel=Label(sign_win,text='Customer Name*',font=('Times New Roman',10,'italic'),bg='light pink',fg='black')
    nameLabel.place(x=200,y=80)
    nameEntry=Entry(sign_win,width=25,font=('Times New Roman',11,'bold'),bd=0)
    nameEntry.place(x=200,y=100)

    userLabel=Label(sign_win,text='Username*',font=('Times New Roman',10,'italic'),bg='light pink',fg='black')
    userLabel.place(x=200,y=140)
    userEntry=Entry(sign_win,width=25,font=('Times New Roman',11,'bold'),bd=0)
    userEntry.place(x=200,y=160)

    passLabel=Label(sign_win,text='Password*',font=('Times New Roman',10,'italic'),bg='light pink',fg='black')
    passLabel.place(x=200,y=200)
    passEntry=Entry(sign_win,width=25,font=('Times New Roman',11,'bold'),bd=0)
    passEntry.place(x=200,y=220)

    aadharLabel=Label(sign_win,text='Aadhar Number*',font=('Times New Roman',10,'italic'),bg='light pink',fg='black')
    aadharLabel.place(x=200,y=260)
    aadharEntry=Entry(sign_win,width=25,font=('Times New Roman',11,'bold'),bd=0)
    aadharEntry.place(x=200,y=280)

    phoneLabel=Label(sign_win,text='Phone Number 1*',font=('Times New Roman',10,'italic'),bg='light pink',fg='black')
    phoneLabel.place(x=200,y=320)
    phoneEntry=Entry(sign_win,width=25,font=('Times New Roman',11,'bold'),bd=0)
    phoneEntry.place(x=200,y=340)

    phoneLabel2=Label(sign_win,text='Phone Number 2',font=('Times New Roman',10,'italic'),bg='light pink',fg='black')
    phoneLabel2.place(x=200,y=380)
    phoneEntry2=Entry(sign_win,width=25,font=('Times New Roman',11,'bold'),bd=0)
    phoneEntry2.place(x=200,y=400)

    phoneLabel3=Label(sign_win,text='Phone Number 3',font=('Times New Roman',10,'italic'),bg='light pink',fg='black')
    phoneLabel3.place(x=200,y=440)
    phoneEntry3=Entry(sign_win,width=25,font=('Times New Roman',11,'bold'),bd=0)
    phoneEntry3.place(x=200,y=460)

    emailLabel=Label(sign_win,text='Email Id 1*',font=('Times New Roman',10,'italic'),bg='light pink',fg='black')
    emailLabel.place(x=200,y=500)
    emailEntry=Entry(sign_win,width=25,font=('Times New Roman',11,'bold'),bd=0)
    emailEntry.place(x=200,y=520)

    emailLabel2=Label(sign_win,text='Email Id 2',font=('Times New Roman',10,'italic'),bg='light pink',fg='black')
    emailLabel2.place(x=500,y=80)
    emailEntry2=Entry(sign_win,width=25,font=('Times New Roman',11,'bold'),bd=0)
    emailEntry2.place(x=500,y=100)

    cityLabel=Label(sign_win,text='City*',font=('Times New Roman',10,'italic'),bg='light pink',fg='black')
    cityLabel.place(x=500,y=140)
    cityEntry=Entry(sign_win,width=25,font=('Times New Roman',11,'bold'),bd=0)
    cityEntry.place(x=500,y=160)

    stateLabel=Label(sign_win,text='State*',font=('Times New Roman',10,'italic'),bg='light pink',fg='black')
    stateLabel.place(x=500,y=200)
    stateEntry=Entry(sign_win,width=25,font=('Times New Roman',11,'bold'),bd=0)
    stateEntry.place(x=500,y=220)

    countryLabel=Label(sign_win,text='Country*',font=('Times New Roman',10,'italic'),bg='light pink',fg='black')
    countryLabel.place(x=500,y=260)
    countryEntry=Entry(sign_win,width=25,font=('Times New Roman',11,'bold'),bd=0)
    countryEntry.place(x=500,y=280)

    pinLabel=Label(sign_win,text='Pincode*',font=('Times New Roman',10,'italic'),bg='light pink',fg='black')
    pinLabel.place(x=500,y=320)
    pinEntry=Entry(sign_win,width=25,font=('Times New Roman',11,'bold'),bd=0)
    pinEntry.place(x=500,y=340)

    def entry():
        if nameEntry.get()=='' or userEntry.get()=='' or passEntry.get()=='' or aadharEntry.get()=='' or cityEntry.get()=='' or stateEntry.get()=='' or countryEntry.get()=='' or pinEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='':
            messagebox.showerror("Error","Required all fields")
        else:
            conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
            cur=conn.cursor()
            cur.execute("SELECT COUNT(*) FROM CUSTOMER")
            res=cur.fetchone()
            ress=str(res[0]+1)
            mark="CUS"
            id=mark+ress
            query1="INSERT INTO CUSTOMER(CUSTOMER_ID,CUSTOMER_NAME,AADHAR_NUMBER,USERNAME,PASSWORD,CITY,STATE,COUNTRY,PINCODE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(query1,(id,nameEntry.get(),aadharEntry.get(),userEntry.get(),passEntry.get(),cityEntry.get(),stateEntry.get(),countryEntry.get(),pinEntry.get()))
            query2="INSERT INTO CUSTOMER_PHONE(CUSTOMER_ID,PHONE_NUMBER) VALUES(%s,%s)"
            cur.execute(query2,(id,phoneEntry.get()))
            query3="INSERT INTO CUSTOMER_EMAIL(CUSTOMER_ID,EMAIL_ID) VALUES(%s,%s)"
            cur.execute(query3,(id,emailEntry.get()))
            if phoneEntry2.get()!='':
                query4="INSERT INTO CUSTOMER_PHONE(CUSTOMER_ID,PHONE_NUMBER) VALUES(%s,%s)"
                cur.execute(query4,(id,phoneEntry2.get()))
            if phoneEntry3.get()!='':
                query5="INSERT INTO CUSTOMER_PHONE(CUSTOMER_ID,PHONE_NUMBER) VALUES(%s,%s)"
                cur.execute(query5,(id,phoneEntry3.get()))
            if emailEntry2.get()!='':
                query6="INSERT INTO CUSTOMER_EMAIL(CUSTOMER_ID,EMAIL_ID) VALUES(%s,%s)"
                cur.execute(query6,(id,emailEntry2.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Welcome","Account created succesfully")
            sign_win.destroy()

    but=Button(sign_win,text='Sign Up',width=20,bg='firebrick1',fg='black',command=entry)
    but.place(x=525,y=400)

    sign_win.mainloop()

def login():
    if userEntry.get()==(''or'Username') or passEntry.get()==(''or'Password'):
        messagebox.showerror("Error","All Fields are required")
    else:
        conn=psycopg2.connect(host="localhost",database="CDS",user="postgres",port="5432",password="07@April@2005")
        cur=conn.cursor()
        query="SELECT * FROM CUSTOMER WHERE USERNAME=%s AND PASSWORD=%s"
        cur.execute(query,(userEntry.get(),passEntry.get()))
        row=cur.fetchone()
        username=row[1]
        global customer_id
        customer_id=row[0]
        conn.commit()
        conn.close()
        if row==None:
            messagebox.showerror("Error","Invalid username or password")
        else:
            mer=Tk()
            mer.title("MM CUSTOMER")
            mer.geometry('880x600+320+0')
            mer.resizable(0,0)
            lbl=Label(mer,bg='light pink')
            lbl.place(x=0,y=0,relwidth=1,relheight=1)
            messagebox.showinfo("Welcome","Login is successful",parent=mer)
            cus.destroy()
            w="Welcome "
            s=w+username
            heading=Label(mer,text=s,font=('Arial',20,'bold'),bg='light pink',fg='navy')
            heading.place(x=40,y=80)
            add=Button(mer,text='Buy Car',width=20,height=5,bg='hot pink',activebackground='grey',command=buy_buy)
            add.place(x=100,y=200)
            activity=Button(mer,text='Purchased Car',width=20,height=5,bg='hot pink',activebackground='grey',command=purchased_buys)
            activity.place(x=300,y=200)
            mer.mainloop()
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
            query="SELECT * FROM CUSTOMER NATURAL JOIN CUSTOMER_PHONE WHERE USERNAME=%s AND PHONE_NUMBER=%s"
            cur.execute(query,(userEntry.get(),phoneEntry.get()))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect username or phone number',parent=window)
            else:
                query="UPDATE CUSTOMER SET PASSWORD=%s WHERE USERNAME=%s"
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
    lbl1=Label(window,bg='light pink')
    lbl1.place(x=0,y=0,relwidth=1,relheight=1)

    heading=Label(window,text='RESET PASSWORD',font=('Arial',20,'bold'),bg='light pink',fg='firebrick2')
    heading.place(x=20,y=80)

    userLabel=Label(window,text='Username*',font=('Times New Roman',10,'italic'),bg='light pink',fg='black')
    userLabel.place(x=20,y=140)
    userEntry=Entry(window,width=25,font=('Times New Roman',11,'bold'),bd=0,bg='light pink')
    userEntry.place(x=20,y=160)
    f1=Frame(window,width=250,height=2,bg='black')
    f1.place(x=20,y=180)

    passLabel=Label(window,text='Password*',font=('Times New Roman',10,'italic'),bg='light pink',fg='black')
    passLabel.place(x=20,y=200)
    passEntry=Entry(window,width=25,font=('Times New Roman',11,'bold'),bd=0,bg='light pink')
    passEntry.place(x=20,y=220)
    f2=Frame(window,width=250,height=2,bg='black')
    f2.place(x=20,y=240)

    passLabel1=Label(window,text='Confirm Password*',font=('Times New Roman',10,'italic'),bg='light pink',fg='black')
    passLabel1.place(x=20,y=260)
    passEntry1=Entry(window,width=25,font=('Times New Roman',11,'bold'),bd=0,bg='light pink')
    passEntry1.place(x=20,y=280)
    f4=Frame(window,width=250,height=2,bg='black')
    f4.place(x=20,y=300)

    phoneLabel=Label(window,text='Phone number*',font=('Times New Roman',10,'italic'),bg='light pink',fg='black')
    phoneLabel.place(x=20,y=320)
    phoneEntry=Entry(window,width=25,font=('Times New Roman',11,'bold'),bd=0,bg='light pink')
    phoneEntry.place(x=20,y=340)
    f3=Frame(window,width=250,height=2,bg='black')
    f3.place(x=20,y=360)
    
    submitButton=Button(window,text='SUBMIT',font=('Times New Roman',11,'bold'),bd=0,
                   bg='firebrick2',activebackground='black',cursor='hand2',activeforeground='red',width=27,height=1,command=reset_password)
    submitButton.place(x=20,y=400)
    return
cus=Tk()
cus.title("CUSTOMER LOGIN")
cus.geometry('880x600+320+0')
cus.resizable(0,0)
lbl=Label(cus,bg='light pink')
lbl.place(x=0,y=0,relwidth=1,relheight=1)

img=PhotoImage(file="C:/Users/SORNAMALYA SIVAKUMAR/Downloads/acc-removebg-preview.png")
label=Label(cus,image=img,bg='light pink')
label.place(x=100,y=0,relwidth=1,relheight=1)

heading=Label(cus,text='CUSTOMER LOGIN',font=('Arial',20,'bold'),bg='light pink',fg='firebrick2')
heading.place(x=20,y=80)

userEntry=Entry(cus,width=25,font=('Times New Roman',11,'bold'),bd=0,bg='light pink')
userEntry.place(x=20,y=160)
userEntry.insert(0,'Username')
userEntry.bind('<FocusIn>',user_entry)
f1=Frame(cus,width=250,height=2,bg='black')
f1.place(x=20,y=180)

passEntry=Entry(cus,width=25,font=('Times New Roman',11,'bold'),bd=0,bg='light pink')
passEntry.place(x=20,y=220)
passEntry.insert(0,'Password')
passEntry.bind('<FocusIn>',pass_entry)
f2=Frame(cus,width=250,height=2,bg='black')
f2.place(x=20,y=240)

forgetButton=Button(cus,text='Forgot Password',bd=0,bg='light pink',activebackground='light pink',activeforeground='black',
                    cursor='hand2',font=('Times New Roman',11,'bold'),fg='red',command=forget_password)
forgetButton.place(x=20,y=260)

loginButton=Button(cus,text='Login',font=('Times New Roman',11,'bold'),bd=0,
                   bg='firebrick2',activebackground='black',cursor='hand2',activeforeground='red',width=27,height=1,command=login)
loginButton.place(x=20,y=300)

accButton=Button(cus,text="Don't have an account?",bd=0,bg='light pink',activebackground='light pink',
                    cursor='hand2',font=('Times New Roman',8,'bold'),fg='blue2')
accButton.place(x=20,y=420)

newAccButton=Button(cus,text='Create new One',bd=0,bg='light pink',activebackground='light pink',
                    cursor='hand2',font=('Times New Roman',11,'bold'),fg='DeepPink4',command=sign_up)
newAccButton.place(x=150,y=420)

cus.mainloop()