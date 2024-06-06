from account import Account

class StudentAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)
        self.withdrawal_limit = 2000
        self.deposit_limit = 50000
    def deposit(self, amount):
        if amount <= self.deposit_limit and super().deposit(amount):
            return True
        return "You cannot deposit above the limit which is 50,000!"
    
    def withdraw(self, amount):
        if amount <= self.withdrawal_limit and super().withdraw(amount):
            return "Withdrawal successfull!"
        return "You cannot withdraw above the limit which is 2,000"
    
    def __str__(self):
        return f"Student {super().__str__()}"