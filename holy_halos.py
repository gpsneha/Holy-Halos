from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="root",database="puja_booking")
cur=con.cursor(buffered=True)


#cur.execute("create table Puja( puja_code int, puja_name varchar(20) not null, puja_amount int, pdevotee_name varchar(20), pphn_num int, pnakshatra varchar(20) not null, prashi varchar(20) not null, puja_time double(10,2), puja_day int, puja_month varchar(20) not null, puja_year int)");
#cur.execute("create table Seva( seva_code int, seva_name varchar(20) not null, seva_amount int, sdevotee_name varchar(20), sphn_num int primary key, snakshatra varchar(20) not null, srashi varchar(20) not null, seva_time double(10,2), seva_day int, seva_month varchar(20) not null, seva_year int)");    

    
def Sregistration():
    cur.execute("INSERT INTO seva VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(textin12.get(), textin13.get(), textin14.get(), textin15.get(), textin16.get(), textin17.get(), textin18.get(), textin19.get(), textin20.get(), textin21.get(), textin22.get()))
    con.commit()

def Sbooking_status():    
    if textin12.get()==0 or textin13.get()==0 or textin14.get()==0 or textin15.get()==0 or textin16.get()==0 or textin17.get()==0 or textin18.get()==0 or textin19.get()==0 or textin20.get()==0 or textin21.get()==0 or textin22.get()==" ":
        messagebox.showinfo(title="Seva Booking Status",message="Please fill all the required fields")
    else:
        messagebox.showinfo(title="Seva Booking Status",message="Your Seva is sucecessfully booked")

def Sregistration_and_Sbooking_status():
     Sbooking_status()
     Sregistration()


def Pregistration():
    cur.execute("INSERT INTO puja VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(textin1.get(), textin2.get(), textin3.get(), textin4.get(), textin5.get(), textin6.get(), textin7.get(), textin8.get(), textin9.get(), textin10.get(), textin11.get()))
    con.commit()

def Pbooking_status():
    if textin1.get()==0 or textin2.get()==0 or textin3.get()==0 or textin4.get()==0 or textin5.get()==0 or textin6.get()==0 or textin7.get()==0 or textin8.get()==0 or textin9.get()==0 or textin10.get()==0 or textin12.get()==" ":
        messagebox.showinfo(title="Puja Booking Status",message="Please fill all the required fields")
    else:
        messagebox.showinfo(title="Puja Booking Status",message="Your Puja is sucecessfully booked")

def Pregistration_and_Pbooking_status():
    Pbooking_status()
    Pregistration()

def pclose_window():
    root.destroy()

def sclose_window():
    root.destroy()
    
def Preciept_details():
    con.cursor()
    pname=textin23.get()
    cur.execute("SELECT pdevotee_name, puja_name, puja_time, puja_day, puja_month, puja_year, puja_amount FROM puja WHERE pphn_num=%s", (pname,)) 
    result_set=cur.fetchall()
    top4=Toplevel()
    top4.title("PUJA RECIEPT")
    top4.geometry("700x350")
    label = Label(top4, text = "WELCOME TO MANTRALAYA SERVICES", font=("Times New Roman",18), bg='white', fg='red').place(x=130,y=20)
    label1 = Label(top4, text = "PUJA RECIEPT", font=("Times New Roman",18), bg='white', fg='red').place(x=250,y=70)
    trv=ttk.Treeview(top4, height=8, selectmode='browse')
    trv.grid(row=1,column=1,padx=30,pady=120)
    trv["column"]=("1","2","3","4","5","6","7")
    trv['show']='headings'
    trv.column("1",width=120,anchor='c')
    trv.column("2",width=120,anchor='c')
    trv.column("3",width=80,anchor='c')
    trv.column("4",width=80,anchor='c')
    trv.column("5",width=80,anchor='c')
    trv.column("6",width=80,anchor='c')
    trv.column("7",width=80,anchor='c')
    trv.heading("1",text="Name")
    trv.heading("2",text="Puja name")
    trv.heading("3",text="Time")
    trv.heading("4",text="Day")
    trv.heading("5",text="Month")
    trv.heading("6",text="Year")
    trv.heading("7",text="Total Amount")
    
    for i in result_set:
        trv.insert("",'end',iid=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
       
    con.commit()    

def Sreciept_details():
    con.cursor()
    sname=textin24.get()
    cur.execute("SELECT sdevotee_name, seva_name, seva_time, seva_day, seva_month, seva_year, seva_amount FROM seva WHERE sphn_num=%s", (sname,)) 
    results=cur.fetchall()
    top5=Toplevel()
    top5.title("SEVA RECIEPT")
    top5.geometry("700x350")
    label = Label(top5, text = "WELCOME TO MANTRALAYA SERVICES", font=("Times New Roman",18), bg='white', fg='red').place(x=130,y=20)
    label1 = Label(top5, text = "SEVA RECIEPT", font=("Times New Roman",18), bg='white', fg='red').place(x=250,y=70)
    trv=ttk.Treeview(top5, height=8, selectmode='browse')
    trv.grid(row=1,column=1,padx=30,pady=120)
    trv["column"]=("1","2","3","4","5","6","7")
    trv['show']='headings'
    trv.column("1",width=100,anchor='c')
    trv.column("2",width=110,anchor='c')
    trv.column("3",width=80,anchor='c')
    trv.column("4",width=80,anchor='c')
    trv.column("5",width=80,anchor='c')
    trv.column("6",width=80,anchor='c')
    trv.column("7",width=80,anchor='c')
    trv.heading("1",text="Name")
    trv.heading("2",text="Seva name")
    trv.heading("3",text="Time")
    trv.heading("4",text="Day")
    trv.heading("5",text="Month")
    trv.heading("6",text="Year")
    trv.heading("7",text="Total Amount")
    for i in results:
        trv.insert("",'end',iid=i[0],values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    con.commit()    

        
root=Tk()
root.title("WELCOME TO MANTHRALAYA SERVICES")
root.geometry("500x500")



textin1=IntVar()
textin2=StringVar()
textin3=IntVar()
textin4=StringVar()
textin5=IntVar()
textin6=StringVar()
textin7=StringVar()
textin8=DoubleVar()
textin9=IntVar()
textin10=StringVar()
textin11=IntVar()


textin12=IntVar()
textin13=StringVar()
textin14=IntVar()
textin15=StringVar()
textin16=IntVar()
textin17=StringVar()
textin18=StringVar()
textin19=DoubleVar()
textin20=IntVar()
textin21=StringVar()
textin22=IntVar()

textin23=IntVar()
textin24=IntVar()


bg=PhotoImage(file="C:\\Users\\DELL\\Pictures\\SnehaGP.GIF")
my_label=Label(root,image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)

def godinfo():
    key=Tk()
    key.title("GODS")
    key.geometry("250x400")
    key.eval('tk::PlaceWindow . center')
    listbox = Listbox(key, height = 14, width = 20, bg = "grey", activestyle = 'dotbox', font = "Helvetica",fg = "yellow")
    label = Label(key, text = "WORSHIPPING GODS") 
    listbox.insert(1, "Lord Rama")
    listbox.insert(2, "Lord Ganesha")
    listbox.insert(3, "Durga Devi")
    listbox.insert(4, "Lord Shiva")
    listbox.insert(5, "Lakshmi Devi")
    listbox.insert(6, "Lord Krishna")
    listbox.insert(7, "Lord Brahma")
    listbox.insert(8, "Saraswati Devi")
    listbox.insert(9, "Lord Vishnu")
    listbox.insert(10, "Parvati Devi")
    listbox.insert(11, "Radha Devi")
    listbox.insert(12, "Sita Devi")
    listbox.insert(13, "Lord Venkateshwara")
    listbox.insert(14, "Lord Satya Narayana")
    label.pack()
    listbox.pack()
    key.mainloop()
    
    

def festinfo():
    key=Tk()
    key.title("FESTIVALS")
    key.geometry("250x300")
    key.eval('tk::PlaceWindow . center')
    listbox = Listbox(key, height = 11, width = 20, bg = "grey", activestyle = 'dotbox', font = "Helvetica",fg = "yellow")
    label = Label(key, text = "FESTIVALS CELEBRATED") 
    listbox.insert(1, "Rath Yatra")
    listbox.insert(2, "Diwali")
    listbox.insert(3, "Rama Navami")
    listbox.insert(4, "Maha Sankranti")
    listbox.insert(5, "Basant Panchami")
    listbox.insert(6, "Maha Shivratri")
    listbox.insert(7, "Janmashtami")
    listbox.insert(8, "Ganesh Chaturthi")
    listbox.insert(9, "Durga Pooja")
    listbox.insert(10, "Brahmotsavam festival")
    listbox.insert(11, "Vasant Chaitra Navaratri")
    label.pack()
    listbox.pack()
    key.mainloop()


    
def pujainfo():
    key=Tk()
    key.title("PUJAS")
    key.geometry("250x300")
    key.eval('tk::PlaceWindow . center')
    listbox = Listbox(key, height = 11, width = 20, bg = "grey", activestyle = 'dotbox', font = "Helvetica",fg = "yellow")
    label = Label(key, text = "PUJA INFORMATION") 
    listbox.insert(1, "Maha Mangala Aarati")
    listbox.insert(2, "Archana puja")
    listbox.insert(3, "Kunkum Puja")
    listbox.insert(4, "Satyanarayan puja")
    listbox.insert(5, "Pancham Snan puja")
    listbox.insert(6, "Rudrabhisheka puja")
    listbox.insert(7, "Kanaka Maha puja")
    listbox.insert(8, "Padya puja")
    listbox.insert(9, "Avahana puja")
    listbox.insert(10, "Vishesha puja")
    label.pack()
    listbox.pack()
    key.mainloop()
  

def sevainfo():
    key=Tk()
    key.title("SEVAS")
    key.geometry("250x300")
    key.eval('tk::PlaceWindow . center')
    listbox = Listbox(key, height = 11, width = 20, bg = "grey", activestyle = 'dotbox', font = "Helvetica",fg = "yellow")
    label = Label(key, text = "SEVA INFORMATION") 
    listbox.insert(1, "Suprabata Seva")
    listbox.insert(2, "Sarva Seva")
    listbox.insert(3, "Thomala Seva")
    listbox.insert(4, "Ekantha Seva")
    listbox.insert(5, "Pushpayagam Seva")
    listbox.insert(6, "Arjitha Seva")
    listbox.insert(7, "Nandadeepa Seva")
    listbox.insert(8, "Maha Naivedya Seva")
    listbox.insert(9, "Poorna Seva")
    listbox.insert(10, "Sahasra Kalabhishekam Seva")
    label.pack()
    listbox.pack()
    key.mainloop()



def pujacode():
    key=Tk()
    key.title("PUJAS")
    key.geometry("300x280")
    key.eval('tk::PlaceWindow . center')
    listbox = Listbox(key, height = 10, width = 60, bg = "grey", activestyle = 'dotbox', font = "Helvetica",fg = "yellow")
    label = Label(key, text = "PUJA CODES") 
    listbox.insert(1, "Maha Mangala Aarati    :      101")
    listbox.insert(2, "Archana puja                :      102")
    listbox.insert(3, "Kunkum Puja                :      103")
    listbox.insert(4, "Satyanarayan puja        :      104")
    listbox.insert(5, "Pancham Snan puja      :      105")
    listbox.insert(6, "Rudrabhisheka puja      :      106")
    listbox.insert(7, "Kanaka Maha puja        :      107")
    listbox.insert(8, "Padya puja                   :      108")
    listbox.insert(9, "Avahana puja                :      109")
    listbox.insert(10,"Vishesha puja               :       110")
    label.pack()
    listbox.pack()
    key.mainloop()  
    

def pujaamount():
    key=Tk()
    key.title("PUJAS")
    key.geometry("420x300")
    key.eval('tk::PlaceWindow . center')
    listbox = Listbox(key, height = 10, width = 60, bg = "grey", activestyle = 'dotbox', font = "Helvetica",fg = "yellow")
    label = Label(key, text = "PUJA AMOUNT") 
    listbox.insert(1, "Maha Mangala Aarati  :      Rs.500")
    listbox.insert(2, "Archana puja              :      Rs.300")
    listbox.insert(3, "Kunkum Puja              :      Rs.800")
    listbox.insert(4, "Satyanarayan puja      :      Rs.2000")
    listbox.insert(5, "Pancham Snan puja     :      Rs.3500")
    listbox.insert(6, "Rudrabhisheka puja     :      Rs.5000")
    listbox.insert(7, "Kanaka Maha puja       :      Rs.4500")
    listbox.insert(8, "Padya puja                  :      Rs.3300")
    listbox.insert(9, "Avahana puja               :      Rs.2500")
    listbox.insert(10,"Vishesha puja              :      Rs.5500")
    label.pack()
    listbox.pack()
    key.mainloop()  


def open_pwindow():
    top=Toplevel()
    top.title("POOJA BOOKING")
    top.geometry("450x450")
    Pcode=Label(top,text="Puja Code").place(x=30,y=50)
    Pname=Label(top,text="Puja Name").place(x=30,y=90)
    Pamount=Label(top,text="Puja Amount").place(x=30,y=130)
    Pdname=Label(top,text="Devotee Name").place(x=30,y=170)
    Pphnnumber=Label(top,text="Phone Number").place(x=30,y=210)
    Pnakshatra=Label(top,text="Associated stars").place(x=30,y=250)
    Prashi=Label(top,text="Zodaic Sign").place(x=30,y=290)
    Ptime=Label(top,text="Puja Time").place(x=30,y=330)
    Pday=Label(top,text="Day").place(x=30,y=370)
    Pmonth=Label(top,text="Month").place(x=120,y=370)
    Pyear=Label(top,text="Year").place(x=250,y=370)
    e1=Entry(top, textvar=textin1).place(x=120,y=50)
    e2=Entry(top, textvar=textin2).place(x=120,y=90)
    e3=Entry(top, textvar=textin3 ).place(x=120,y=130)
    e4=Entry(top, textvar=textin4).place(x=120,y=170)
    e5=Entry(top, textvar=textin5).place(x=120,y=210)
    e6=Entry(top, textvar=textin6).place(x=120,y=250)
    e7=Entry(top, textvar=textin7).place(x=120,y=290)
    e8=Entry(top, textvar=textin8).place(x=120,y=330)
    e9=Entry(top, width=5, textvar=textin9).place(x=70,y=370)
    e10=Entry(top, width=10, textvar=textin10).place(x=170,y=370)
    e11=Entry(top, width=5, textvar=textin11).place(x=280,y=370)
    but1=Button(top, text="Submit", fg="white", bg="blue", command=Pregistration_and_Pbooking_status)
    but1.place(x=50,y=410)
    but2=Button(top, text="Cancel", fg="white", bg="blue", command=pclose_window)
    but2.place(x=130,y=410)
    but3=Button(top, text="Clear", fg="white", bg="blue")
    but3.place(x=210,y=410)


def sevacode():
     key=Tk()
     key.title("SEVAS")
     key.geometry("400x300")
     key.eval('tk::PlaceWindow . center')
     listbox = Listbox(key, height = 11, width = 60, bg = "grey", activestyle = 'dotbox', font = "Helvetica",fg = "yellow")
     label = Label(key, text = "SEVA CODES") 
     listbox.insert(1, "Suprabata Seva                      :      201")
     listbox.insert(2, "Sarva Seva                             :      202")
     listbox.insert(3, "Thomala Seva                         :      203")
     listbox.insert(4, "Ekantha Seva                          :      204")
     listbox.insert(5, "Pushpayagam Seva                 :      205")
     listbox.insert(6, "Arjitha Seva                             :      206")
     listbox.insert(7, "Nandadeepa Seva                    :      207")
     listbox.insert(8, "Maha Naivedya Seva                :      208")
     listbox.insert(9, "Poorna Seva                            :      209")
     listbox.insert(10, "Sahasra Kalabhishekam Seva   :      210")
     label.pack()
     listbox.pack()
     key.mainloop()       

def sevaamount():
    key=Tk()
    key.title("SEVAS")
    key.geometry("420x300")
    key.eval('tk::PlaceWindow . center')
    listbox = Listbox(key, height = 11, width = 70, bg = "grey", activestyle = 'dotbox', font = "Helvetica",fg = "yellow")
    label = Label(key, text = "SEVA AMOUNT") 
    listbox.insert(1, "Suprabata Seva                        :      Rs.2500")
    listbox.insert(2, "Sarva Seva                               :      Rs.3000")
    listbox.insert(3, "Thomala Seva                           :      Rs.4500")
    listbox.insert(4, "Ekantha Seva                            :      Rs.3500")
    listbox.insert(5, "Pushpayagam Seva                   :      Rs.4000")
    listbox.insert(6, "Arjitha Seva                               :     Rs.5000")
    listbox.insert(7, "Nandadeepa Seva                     :      Rs.1800")
    listbox.insert(8, "Maha Naivedya Seva                 :      Rs.6000")
    listbox.insert(9, "Poorna Seva                             :      Rs.5500")
    listbox.insert(10, "Sahasra Kalabhishekam Seva    :      Rs.6500")
    label.pack()
    listbox.pack()
    key.mainloop()

def open_swindow():
    top1=Toplevel()
    top1.title("SEVA BOOKING")
    top1.geometry("450x450")
    Scode=Label(top1,text="Seva Code").place(x=30,y=50)
    Sname=Label(top1,text="Seva Name").place(x=30,y=90)
    Samount=Label(top1,text="Seva Amount").place(x=30,y=130)
    Sdname=Label(top1,text="Devotee Name").place(x=30,y=170)
    Sphnnumber=Label(top1,text="Phone Number").place(x=30,y=210)
    Snakshatra=Label(top1,text="Associated stars").place(x=30,y=250)
    Srashi=Label(top1,text="Zodaic Sign").place(x=30,y=290)
    Stime=Label(top1,text="Seva Time").place(x=30,y=330)
    Sday=Label(top1,text="Day").place(x=30,y=370)
    Smonth=Label(top1,text="Month").place(x=120,y=370)
    Syear=Label(top1,text="Year").place(x=250,y=370)
    e1=Entry(top1, textvar=textin12).place(x=120,y=50)
    e2=Entry(top1, textvar=textin13).place(x=120,y=90)
    e3=Entry(top1, textvar=textin14).place(x=120,y=130)
    e4=Entry(top1, textvar=textin15).place(x=120,y=170)
    e5=Entry(top1, textvar=textin16).place(x=120,y=210)
    e6=Entry(top1, textvar=textin17).place(x=120,y=250)
    e7=Entry(top1, textvar=textin18).place(x=120,y=290)
    e8=Entry(top1, textvar=textin19).place(x=120,y=330)
    e9=Entry(top1, width=5, textvar=textin20).place(x=70,y=370)
    e10=Entry(top1, width=10, textvar=textin21).place(x=170,y=370)
    e11=Entry(top1, width=5, textvar=textin22).place(x=280,y=370)
    but1=Button(top1, text="Submit", fg="white", bg="blue", command=Sregistration_and_Sbooking_status)
    but1.place(x=50,y=410)
    but2=Button(top1, text="Cancel", fg="white", bg="blue", command=sclose_window)
    but2.place(x=130,y=410)
    but3=Button(top1, text="Clear", fg="white", bg="blue")
    but3.place(x=210,y=410)


def Precieptcode():
    top2=Toplevel()
    top2.title("WELCOME TO MANTRALAYA SERVICES")
    top2.geometry("350x150")
    Pphone_number=Label(top2,text="Enter your Phone Number").place(x=30,y=50)
    e1=Entry(top2, textvar=textin23).place(x=200,y=50)
    but1=Button(top2, text="Print Reciept", fg="white", bg="blue", command=Preciept_details)
    but1.place(x=150, y=100)
    
def Srecieptcode():
    top3=Toplevel()
    top3.title("WELCOME TO MANTRALAYA SERVICES")
    top3.geometry("350x150")
    Sphone_number=Label(top3,text="Enter your Phone Number").place(x=30,y=50)
    e1=Entry(top3, textvar=textin24).place(x=200,y=50)
    but1=Button(top3, text="Print Reciept", fg="white", bg="blue", command=Sreciept_details)
    but1.place(x=150, y=100)
    
    
        
menubar=Menu(root)
TempleInformationmenu=Menu(menubar,tearoff=0)
TempleInformationmenu.add_command(label='Worshipping God', command=godinfo)
TempleInformationmenu.add_command(label='Festivals Celebrated',command=festinfo)
TempleInformationmenu.add_command(label='Puja Details',command=pujainfo)
TempleInformationmenu.add_command(label='Seva Details',command=sevainfo)
TempleInformationmenu.add_separator()
menubar.add_cascade(label='Temple Information',menu=TempleInformationmenu)


Sevamenu=Menu(menubar,tearoff=0)
Sevamenu.add_command(label='Seva Code',command=sevacode)
Sevamenu.add_command(label='Seva Amount',command=sevaamount)
Sevamenu.add_command(label='Book Seva',command=open_swindow)
Sevamenu.add_separator()
menubar.add_cascade(label='Seva Booking',menu=Sevamenu)

Pujamenu=Menu(menubar,tearoff=0)
Pujamenu.add_command(label='Puja Code',command=pujacode)
Pujamenu.add_command(label='Puja Amount',command=pujaamount)
Pujamenu.add_command(label='Book Puja',command=open_pwindow)
Pujamenu.add_separator()
menubar.add_cascade(label='Puja Booking',menu=Pujamenu)


Recieptmenu=Menu(menubar,tearoff=0)
Recieptmenu.add_command(label='Puja Reciept', command=Precieptcode)
Recieptmenu.add_command(label='Seva Reciept', command=Srecieptcode)
Recieptmenu.add_separator()
menubar.add_cascade(label='Reciept',menu=Recieptmenu)

root.config(menu=menubar)
root.mainloop()
