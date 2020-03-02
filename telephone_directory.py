from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import sqlite3

root=Tk( ) 
root.title(" TELEPHONE DIRECTORY")
root.geometry("600x600+350+350")
root.configure(background = "")
photo = PhotoImage(file = "telephone.png")
#w = Label(root, image=photo)
w=Label(root, image=photo)
w.pack(side='bottom')
#ent = Entry(root)
#ent.pack()
#ent.focus_set() 
photo_new= PhotoImage(file = "telephone2.png")
#w = Label(root, image=photo)
m=Label(root, image=photo_new)
m.pack(side='left')

#for add
adtel_no=Toplevel(root)
adtel_no.title("add telephone number")
adtel_no.geometry("500x500+350+250")
root.configure(background = "RoyalBlue1")
adtel_no.withdraw( )

lblAddname = Label(adtel_no , text ="Enter name " , fg='red')
lblAddname.pack( )
entAddname = Entry(adtel_no , bd=5)
entAddname.pack( )
entAddname.focus( )

lblAddtel_no= Label(adtel_no , text ="Enter telephone number ",fg='red')
lblAddtel_no.pack( )
entAddtel_no = Entry(adtel_no, bd=5)
entAddtel_no.pack( )
entAddtel_no.focus( )



def f1( ):
	root.withdraw( )
	adtel_no.deiconify( )
adtel_no.configure(background="RoyalBlue2")
photon = PhotoImage(file = "telephone3.png")
x=Label(adtel_no, image=photon)
x.pack(side='bottom')
btnAdd=Button(root , text="Add telephone number", width =20 ,command=f1)
btnAdd.pack(pady=20 )


def f2( ):
	con=None
	cursor=None
	try:
		
		con=sqlite3.connect('tel_dir.db')
                
		
		if  int(entAddtel_no.get( )) > 0 and len(entAddtel_no.get( ))==10:
			tel_no=int(entAddtel_no.get( ))
		else:
			
			messagebox.showerror("Issue ",'Give  postive number only ')
		
		if entAddname.get( ).isalpha( )== True:
			name=entAddname.get ( )
			if  int(len(name) ) > 1:
				cursor=con.cursor( )
				sql="insert into telephone values('%d ' , '%s')"
				args=(tel_no,name)
				cursor.execute(sql % args)
				con.commit( )
				msg=str(cursor.rowcount)+"inserted"
				entAddtel_no.delete(0,END)
				entAddname.delete(0,END)
				messagebox.showinfo("Success ",msg)
			else :
				messagebox.showerror("Issue ",'Give minimum two character ')
		else:
			messagebox.showerror("Issue ",'Give  character only ')
	
		
		

	except sqlite3.Error as e:
		con.rollback( )
		messagebox.showerror("Issue ",e)

	except UnboundLocalError  as m:
		messagebox.showerror("Issue ",m)
	except ValueError  as t:
		messagebox.showerror("Issue ",t)
	
			
		

	finally:

		
		if cursor is not None:
			cursor.close( )

		if con is not None:
			con.close( )
		


btnAddSave = Button(adtel_no, text= "Save", command=f2)
btnAddSave.pack(pady=10 )


def f3( ):
	adtel_no.withdraw( )
	root.deiconify( )
btnAddBack=Button(adtel_no , text="Back", command=f3)
btnAddBack.pack(pady=10 )

#for view

vitel_no=Toplevel(root)
vitel_no.title("View telephone number")
vitel_no.geometry("400x300+350+250")
vitel_no.withdraw( )


def f4( ):

	root.withdraw( )
	vitel_no.deiconify( )
	con=None
	cursor=None
	try:
		con=sqlite3.connect('tel_dir.db')
		cursor=con.cursor( )
		sql="select * from telephone";
		cursor.execute(sql)
		data=cursor.fetchall( )
		
		tel_list.config(state=NORMAL)
		tel_list.delete(0,END)	
		for row in data:
			tel_list.insert(END,row,str(""))
		tel_list.config(state=DISABLED)
		
	except sqlite3.Error as e:
		messagebox.showerror("Issue ",e)
		
	finally:
		if cursor is not None:
			cursor.close( )

		if con is not None:
			con.close( )

btnView=Button(root, text="View telephone number", width =20 ,command=f4)
btnView.pack(pady=20 )

stData=Scrollbar(vitel_no)
stData.grid(row=0,column=1,sticky='ns')

tel_list=Listbox(vitel_no,width=60,height=25,yscrollcommand=stData.set)
tel_list.grid(row=0,column=0,padx=8)
stData.config(command=tel_list.yview())


def f5( ):
	vitel_no.withdraw( )
	root.deiconify( )
btnViewBack=Button(vitel_no,text="Back",command=f5)
btnViewBack.grid()






#for update

uptel_no=Toplevel(root)
uptel_no.title("Update telephone number")
uptel_no.geometry("500x500+350+250")
uptel_no.withdraw( )


lblUpdatename = Label(uptel_no , text ="Enter name ")
lblUpdatename.pack( )
entUpdatename = Entry(uptel_no , bd=5)
entUpdatename.pack( )


lblUpdatetel_no = Label(uptel_no , text ="Enter telephone number ")
lblUpdatetel_no.pack( )
entUpdatetel_no= Entry(uptel_no , bd=5)
entUpdatetel_no.pack( )




def f6( ):
	root.withdraw( )
	uptel_no.deiconify( )
uptel_no.configure(background="forest green")
btnUpdate=Button(root , text="Update telephone number", width =20 ,command=f6)
btnUpdate.pack(pady=20 )

