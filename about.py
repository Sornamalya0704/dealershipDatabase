from tkinter import*
import tkinter as tk
abt=Tk()
abt.title("ABOUT")
abt.geometry('880x600+320+0')
abt.resizable(0,0)
lbl=Label(abt,bg='pink1')
lbl.place(x=0,y=0,relwidth=1,relheight=1)

heading=Label(abt,text='about...',font=('Times New Roman',20,),bg='pink1',fg='black')
heading.place(x=40,y=40)

T=Text(abt,height=20,width=100,bg='pink1',pady=0,border=0)
text="""
            VISHVAAS MM CARS is the multi franchise automobile sales organization
      that is dedicated to creating life long customers. We all recognize that to 
      achieve this ,we must provide exceptional automotive for our customers, and 
      the very comfort work place for our team members. We are committed, through 
      the support and service to actively improve the greater community; and will 
      continually work to earn the respect and trust of our customers , employees 
      and their families. ZINDAGEE MM CARS will always be driven by fairness, the 
      recognition of diversity and respect for the individual.

            Authorized MM Car Dealers in Tamil Nadu to buy a new Branded cars. To 
      get On the Road Price please submit all your details to our executive , Our 
      Executive will send you the pricing details shortly for your mail.

      Locations: Coimbatore, Tirupur, Erode, Salem, Madurai, Trichy & Tirunelveli.
      Phone : +91 95002 36559
      Phone : 095006 05222"""
T.place(x=60,y=100)
T.insert(tk.END,text)
T.config(state=DISABLED)
abt.mainloop()