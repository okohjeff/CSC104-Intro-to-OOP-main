class Account:
    def __init__(self):
        self.balance = 10000
        print("Starting balance is", self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("New balance is", self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("New balance is", self.balance)

myAccount = Account()
myAccount.deposit(2000)