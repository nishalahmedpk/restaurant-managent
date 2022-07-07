from cProfile import label
from tkinter import *
from tkinter import ttk


app = Tk()
app.title('Restaurant Management 0.1 Beta')
app.geometry('900x700+0+0')

#Temp Database
fooditems = ('Biriyani','Shawarma','Juice')
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

#Header
headingframe = Label(app,bd=20,text='RESTAURANT',fg='white',font=('arial',50,'bold'),bg='red')
headingframe.pack(side='top',fill='x')

#======================Order Details======================
orderframe = Frame(app,bd=5,relief='ridge')
orderframe.place(x=0,y=120,height=100,width=900)

#==================================Order Taking=======================
takeframe = Frame(app,bd=5,relief='ridge')
takeframe.place(x=0,y=220,height=400,width=900)

#Add order
addframe = LabelFrame(takeframe,bd=5,relief='ridge') 
addframe.place(x=5,y=5,width=600,height=80)

addlabel = Label(addframe,text='Add Item:', font=('Arial',12,'bold'),padx=20,pady=25)
addlabel.grid(row=0,column=0)

add = ttk.Combobox(addframe,font=('Arial',12,'bold'),width=20)
add['values'] = fooditems
add.grid(row=0,column=1)

qntylabel = Label(addframe,text='Qnty:', font=('Arial',12,'bold'),padx=20)
qntylabel.grid(row=0,column=2)

qnty = ttk.Combobox(addframe,font=('Arial',12,'bold'),width=3)
qnty['values'] = numbers
qnty.grid(row=0,column=3)

blank = Label(addframe,text='',padx=10)
blank.grid(row=0,column=4)

addbutton = Button(addframe,text='Add', font=('Arial',12,'bold'),padx=20)
addbutton.grid(row=0,column=5)

#Items
itemsframe = LabelFrame(takeframe,bd=5,relief='ridge')
itemsframe.place(x=5,y=90,width=600,height=295)

#OrderStatus Generate Bill and Bill
billframe = LabelFrame(takeframe,bd=5,relief='ridge')
billframe.place(x=610,y=5,height=380,width=275)

statusframe = LabelFrame(billframe,padx=50,relief='flat')
statusframe.grid(row=0,column=0)

statuslabel = Label(statusframe,text='Status:',font=('Arial',12,'bold'),pady=25)
statuslabel.grid(row=0,column=0)

paystatues = ttk.Combobox(statusframe,font=('Arial',12,'bold'),width=8,state='readonly')
paystatues['values'] = ('Paid','Not Paid')
paystatues.grid(row=0,column=1)

generatebill = Button(billframe,text='Generate Bill', font=('Arial',12,'bold'),padx=67)
generatebill.grid(row=1)

bill = Text(billframe, height=14,width=30,pady=10)
bill.grid(row=2)


#===============================Bottom Part================================
bottomframe = Frame(app,bd=5,relief='ridge')
bottomframe.place(x=0,y=620,height=80,width=900)





app.mainloop()