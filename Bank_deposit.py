# Bank_deposit_withdrawl_machine


print("***Congraluations your Bank Account is Opened***")
# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("!!! Welcome to the Deposit & Withdrawal Machine !!!")
 
    def deposit(self):
        amount=float(input("Enter amount you want to Deposit: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount you want to be Withdraw: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdraw:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)

  
# creating an object of class
s = Bank_Account()

# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()
