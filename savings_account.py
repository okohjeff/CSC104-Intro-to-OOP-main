from account import Account

class SavingsAccount(Account):
    def __init__(self):
        super().__init__()

    def withdraw(self, amount):
        if amount < 2000:
            super().withdraw(amount)
        else:
            print("You cannot withdraw above your limit")

mySavingsAccount = SavingsAccount()
mySavingsAccount.withdraw(3000)