def f7( ):
	con=None
	cursor=None
	try:
		con=sqlite3.connect('tel_dir.db')
		if  int(entUpdatetel_no.get( )) > 0 and len(entUpdatetel_no.get( ))==10:
			tel_no=int(entUpdatetel_no.get( ))
		else:
			messagebox.showerror("Issue ",'Give  postive number only and give 10 digits number')

		if entUpdatename.get( ).isalpha( )== True:
			name=entUpdatename.get ( )
			if  int(len(name) ) > 1:
				cursor=con.cursor( )
				sql="update telephone set tel_no='%d' where name='%s' "
				args=(tel_no,name)
				cursor.execute(sql % args)
				con.commit( )
				msg=str(cursor.rowcount)+"updated"
				entUpdatetel_no.delete(0,END)
				entUpdatename.delete(0,END)
				messagebox.showinfo("Success ",msg)
			else :
				messagebox.showerror("Issue ",'Give minimum two character ')
		else:
			messagebox.showerror("Issue ",'Give  character only ')
		

	except sqlite3.Error as e:
		con.rollback( )
		messagebox.showerror("Issue ",e)

	except UnboundLocalError  as m:
		messagebox.showerror("Issue ",m)
		

	finally:

		
		if cursor is not None:
			cursor.close( )

		if con is not None:
			con.close( )
		


btnUpdateSave = Button(uptel_no , text= "Save",command=f7)
btnUpdateSave.pack(pady=10 )

def f8( ):
	uptel_no.withdraw( )
	root.deiconify( )
btnUpdateBack=Button(uptel_no , text="Back", command=f8)
btnUpdateBack.pack(pady=10 )

#delete

deltel_no=Toplevel(root)
deltel_no.title("Delete telephone number")
deltel_no.geometry("400x300+350+250")
deltel_no.withdraw( )

lblDeletename= Label(deltel_no , text ="Enter name ")
lblDeletename.pack( )
entDeletename = Entry(deltel_no , bd=5)
entDeletename.pack( )


def f9( ):
	root.withdraw( )
	deltel_no.deiconify( )
deltel_no.configure(background="forest green")
btnDelete=Button(root , text="Delete telephone number", width =20 ,command=f9)
btnDelete.pack(pady=20 )

def f10( ):

	con=None
	cursor=None
	try:
		con=sqlite3.connect('tel_dir.db')
		
		name=entDeletename.get( )
		cursor=con.cursor( )
		sql="delete from telephone where name='%s' " 
		args=(name)
		cursor.execute(sql%args)
		con.commit( )
		msg=str(cursor.rowcount)+"deleted"
		entDeletename.delete(0,END)
		messagebox.showinfo("Success ",msg)

	except sqlite3.Error as e:
		con.rollback( )
		messagebox.showerror("Issue ",e)
		

	finally:
		
		if cursor is not None:
			cursor.close( )

		if con is not None:
			con.close( )
		

btnDeletedel = Button(deltel_no , text= "Delete",command=f10)
btnDeletedel.pack(pady=10 )

def f11( ):
	deltel_no.withdraw( )
	root.deiconify( )
btnDeleteBack=Button(deltel_no , text="Back", command=f11)
btnDeleteBack.pack(pady=10 )


#for search

searchtel_no=Toplevel(root)
searchtel_no.title("Search telephone number")
searchtel_no.geometry("400x300+350+250")
searchtel_no.withdraw( )

lblSearchname = Label(searchtel_no , text ="Enter name " , fg='red')
lblSearchname.pack( )
entSearchname = Entry(searchtel_no , bd=5)
entSearchname.pack( )


def f14( ):
	root.withdraw( )
	searchtel_no.deiconify( )
searchtel_no.configure(background="VioletRed1")
btnSearch=Button(root , text="Search telephone number", width =20 ,command=f14)
btnSearch.pack(pady=20 )


def f12( ):
	root.withdraw( )
	searchtel_no.deiconify( )
	con=None
	cursor=None
	try:
		
		con=sqlite3.connect('tel_dir.db')
		if entSearchname.get( ).isalpha( )== True:
			name=entSearchname.get ( )
			if  int(len(name) ) > 1:
				cursor=con.cursor( )
				sql="select * from telephone where name='%s'";
				args=(name)
				cursor.execute(sql% args)
				con.commit
				data=cursor.fetchall( )
				#msg=" "
				tel_Data.config(state=NORMAL)
				#for d in data:
				#msg=msg+"tel_no: " + str(d[0])    +    "  name:  " +  d[1]   +"\n"
				tel_Data.insert(INSERT,data)
				entSearchname.delete(0,END)
				tel_Data.config(state=DISABLED)
				#stData.clear( )
	except sqlite3.Error as e:
		messagebox.showerror("Issue ",e)
		
	finally:

		
		if cursor is not None:
			cursor.close( )

		if con is not None:
			con.close( )

btnSearch = Button(searchtel_no, text= "Search", command=f12)
btnSearch.pack(pady=10 )

tel_Data=scrolledtext.ScrolledText(searchtel_no ,width=40, height=10)
tel_Data.pack( )



def f13( ):
	searchtel_no.withdraw( )
	root.deiconify( )
btnSearchBack=Button(searchtel_no,text="Back",command=f13)
btnSearchBack.pack(pady=10 )

def clearData( ):
	entAddtel_no.delete(0,END)
	entAddname.delete(0,END)
	entUpdatetel_no.delete(0,END)
	entUpdatename.delete(0,END)
	entSearchname.delete(0,END)

btnClearData=Button(root,text='clear',font=('arial',20,'bold'),height=1,width=10,bd=5,command=clearData)
btnClearData.pack()


root.mainloop( )








