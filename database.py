import csv
def getfooditems():
    l = []
    with open('fooditems.csv','r+') as x:
        r = csv.reader(x)
        for i in r:
            if i == []:
                pass
            else:
                l.append(i[0])
    return l

def getfoodcategory():
    l = []
    with open('fooditems.csv','r+') as x:
        r = csv.reader(x)
        for i in r:
            if i == []:
                pass
            else:
                if i[2] not in l:
                    l.append(i[2])
    return l

fooditems = getfooditems()

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

currencies = ['AED','INR', 'USD']

foodcategory = getfoodcategory()

ordertypecombovalues = ['Dine-in','Take-Away','Delivery']

paystatuesvalues = ('Paid','Not Paid','Credit')

restaurantname='RESTAURANT NAME'

foreground123 = 'DarkSlateGray'

  #can change in preferences hopefully
