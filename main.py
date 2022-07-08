from tkinter import *
from tkinter import ttk
from database import *
import os

def start():
    global ap
    ap = Tk()
    ap.title('Restaurant Management 0.1 Beta')
    ap.geometry('900x700+0+0')

    #==========Commmands=================

    def placeorder():
        generatebill['state'] = DISABLED
    def gosettings():
        settings = Toplevel(ap)
        settings.title('Preferences')
        settings.geometry('900x475+0+150')

        frame1 = Frame(settings,bd=5,height=375,width=800,relief='ridge',padx=20,pady=20)
        frame1.place(anchor=CENTER,relx=0.5, rely=0.5)

        percent =  Label(frame1,text='Discount(%):',font=('arial',20,'bold'),pady=5,padx=5)
        percent.grid(row=0,column=0)
        percententry = Entry(frame1,font=('arial',20,'bold'))
        percententry.grid(row=0,column=1)

        curency =  Label(frame1,text='Currency:',font=('arial',20,'bold'),pady=5,padx=5)
        curency.grid(row=1,column=0)
        curencyentry = ttk.Combobox(frame1,font=('arial',20,'bold'),state='readonly',width=19)
        curencyentry['values'] = currencies
        curencyentry.grid(row=1,column=1)

        tax =  Label(frame1,text='Tax(%):',font=('arial',20,'bold'),pady=5,padx=5)
        tax.grid(row=2,column=0)
        taxentry = Entry(frame1,font=('arial',20,'bold'))
        taxentry.grid(row=2,column=1)

        delvry =  Label(frame1,text='Delivery Fee:',font=('arial',20,'bold'),pady=5,padx=5)
        delvry.grid(row=3,column=0)
        delvryentry = Entry(frame1,font=('arial',20,'bold'))
        delvryentry.grid(row=3,column=1)

        data = Label(frame1,font=('arial',20,'bold'),text='Path:',pady=5,padx=5)
        databasepath = Entry(frame1,font=('arial',20,'bold'))
        data.grid(row=4,column=0)
        databasepath.grid(row=4,column=1)

        apply = Button(frame1,text='Apply Changes',font=('arial',20,'bold'),bg='black',fg='white')
        apply.grid(row=5,column=0)
        clear = Button(frame1,text='Clear Database',font=('arial',20,'bold'),padx=35,fg='red',bg='black')
        clear.grid(row=5,column=1)

        settings.mainloop()
    def godiscounts():
        discounts = Toplevel(ap)
        discounts.title('Discounts')
        discounts.geometry('900x475+0+150')

        frame1 = Frame(discounts,bd=5,height=375,width=800,relief='ridge', padx=20)
        frame1.place(anchor=CENTER,relx=0.5, rely=0.5)

        percent =  Label(frame1,text='Discount(%)',font=('arial',30,'bold'),pady=20,padx=5)
        percent.grid(row=0,column=0)
        percententry = Entry(frame1,font=('arial',30,'bold'))
        percententry.grid(row=0,column=1)

        money =  Label(frame1,text='Discount(-AED)',font=('arial',30,'bold'),pady=20,padx=5)
        money.grid(row=1,column=0)
        moneyentry = Entry(frame1,font=('arial',30,'bold'))
        moneyentry.grid(row=1,column=1)

        discounts.mainloop()
    def addinv():
        inv = Toplevel(ap)
        inv.title('Add Inventory')
        inv.geometry('900x475+0+150')
        
        frame1 = Frame(inv,bd=5,height=375,width=800,relief='ridge',padx=20,pady=20)
        frame1.place(anchor=CENTER,relx=0.5, rely=0.5)

        food =  Label(frame1,text='Name Of Food:',font=('arial',20,'bold'),pady=5,padx=5)
        food.grid(row=0,column=0)
        foodentry = Entry(frame1,font=('arial',20,'bold'))
        foodentry.grid(row=0,column=1)

        cat =  Label(frame1,text='Category:',font=('arial',20,'bold'),pady=5,padx=5)
        cat.grid(row=1,column=0)
        catentry = ttk.Combobox(frame1,font=('arial',20,'bold'),state='readonly',width=19)
        catentry['values'] = foodcategory
        catentry.grid(row=1,column=1)

        price =  Label(frame1,text='Price:',font=('arial',20,'bold'),pady=5,padx=5)
        price.grid(row=2,column=0)
        priceentry = Entry(frame1,font=('arial',20,'bold'))
        priceentry.grid(row=2,column=1)

        kywrd =  Label(frame1,text='Keywords:',font=('arial',20,'bold'),pady=5,padx=5)
        kywrd.grid(row=3,column=0)
        kywrdentry = Entry(frame1,font=('arial',20,'bold'))
        kywrdentry.grid(row=3,column=1)

        add = Button(frame1,text='Add Item',font=('arial',20,'bold'),padx=80,bg='black',fg='white')
        add.grid(row=4,column=1)

        inv.mainloop()

    #Main Frame
    app = Frame(ap,relief='flat')
    app.place(x=0,y=0,height=700,width=900,anchor=CENTER,relx=0.5, rely=0.5)


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

    newfood = Button(bottomframe,text='Add To Inventory',font=('Arial',12,'bold'),padx=25,pady=15,fg='white',bg='black',command=addinv)
    newfood.place(x=5,y=5)

    settingsbutton = Button(bottomframe,text='Preferences',font=('Arial',12,'bold'),padx=25,pady=15,fg='white',bg='black',command=gosettings)
    settingsbutton.place(x=205,y=5)

    discounts = Button(bottomframe,text='Discounts',font=('Arial',12,'bold'),padx=25,pady=15,fg='red',bg='black',command=godiscounts)
    discounts.place(x=515,y=5)

    neworder = Button(bottomframe,text='New Order',font=('Arial',12,'bold'),padx=25,pady=15,fg='white',bg='black',command=goneworder)
    neworder.place(x=365,y=5)


    about2 = Label(bottomframe,text='SOOPERMAN',font=('Roberto',20,'bold'),fg='red')
    about2.place(y=30,x=700)

    about = Label(bottomframe,text='Developed by',font=('Arial',12,'bold'))
    about.place(y=5,x=770)



    ap.mainloop()

def goneworder():
    global ap
    ap.destroy()
    start()
    
start()