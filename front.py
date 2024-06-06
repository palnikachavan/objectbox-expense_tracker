## command line menu 

import trial  as back
from objectbox import *
import uuid

Store.remove_db_files("TransactionsDB")
store = Store(directory="TransactionsDB")
box = store.box(back.Transaction)

total = 10000
mod = back.Transaction()
    
def create_obj(amt, act, dat = '01/06/2024', nam = ""):
    obj = back.Transaction()
    obj.amount = amt
    obj.action = act
    obj.id = box.count() + 1
    name = nam
    obj.date = dat
    return obj

while(1):
    print("\n\t\t\tChoose operation ")
    print("1. Credit")
    print("2. Debit")
    print("3. Lend")
    print("4. Borrow")
    print("5. Display")
    print("6. Exit")
    choice = int(input())
    if(choice == 1):
        amt = int(input("Enter amount to be credited : "))
        obj = create_obj(amt, 'credit', "01/06/2024", "Home")
        
        box.put(obj)
        
        total = obj.credit(amt, total)
        back.curr_balance(total)
        
    elif(choice == 2):
        amt = int(input("Enter amount to be debited : "))
        obj = create_obj(amt, 'debit', "01/06/2024")
        box.put(obj)
        total = obj.debit(amt, total)
        back.curr_balance(total)
    
    elif(choice == 3):
        amt = int(input("Enter amount to be lent : "))
        name = input("Enter name of person to be lent : ")
        obj = create_obj(amt, 'lent', "01/06/2024", name)
        box.put(obj)
        total = obj.lent(amt, name, total)
        back.curr_balance(total)
        
    elif(choice == 4):
        amt = int(input("Enter amount to be borrowed : "))
        name = input("Enter name of person to be borrowed : ")
        obj = create_obj(amt, 'borrowed', "01/06/2024", name)
        box.put(obj)
        total = obj.borrowed(amt, name, total)
        back.curr_balance(total)
        
    elif(choice == 5):
        print("Display Transactions :")
        print("1. Credit")
        print("2. Debit")
        print("3. Lent")
        print("4. Borrowed")
        option = int(input("Enter choice :"))
        if(option == 1):
            q = box.query(back.Transaction.action.equals('credit')).build()
            a = q.find()     #returns a list of objects
            if(len(a) > 1):
                for i in range(len(a)):
                    a[i].display()
            else:
                a[0].display()
        
        elif(option == 2):
            q = box.query(back.Transaction.action.equals('debit')).build()
            a = q.find()     #returns a list of objects
            if(len(a) > 1):
                for i in range(len(a)):
                    a[i].display()
            else:
                a[0].display()
                    
        elif(option == 3):
            q = box.query(back.Transaction.action.equals('lent')).build()
            a = q.find()     #returns a list of objects
            if(len(a) > 1):
                for i in range(len(a)):
                    a[i].display()
            else:
                a[0].display()
                
        elif(option == 4):
            q = box.query(back.Transaction.action.equals('borrowed')).build()
            a = q.find()     #returns a list of objects
            if(len(a) > 1):
                for i in range(len(a)):
                    a[i].display()
            else:
                a[0].display()
            
    elif(choice == 6):
        print("Exiting...")
        break
    
    else:
        print("Invalid choice")