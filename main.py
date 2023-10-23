

from tkinter import *
from tkinter import ttk
import time
import datetime
from PIL import ImageTk,Image
import os
import sqlite3
from tkinter import messagebox
now = datetime.datetime.now()
#----------- importing sqlite for server side operations---------------------------------------------------------------------------------
con = sqlite3.Connection('hm_proj.db')
cur = con.cursor()
cur.execute("create table if not exists hoteld(t_r number,r_r number,t_s number)")
cur.execute("create table if not exists roomd(rn number primary key,beds number,ac varchar(10),tv varchar(10),internet varchar(10),price number(10))")

#pmethod=0

#rstatus extra column
#for i in range (1,21):
#cur.execute("update roomd set tv='Yes' where rn = ? ",(19,))
cur.execute("create table if not exists payments(id number primary key,dot varchar(15),time varchar(10),amt number,method varchar(10))")
cur.execute("create table if not exists paymentsf(id number  primary key,f_name varchar,l_name varchar,c_number varchar,email varchar , r_n number ,day varchar,month varchar,year varchar,time varchar , method varchar,totalamt varchar)")
#cur.execute("insert into paymentsf values(1,'Tushar','9817637698','tusharbhardwaj197@gmail.com',2,'1','11','2018','11:20:27 PM','Cash','3500')")
#cur.execute("alter table paymentsf add totalamt varchar")
con.commit()
#cur.execute("drop table paymentsf")
#cur.execute("insert into hoteld values(20,11,30)")
con.commit()
cur.execute("select * from payments")
con.commit()
x=cur.fetchall()
con.commit()
#print(x)
#-----------splash_screen------------------------------------------------------------------------------------------------------------------
sroot = Tk()
sroot.minsize(height=516,width=1150)
sroot.configure(bg='white')
spath = "images\My pic.jpg"
simg = ImageTk.PhotoImage(Image.open(spath))
my = Label(sroot,image=simg)
my.image = simg
my.place(x=0,y=0)
Frame(sroot,height=516,width=5,bg='black').place(x=520,y=0)
#chilanka
Label(sroot,text="Hotel Management System ",font='Timesnewroman 40 ',bg='white',fg='black').place(x=535,y=10)
Label(sroot,text="Made by -",font='Timesnewroman 40 ',bg='white',fg='black').place(x=535,y=90)
Label(sroot,text="Tushar",font='Timesnewroman 40 ',bg='white',fg='grey').place(x=535,y=180)
Label(sroot,text="tusharbhardwaj197@gmail.com",font='Timesnewroman 40',bg='white',fg='grey').place(x=535,y=270)
#Label(sroot,text="9817637698",font='Timesnewroman 40',bg='white',fg='grey').place(x=535,y=450)
#----------- main project------------------------------------------------------------------------------------------------------------------
def mainroot():
	#sroot.destroy()
	root = Tk()
	root.geometry('1080x500')
	root.minsize(width=1080,height=550)
	root.maxsize(width=1080,height=550)
	root.configure(bg='white')
	root.title("Hotel management system")
	#--------------seperator-------------------------------------------------------------------------------------------------------------------

	sep = Frame(height=500,bd=1,relief='sunken',bg='white')
	#sep.place(x=20,y=0)
	#----------------Connection with printer-------------------------------------------------------------------------------------------------------------

	def connectprinter():
		os.startfile("C:/Users/TestFile.txt", "print")
	#---------------top frame------------------------------------------------------------------------------------------------------------------

	top_frame = Frame(root,height=70,width=1080,bg='orange')
	path = "images/newestbg5.jpg"
	img = ImageTk.PhotoImage(Image.open(path))
	label = Label(top_frame,image = img ,height=70,width=1080)
	label.image=img
	label.place(x=0,y=0)
	top_frame.place(x=0,y=0)
	tf_label = Label(top_frame,text='Hotel Management System',font='msserif 33',fg='black',bg='gray89',height=70)
	tf_label.pack(anchor='center')
	top_frame.pack_propagate(False)

	#---------------DATE TIME------------------------------------------------------------------------------------------------------------------
	def datetime():
		#while(True):
		localtime = now.strftime("%Y-%m-%d %H:%M")
		lblInfo = Label(top_frame,font='helvetica 15',text=localtime,bg='blue',fg='white')
		#lblInfo.place(x=333,y=40)

	#----------------bottom frame - hotel status and default page-------------------------------------------------------------------------------
	def hotel_status():
		global b_frame
		b_frame = Frame(root,height=400,width=1080,bg='gray91')
		b_frame.place(x=0,y=120+6+20+60+11)
		b_frame.pack_propagate(False)
		path = "images/newbg6lf.jpg"
		img = ImageTk.PhotoImage(Image.open(path))
		label = Label(b_frame,image = img ,height=400,width=1080)
		label.image=img
		label.place(x=0,y=0)
		cur.execute("select * from hoteld")
		x = cur.fetchall()
		#print(x)
		cur.execute("select count(rn) from roomd")
		x = cur.fetchone()
		print (x)
		cur.execute("select count(rn) from roomd where rstatus = 'Reserved'")
		y = cur.fetchone()
		print (y)
		tor = x[0]
		rer = y[0]
		tos = 21
		avr = int(tor)-int(rer)
		avr = str(avr)
		#print(tor,rer,tos,avr)
		hts = Label(b_frame,text='Hotel Status',font='msserif 15',fg='black',bg='gray91',height=1)
	#------------inner frames of bottom frame-------------------------

		smf1 = Frame(b_frame,height=150,width=175,bg='white')
		tr = Label(smf1,text='Total Rooms:',fg='white',bg='cyan4',width=100,height=2,font='helvetica 15')
		tr.pack(side='top')
		smf1.pack_propagate(False)
		smf1.place(x=0,y=30)
		Label(smf1,text=tor,fg='cyan4',bg='white',font='msserif 50').pack(anchor='center')

		smf2 = Frame(b_frame,height=150,width=175,bg='white')
		ar = Label(smf2,text='Available Rooms:',fg='white',bg='cyan4',width=130,height=2,font='helvetica 15')
		ar.pack(side='top')
		smf2.pack_propagate(False)
		smf2.place(x=180+4,y=30)
		Label(smf2,text=avr,fg='cyan4',bg='white',font='msserif 50').pack(anchor='center')

		smf3 = Frame(b_frame,height=150,width=175,bg='white')
		tre = Label(smf3,text='Total reservations:',fg='white',bg='cyan4',width=130,height=2,font='helvetica 15')
		tre.pack(side='top')
		smf3.pack_propagate(False)
		smf3.place(x=360+6,y=30)
		Label(smf3,text=rer,fg='cyan4',bg='white',font='msserif 50').pack(anchor='center')

		smf4 = Frame(b_frame,height=150,width=175,bg='white')
		tc = Label(smf4,text='Total Customers:',fg='white',bg='cyan4',width=130,height=2,font='helvetica 15')
		tc.pack(side='top')
		smf4.pack_propagate(False)
		smf4.place(x=540+8,y=30)
		Label(smf4,text='40',fg='cyan4',bg='white',font='msserif 50').pack(anchor='center')

		smf5 = Frame(b_frame,height=150,width=175,bg='white')
		ts = Label(smf5,text='Total Staff:',fg='white',bg='cyan4',width=130,height=2,font='helvetica 15')
		ts.pack(side='top')
		smf5.pack_propagate(False)
		smf5.place(x=720+10,y=30)
		Label(smf5,text=tos,fg='cyan4',bg='white',font='msserif 50').pack(anchor='center')
		redf1 = Frame(b_frame,height=8,width=1080,bg='cyan4')

		smf6 = Frame(b_frame,height=150,width=175,bg='white')
		ts = Label(smf6,text='Under renovation:',fg='white',bg='cyan4',width=130,height=2,font='helvetica 15')
		ts.pack(side='top')
		smf6.pack_propagate(False)
		smf6.place(x=915,y=30)
		Label(smf6,text='3',fg='cyan4',bg='white',font='msserif 50').place(x=60,y=60)
		#redf1 = Frame(b_frame,height=8,width=1080,bg='cyan4')

		#Label(b_frame,text='==================================================================================',fg='cyan4').place(x=0,y=20)
		redf1.place(x=0,y=22)
		Label(b_frame,text='Hotel Status',font='msserif 12',bg='cyan4',fg='white').pack(anchor='center')
		redf1.pack_propagate(False)
		#b_frame.pack_propagate(False)

	#-----------------------------------------------------------------
		nl = Label(b_frame,text='made by tushar',fg='black',bg='gray91',font='msserif 8')
		nl.place(x=955,y=310)
		nl.tkraise()

	#-------------- Guests --------------------------------------------------------------------------------------------------------------------------
	def staff():
		b_frame = Frame(root,height=400,width=1080,bg='white')
		path = "images/newbg6lf.jpg"
		img = ImageTk.PhotoImage(Image.open(path))
		label = Label(b_frame,image = img ,height=400,width=1080)
		label.image=img
		label.place(x=0,y=0)
		l = Label(b_frame,text='Details of Staff will be Available soon')
		#l.place(x=180,y=0)
		'''smf4 = Frame(b_frame,height=150,width=175,bg='white')
		tc = Label(smf4,text='Total Customers:',fg='white',bg='cyan4',width=130,height=2,font='helvetica 15')
		tc.pack(side='top')
		smf4.pack_propagate(False)
		smf4.place(x=540+8,y=30)
		Label(smf4,text='40',fg='cyan4',bg='white',font='msserif 50').pack(anchor='center')
		'''
		emp1f = Frame(b_frame)
		path1 = "images/newman.jpg"
		img1 = ImageTk.PhotoImage(Image.open(path1))
		emp1 = Label(emp1f,image = img1)
		emp1.image=img1
		emp1.pack()
		emp1f.place(x=0,y=0)
		emp1inf = Frame(b_frame,bg='White',height=122,width=300)
		Label(emp1inf,text="Manager",bg='white',font='msserif 17 bold').place(x=60,y=0)
		Label(emp1inf,text="Mr. Tushar bhardwaj",bg='white',fg="Grey",font='msserif 10').place(x=60,y=37)
		Label(emp1inf,text="Extention : 025",bg='white',fg="Grey",font='msserif 10').place(x=60,y=59)
		Label(emp1inf,text="Mail : Manager@hotelname.com",bg='white',fg="Grey",font='msserif 10').place(x=60,y=83)
		emp1inf.pack_propagate(False)
		emp1inf.place(x=117,y=1)

		emp1f = Frame(b_frame)
		path2 = "images/receptionnew.jpg"
		img2 = ImageTk.PhotoImage(Image.open(path2))
		emp1 = Label(emp1f,image = img2)
		emp1.image=img2
		emp1.pack()
		emp1f.place(x=657,y=0)
		emp1inf = Frame(b_frame,bg='White',height=116,width=310)
		Label(emp1inf,text="Customer Executive",bg='white',font='msserif 17 bold').place(x=45,y=0)#pack(side='top')
		Label(emp1inf,text="Ms. Yash bhardwaj",bg='white',fg="Grey",font='msserif 10').place(x=45,y=37)
		Label(emp1inf,text="Extention : 032",bg='white',fg="Grey",font='msserif 10').place(x=45,y=59)
		Label(emp1inf,text="Mail : Costoexe@hotelname.com",bg='white',fg="Grey",font='msserif 10').place(x=45,y=83)	
		emp1inf.pack_propagate(False)
		emp1inf.place(x=767,y=2)

		emp1f = Frame(b_frame)
		path3 = "images/fchefnew.jpg"
		img3 = ImageTk.PhotoImage(Image.open(path3))
		emp1 = Label(emp1f,image = img3)
		emp1.image=img3
		emp1.pack()
		emp1f.place(x=0,y=152)
		emp1inf = Frame(b_frame,bg='White',height=121,width=320)
		Label(emp1inf,text="Restaurant",bg='white',font='msserif 17 bold').place(x=72,y=0)#pack(side='top')
		Label(emp1inf,text="Mr. Kartik narwal (Head)",bg='white',fg="Grey",font='msserif 10').place(x=72,y=37)
		Label(emp1inf,text="Extention : 028",bg='white',fg="Grey",font='msserif 10').place(x=72,y=59)
		Label(emp1inf,text="Mail : Restaurant@hotelname.com",bg='white',fg="Grey",font='msserif 10').place(x=72,y=83)	
		emp1inf.pack_propagate(False)
		emp1inf.place(x=99,y=153)
		emp1inf.tkraise()

		emp1f = Frame(b_frame)
		path4 = "images/roomservicenew.jpg"
		img4 = ImageTk.PhotoImage(Image.open(path4))
		emp1 = Label(emp1f,image = img4)
		emp1.image=img4
		emp1.pack()
		emp1f.place(x=657,y=152)
		emp1inf = Frame(b_frame,bg='White',height=124,width=315)
		Label(emp1inf,text="Room Service",bg='white',font='msserif 17 bold').place(x=55,y=0)#pack(side='top')
		Label(emp1inf,text="Ms. Shreya Panwar (Head)",bg='white',fg="Grey",font='msserif 10').place(x=55,y=37)
		Label(emp1inf,text="Extention : 041",bg='white',fg="Grey",font='msserif 10').place(x=55,y=59)
		Label(emp1inf,text="Mail : Roomsserv@hotelname.com",bg='white',fg="Grey",font='msserif 10').place(x=55,y=83)	
		emp1inf.pack_propagate(False)
		emp1inf.place(x=763,y=153)
		#b_frame.pack_propagate(False)
		'''sidebuttons = Text(b_frame,width=1,height=19)
		sc = Scrollbar(b_frame,command=sidebuttons.yview,width=10,bg='lightsteelblue3')
		sidebuttons.configure(yscrollcommand=sc.set)
		sc.pack(side='left',fill=Y)
		sidebuttons.place(x=10,y=0)
		b1  = Button(b_frame,font='mssherif 10', text="Room 1", bg='white',fg='cyan4',width=10)
		b2  = Button(b_frame,font='mssherif 10', text="Room 2", bg='white',fg='cyan4',width=10)
		b3  = Button(b_frame,font='mssherif 10', text="Room 3", bg='white',fg='cyan4',width=10)
		b4  = Button(b_frame,font='mssherif 10', text="Room 4", bg='white',fg='cyan4',width=10)
		b5  = Button(b_frame,font='mssherif 10', text="Room 5", bg='white',fg='cyan4',width=10)
		b6  = Button(b_frame,font='mssherif 10', text="Room 6", bg='white',fg='cyan4',width=10)
		b7  = Button(b_frame,font='mssherif 10', text="Room 7", bg='white',fg='cyan4',width=10)
		b8  = Button(b_frame,font='mssherif 10', text="Room 8", bg='white',fg='cyan4',width=10)
		b9  = Button(b_frame,font='mssherif 10', text="Room 9", bg='white',fg='cyan4',width=10)
		b10 = Button(b_frame,font='mssherif 10', text="Room 10",bg='white',fg='cyan4',width=10)
		sidebuttons.window_create("end",window=b1)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b2)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b3)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b4)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b5)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b6)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b7)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b8)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b9)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b10)'''
		Frame(b_frame,height=13,width=250,bg='white').place(x=410,y=2)
		Frame(b_frame,height=13,width=250,bg='white').place(x=410,y=153)
		#Frame(b_frame,height=180,width=13,bg='white').place(x=406,y=20)



		b_frame.place(x=0,y=120+6+20+60+11)
		b_frame.pack_propagate(False)
		b_frame.tkraise()
		nl = Label(b_frame,text='Made by Tushar',fg='black',bg='gray91',font='msserif 8')
		nl.place(x=955,y=310)
		nl.tkraise()

	