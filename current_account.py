from account import Account

class CurrentAccount(Account):
    def __init__(self):
        super().__init__()

myCurrentAccount = CurrentAccount()
myCurrentAccount.deposit(1000)
myCurrentAccount.withdraw(5000)