from objectbox import *


@Entity()
class Transaction:
    id = Id()   # transaction id
    action = String() # transaction
    amount = Int32()
    name = String()
    date = String()
        
    def credit(self, x, total):
        total += x
        print(x, "amount added.")
        return total
    
    def debit(self, x, total):
        if(total < x):
            print("Insufficient balance")    
        else:
            total -= x
            print(x, "amount debited.")
        return total
    
    def lent(self, x, name_, total):
        if(total < x):
            print("Insufficient balance. Cannot lend.")
        else:
            print(x,"Amouunt of money lent to",name_)
            total -= x
        return total
    
    def borrowed(self, x, name_, total):
        total += x
        print(x,"amount borrowed from ", name_)
        return total
    
    def display(self):
        print("Id = ",self.id)
        print("Amount = ",self.amount)
        print("Name = ",self.name)
        print("Action = ",self.action)
        print("Date = ",self.date)
        
def curr_balance(total):
    print("Current Amount :",total)        
        





# store = Store(directory="TransactionsDB")
# box = store.box(Transaction)

# obj = Transaction()
# obj.id = 1
# obj.action = 'cred'
# obj.amount = 5000
# obj.date = "01/06/2024"

# obj2 = Transaction()
# obj2.id = 10
# obj2.action = 'cred'
# obj2.amount = 5000
# obj2.date = "01/06/2024"

# box.put(obj)
# box.put(obj2)
# q = box.query(Transaction.action.equals('cred')).build()
# print(len(q.find()))
# for i in range(len(q.find())):
#     q.find()[i].display()

# a = q.find()[0]
# a.display()
# a = q.find()[1]
# a.display()
# # print(q._entity.id)



# # def push_object(obj):
# #     box.put(obj)
    
# # def query_object(a):
# #     q = box.query(Transaction.amount.equals(a)).build()
# #     out = q.find()[0]
# #     out.display()
