from tkinter import *
from tkinter import ttk
from database import *


ap = Tk()
ap.title('Restaurant Management 0.1 Beta')
ap.geometry('900x700+0+0')
ap.resizable(False,False)

#==========Commmands=================
def placeorder():
    generatebill['state'] = DISABLED


#Main Frame
app = Frame(ap,relief='flat')
app.place(x=0,y=0,height=700,width=900)


#Header
headingframe = Label(app,bd=20,text='RESTAURANT',fg='white',font=('arial',50,'bold'),bg='black')
headingframe.pack(side='top',fill='x')

#======================Order Details======================
orderframe = LabelFrame(app,bd=5,relief='ridge')
orderframe.place(x=0,y=120,height=100,width=900)

ordernotext = Label(orderframe,text='Order No:',font=('Arial',12,'bold'),padx=25,pady=15)  #Order NO
orderno = Label(orderframe, text=ordernumber, font=('Arial',12,'bold'),fg='red')

ordernotext.grid(row=0,column=0)
orderno.grid(row=0,column=1)

ordertype = Label(orderframe,text='Type:',font=('Arial',12,'bold'),padx=20)   #Type
ordertypecombo = ttk.Combobox(orderframe,width=10, font=('Arial',12,'bold'),state='readonly')
ordertypecombo['values']=('Delivery','Dine-in','Take-Away')

ordertype.grid(row=1,column=0)
ordertypecombo.grid(row=1,column=1)

mobilenotext = Label(orderframe,text='Mobile No:',font=('Arial',12,'bold'),padx=20)     #Mobile No
mobileno = Entry(orderframe,font=('Arial',12,'bold'))
mobileno.insert(0,'971')

mobilenotext.grid(row=0,column=2)
mobileno.grid(row=0,column=3)

addresstext = Label(orderframe,text='Address:',font=('Arial',12,'bold'),padx=20)        #Address
address = Entry(orderframe,font=('Arial',12,'bold'))

addresstext.grid(row=0,column=4)
address.grid(row=0,column=5)



#==================================Order Taking=======================
takeframe = LabelFrame(app,bd=5,relief='ridge')
takeframe.place(x=0,y=220,height=400,width=900)

#Add order
addframe = LabelFrame(takeframe,bd=5,relief='ridge') 
addframe.place(x=5,y=5,width=600,height=80)

addlabel = Label(addframe,text='Add Item:', font=('Arial',12,'bold'),padx=20,pady=25)
addlabel.grid(row=0,column=0)

add = ttk.Combobox(addframe,font=('Arial',12,'bold'),width=20,state='readonly')
add['values'] = fooditems
add.grid(row=0,column=1)

qntylabel = Label(addframe,text='Qnty:', font=('Arial',12,'bold'),padx=20)
qntylabel.grid(row=0,column=2)

qnty = ttk.Combobox(addframe,font=('Arial',12,'bold'),width=3)
qnty['values'] = numbers
qnty.grid(row=0,column=3)

blank = Label(addframe,text='',padx=10)
blank.grid(row=0,column=4)

addbutton = Button(addframe,text='Add', font=('Arial',12,'bold'),padx=20,fg='white',bg='black')
addbutton.grid(row=0,column=5)

#Items
itemsframe = LabelFrame(takeframe,bd=5,relief='ridge')
itemsframe.place(x=5,y=90,width=600,height=295)

itemscroll = ttk.Scrollbar(itemsframe,orient=VERTICAL)
itemscroll.pack(side='right',fill=Y)

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

generatebill = Button(billframe,text='Generate Bill', font=('Arial',12,'bold'),padx=67,fg='white',bg='black',command=lambda:placeorder)
generatebill.grid(row=1)

bill = Text(billframe, height=14,width=30,pady=10)
bill.grid(row=2)


#===============================Bottom Part================================
bottomframe = LabelFrame(app,bd=5,relief='ridge')
bottomframe.place(x=0,y=620,height=80,width=900)

newfood = Button(bottomframe,text='Add To Inventory',font=('Arial',12,'bold'),padx=25,pady=15,fg='white',bg='black')
newfood.place(x=5,y=5)

settings = Button(bottomframe,text='Preferences',font=('Arial',12,'bold'),padx=25,pady=15,fg='white',bg='black')
settings.place(x=205,y=5)

discounts = Button(bottomframe,text='Discounts',font=('Arial',12,'bold'),padx=25,pady=15,fg='red',bg='black')
discounts.place(x=515,y=5)

neworder = Button(bottomframe,text='New Order',font=('Arial',12,'bold'),padx=25,pady=15,fg='white',bg='black')
neworder.place(x=365,y=5)


about2 = Label(bottomframe,text='SOOPERMAN',font=('Roberto',20,'bold'),fg='red')
about2.place(y=30,x=700)

about = Label(bottomframe,text='Developed by',font=('Arial',12,'bold'))
about.place(y=5,x=770)



ap.mainloop()