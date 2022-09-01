class Customer:
    '''  This class developed by SbI and describes bank operation'''
    bankname="SBIBANK"
    def __init__(self, name,balance=0.0):
        self.name=name
        self.balance=balance

    def  deposit(self, amount):
        self.balance = self.balance+amount
        print('After deposit,balance: ', self.balance)

    def   withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient  Function can't perform this operation")
        else:
            self.balance = self. balance-amount
            print("After withdraw balance:- ", self.balance)

print("welcome   to ", Customer.bankname)
name=input("Enter Your Name:- ")
c = Customer(name)
while True:
    print("d-Deposit\nw=withdraw\ne=Exit")
    option = input("Chose your operation:- ")
    if option.lower() == "d":
        amount = float(input("Enter amount to deposit:-"))
        c .deposit(amount)
    elif option.lower() == "w":
        amount = float(input("Enter amount withdraw:- "))
        c.withdraw(amount)
    elif option.lower() == 'e':
        print("Thanks for Banking....")
        break
    else:
        print("Your Option Is invalid....please Chose Valid Option")


