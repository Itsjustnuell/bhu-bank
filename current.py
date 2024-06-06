from account import Account

class CurrentAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)

    def deposit(self, amount):
        if super().deposit(amount):
            return "Deposited successfully"
    def withdraw(self, amount):
        if super().withdraw(amount):
            return "Withdrawn successfully"
        return "Insufficient funds!"

    def __str__(self):
        return f"Current {super().__str__()}"