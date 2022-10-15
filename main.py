from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import *
from mysqldatabase import *

snumber = 1
noofitems = 0
orderlist = []
o = []
personaldiscountnumber = 0
personaldiscount = 0
table = 'july'

def getpath():
    with open('preferences.dat','r+b') as x:
        import pickle
        dictonary = pickle.load(x)
        try:
            with open(dictonary['Path'],'r+') as x:
                x.close
        except FileNotFoundError:
            with open(dictonary['Path'],'w+') as x:
                x.close()
        return dictonary['Path']
path = getpath()

def start():
    global ap,xaxis
    ap = Tk()
    #ap.tk_setPalette('black')
    ap.title('Restaurant Management 0.1 Beta')
    ap.geometry('900x700+0+0')
    ap.state('zoomed')

    #==========Commmands=================

    def preferences():
        #discount
        discountdata = percententry1.get()
        #currency
        currency = curencyentry.get()
        #tax%
        taxx = taxentry.get()
        #delivery fee
        deliveryy = delvryentry.get()
        #path
        way = databasepath.get()
        bob=0
        with open('preferences.dat','w+b') as x:
            import pickle
            d={}
            if discountdata=='' or currency=='' or deliveryy=='' or taxx=='' or way == '':
                messagebox.showerror('Error','Enter All Fields')
            else:
                d['Discount'] = discountdata
                d['Currency'] = currency
                d['Delivery'] = deliveryy  #errror
                d['Tax'] = taxx #error
                d['Path'] = way+'.csv'
                pickle.dump(d,x)
                bob = 1
        if bob == 1:
            with open(way+'.csv','w+') as y:
                import csv
                w= csv.writer(y)
                w.writerow(['S.NO','Mobile No','No Of Items','Items','Type','Status','Total Price'])

    def addtodatabase():
        global path,status123,o
        #adds to orders.csv
        #called in place order
        import csv
        serialnumber = getordernop(table)
        moobilenumber = mobileno.get()
        noofitemsoredered = noofitems
        type123 = ordertypecombo.get()
        status123 = paystatues.get()
        tots = 0
        for i in orderlist:
            bill.insert(END,i[0]+'\t\t\t'+i[1]+'\n')
            tots+=int(i[1])
        if paystatues.get()=='Credit':
            tots = -(tots)     
        with open(path,'a+',newline='') as x:
            w = csv.writer(x)
            w.writerow([serialnumber,moobilenumber,noofitemsoredered,o,type123,status123,tots])

    def additem():
        global snumber, orderlist,noofitems,o
        import csv
        item = add.get()
        quantityget=qnty.get()
        with open('fooditems.csv','r+') as x:
            r = csv.reader(x)
            for i in r:
                if i[0]==item:
                    price = i[1]
        serialnumber['state'] = 'normal'
        ite['state'] = 'normal'
        price1['state']='normal'
        quantity['state']='normal'
        total1['state']='normal'


        serialnumber.insert(END,str(snumber)+'\n')
        ite.insert(END,item+'\n')
        price1.insert(END,price+'\n')
        quantity.insert(END,quantityget+'\n')
        price = int(price)
        quantityget = int(quantityget)
        tot = price*quantityget
        tot = str(tot)
        total1.insert(END,tot+'\n')

        if item not in o:
            o.append(item)
        l1 = str(item)+' x'+str(quantityget)
        l2 = tot
        l = [l1,l2]
        orderlist.append(l)
   
        serialnumber['state'] = 'normal'
        ite['state'] = 'disabled'
        price1['state']='disabled'
        quantity['state']='disabled'
        total1['state']='disabled'   
        snumber+=1
        noofitems += 1*quantityget
    
    def placeorder():
        dog =0
        global orderlist
        try:
            int(mobileno.get())
        except ValueError:
            dog =1

        if len(mobileno.get()) != 12 or dog==1 or ordertypecombo.get()=='' or paystatues.get()=='' or orderlist==[]:
            messagebox.showerror('Error','Enter All Fields Properly')
        else:
            addtodatabase()
            type123 = ordertypecombo.get()
            status123 = paystatues.get()
            generatebill['state'] = 'disabled'
            addbutton['state'] = 'disabled'
            discounts['state'] = 'disabled'
            
            #bill
            bill['state']='normal'
            restaurantname='RESTAURANT NAME'
            bill.insert(END,restaurantname.center(30))
            bill.insert(END,'-'*30+'\n')
            bill.insert(END,'Item\t\t\tPrice\n')
            bill.insert(END,'-'*30+'\n')
            tots = 0
            for i in orderlist:
                bill.insert(END,i[0]+'\t\t\t'+i[1]+'\n')
                tots+=int(i[1])
            tots2 = tots
            if tots2 <0:
                tots2 =0
            bill.insert(END,'-'*30+'\n')
            bill.insert(END,'Initital Price:\t\t\t'+str(tots)+'\n')
            if ordertypecombo.get()=='Delivery':
                deliveryfees = 0
                with open('preferences.dat','r+b') as x:
                    import pickle
                    dictionary = pickle.load(x)
                    deliveryfees = int(dictionary['Delivery'])
                    bill.insert(END,'Delivery Fee:\t\t\t'+str(deliveryfees)+'\n')
                    tots2+=deliveryfees
            if personaldiscountnumber != 0:
                tots2-=personaldiscountnumber
                bill.insert(END,'Personal Discount:\t\t\t'+str(personaldiscountnumber)+'\n')
            if personaldiscount != 0:
                tots2= tots2 - tots*(personaldiscount/100)
                bill.insert(END,'Personal Discount%:\t\t\t'+str(personaldiscount)+'\n')

            with open('preferences.dat','r+b') as x:
                import pickle
                dictionary = pickle.load(x)
                disc = int(dictionary['Discount'])
                tots2 -= (disc/100)*tots2
            if disc != 0:
                bill.insert(END,'Discount%:\t\t\t'+str(disc)+'\n')
            with open('preferences.dat','r+b') as x:
                import pickle
                dictionary = pickle.load(x)
                tax = int(dictionary['Tax'])
                tots2 += (tax/100)*tots2
            if tax != 0:
                bill.insert(END,'Tax%:\t\t\t'+str(tax)+'\n')
            if paystatues.get()=='Credit':
                tots2 = -(tots2)                  
            bill.insert(END,'Total Price:\t\t\t'+str(tots2)+'\n')
            bill.insert(END,'-'*30+'\n')
            bill.insert(END,'Status:\t\t'+str(status123)+'\n')
            bill.insert(END,'Order Type:\t\t'+str(type123)+'\n')
            if ordertypecombo.get()=='Delivery':
                pass

            bill['state']='disabled'
    def gosettings():
        global percententry1,curencyentry,taxentry,delvryentry,databasepath

        file = open('preferences.dat','r+b')
        import pickle
        dictonary = pickle.load(file) 

        settings = Toplevel(ap)
        settings.title('Preferences')
        settings.geometry('900x475+0+150')

        frame1 = Frame(settings,bd=5,height=375,width=800,relief='ridge',padx=20,pady=20)
        frame1.place(anchor=CENTER,relx=0.5, rely=0.5)

        percent1 =  Label(frame1,text='Discount(%):',font=('arial',20,'bold'),pady=5,padx=5)
        percent1.grid(row=0,column=0)
        percententry1 = Entry(frame1,font=('arial',20,'bold'))
        percententry1.grid(row=0,column=1)
        percententry1.insert(0,dictonary['Discount'])

        curency =  Label(frame1,text='Currency:',font=('arial',20,'bold'),pady=5,padx=5)
        curency.grid(row=1,column=0)
        curencyentry = ttk.Combobox(frame1,font=('arial',20,'bold'),width=19)
        curencyentry['values'] = currencies
        curencyentry.grid(row=1,column=1)
        curencyentry.insert(0,dictonary['Currency'])
        curencyentry['state'] = 'readonly'

        tax =  Label(frame1,text='Tax(%):',font=('arial',20,'bold'),pady=5,padx=5)
        tax.grid(row=2,column=0)
        taxentry = Entry(frame1,font=('arial',20,'bold'))
        taxentry.grid(row=2,column=1)
        taxentry.insert(0,dictonary['Tax'])

        delvry =  Label(frame1,text='Delivery Fee:',font=('arial',20,'bold'),pady=5,padx=5)
        delvry.grid(row=3,column=0)
        delvryentry = Entry(frame1,font=('arial',20,'bold'))
        delvryentry.grid(row=3,column=1)
        delvryentry.insert(0,dictonary['Delivery'])

        data = Label(frame1,font=('arial',20,'bold'),text='Path:',pady=5,padx=5)
        databasepath = Entry(frame1,font=('arial',20,'bold'))
        data.grid(row=4,column=0)
        databasepath.grid(row=4,column=1)
        databasepath.insert(0,str(dictonary['Path'])[:-4])

        apply = Button(frame1,text='Apply Changes',font=('arial',20,'bold'),bg='black',fg='white',command=preferences)
        apply.grid(row=5,column=0)
        clear = Button(frame1,text='Clear Database',font=('arial',20,'bold'),padx=35,fg='red',bg='black',command=newdatabase)
        clear.grid(row=5,column=1)


        file.close()
        settings.mainloop()

    def personaldiscountsupdate():
        global personaldiscountnumber,personaldiscount
        personaldiscountnumber += int(moneyentry.get())
        personaldiscount = int(percententry.get())

    def godiscounts():
        global moneyentry,percententry
        discounts = Toplevel(ap)
        discounts.title('Discounts')
        discounts.geometry('900x475+0+150')

        frame1 = Frame(discounts,bd=5,height=375,width=800,relief='ridge', padx=20,pady=20)
        frame1.place(anchor=CENTER,relx=0.5, rely=0.5)

        percent =  Label(frame1,text='Discount(%)',font=('arial',30,'bold'),pady=20,padx=5)
        percent.grid(row=0,column=0)
        percententry = Entry(frame1,font=('arial',30,'bold'))
        percententry.grid(row=0,column=1)
        percententry.insert(0,'0')

        money =  Label(frame1,text='Discount(-AED)',font=('arial',30,'bold'),pady=20,padx=5)
        money.grid(row=1,column=0)
        moneyentry = Entry(frame1,font=('arial',30,'bold'))
        moneyentry.grid(row=1,column=1)
        moneyentry.insert(0,'0')

        personaldiscountbutton = Button(frame1,text='Apply',font=('arial',30,'bold'),pady=-5,padx=150,fg='white',bg='black',command=personaldiscountsupdate)
        personaldiscountbutton.grid(row=2,column=1)

        discounts.mainloop()
    def addinv():

        def addtodata():
            import csv 
            name = foodentry.get()
            price = priceentry.get()
            category = catentry.get()
            with open('fooditems.csv','a+',newline='') as x:    
                w = csv.writer(x)
                w.writerow([name,price,category])

        inv = Toplevel(ap)
        inv.title('Add Inventory')
        inv.geometry(f'900x475+0+150')
        
        frame1 = Frame(inv,bd=5,height=375,width=800,relief='ridge',padx=20,pady=20)
        frame1.place(anchor=CENTER,relx=0.5, rely=0.5)

        foodentry = StringVar()
        catentry =StringVar()
        priceentry = StringVar()
        kywrdentry =StringVar()

        food =  Label(frame1,text='Name Of Food:',font=('arial',20,'bold'),pady=5,padx=5)
        food.grid(row=0,column=0)
        foodentry = Entry(frame1,font=('arial',20,'bold'))
        foodentry.grid(row=0,column=1)

        cat =  Label(frame1,text='Category:',font=('arial',20,'bold'),pady=5,padx=5)
        cat.grid(row=1,column=0)
        catentry = ttk.Combobox(frame1,font=('arial',20,'bold'),width=19)
        catentry['values'] = foodcategory
        catentry.grid(row=1,column=1)

        pricee =  Label(frame1,text='Price:',font=('arial',20,'bold'),pady=5,padx=5)
        pricee.grid(row=2,column=0)
        priceentry = Entry(frame1,font=('arial',20,'bold'))
        priceentry.grid(row=2,column=1)
        
        add = Button(frame1,text='Add Item',font=('arial',20,'bold'),padx=80,bg='black',fg='white', command=addtodata)
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
    orderno = Label(orderframe, text=str(getordernop(table)), font=('Arial',12,'bold'),fg='red')

    ordernotext.grid(row=0,column=0)
    orderno.grid(row=0,column=1)

    ordertype = Label(orderframe,text='Type:',font=('Arial',12,'bold'),padx=20)   #Type
    ordertypecombo = ttk.Combobox(orderframe,width=10, font=('Arial',12,'bold'),state='readonly')
    ordertypecombo['values']=ordertypecombovalues

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

    addbutton = Button(addframe,text='Add', font=('Arial',12,'bold'),padx=20,fg='white',bg='black',command=additem)
    addbutton.grid(row=0,column=5)

    #Items
    itemsframe = LabelFrame(takeframe,bd=5,relief='ridge',padx=10,pady=10)
    itemsframe.place(x=5,y=90,width=600,height=295)


    #SNO
    serialnumber = Text(itemsframe,width=4,height=15)
    serialnumber.grid(row=0,column=0)
    serialnumber.insert('1.0','-'*4+'\n')
    serialnumber.insert('2.0','S.NO\n')
    serialnumber.insert('3.0','-'*4+'\n')
    serialnumber['state']='disabled'

    #ITEMS
    iteframe = LabelFrame(itemsframe,bd=5,relief='flat',padx=10,pady=10)
    iteframe.grid(row=0,column=1)
    
    ite = Text(iteframe,width=30,height=15)
    ite.grid(row=0,column=1)
    ite.insert('1.0',"-"*30+'\n')
    ite.insert('2.0','Items\n')
    ite.insert('3.0',"-"*30+'\n')
    ite['state']='disabled'

    #PRICE
    price1frame = LabelFrame(itemsframe,bd=5,relief='flat',padx=5,pady=10)
    price1frame.grid(row=0,column=2)
    price1 = Text(price1frame,width=5,height=15)
    price1.grid()
    price1.insert('1.0','-----'+'\n')
    price1.insert('2.0','Price')
    price1.insert('3.0','-----'+'\n')
    price1['state']='disabled'

    #QUANTITY
    quantity1frame = LabelFrame(itemsframe,bd=5,relief='flat',padx=5,pady=10)
    quantity1frame.grid(row=0,column=3)
    quantity = Text(quantity1frame,width=8,height=15)
    quantity.grid()
    quantity.insert('1.0','-'*8+'\n')
    quantity.insert('2.0','Quantity')
    quantity.insert('3.0','-'*8+'\n')
    quantity['state']='disabled'

    #TOTAL
    total1frame = LabelFrame(itemsframe,bd=5,relief='flat',padx=5,pady=10)
    total1frame.grid(row=0,column=4)
    total1 = Text(total1frame,width=12,height=15)
    total1.grid()
    total1.insert('1.0','-'*12+'\n')
    total1.insert('2.0','Total Price \n')
    total1.insert('3.0','-'*12+'\n')
    total1['state']='disabled'


    #OrderStatus Generate Bill and Bill
    billframe = LabelFrame(takeframe,bd=5,relief='ridge')
    billframe.place(x=610,y=5,height=380,width=275)

    statusframe = LabelFrame(billframe,padx=50,relief='flat')
    statusframe.grid(row=0,column=0)

    statuslabel = Label(statusframe,text='Status:',font=('Arial',12,'bold'),pady=25)
    statuslabel.grid(row=0,column=0)

    global paystatues
    paystatues = ttk.Combobox(statusframe,font=('Arial',12,'bold'),width=8,state='readonly')
    paystatues['values'] = paystatuesvalues
    paystatues.grid(row=0,column=1)

    generatebill = Button(billframe,text='Generate Bill', font=('Arial',12,'bold'),padx=67,fg='white',bg='black',command=placeorder)
    generatebill.grid(row=1)

    bill = Text(billframe, height=14,width=30,pady=10,state='disabled')
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


    about2 = Label(bottomframe,text='Nishal',font=('Roberto',20,'bold'))
    about2.place(y=30,x=790)

    about = Label(bottomframe,text='Jonathan &',font=('Arial',12,'bold'))
    about.place(y=5,x=785)



    ap.mainloop()

def goneworder():
    global ap, snumber,orderlist,tots,noofitems,personaldiscountnumber, o,personaldiscount
    ap.destroy()
    snumber = 1
    noofitems = 0
    orderlist = []
    tots=0
    o=[]
    start()
    personaldiscountnumber = 0
    personaldiscount = 0
start()