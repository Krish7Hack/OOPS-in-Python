class Car:

    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.brk=True
        print("Car Started..")

car1=Car()
car1.start()

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc
    
    def debit(self,amount):
        self.balance=self.balance-amount
        print("Debited Amount:",amount)
        print("Balance:",self.get_balance())

    def credit(self,amount):
        self.balance=self.balance+amount
        print("Credited Amount:",amount)
        print("Balance:",self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1=Account(10000,12345)
acc1.debit(5000)
acc1.credit(1000)