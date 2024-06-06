from account import Account

class Savings(Account):
    def __init__(self, balance=0):
        super().__init__(balance)
        self.interest_rate = 0.005
        self.withdrawal_limit = 700000

    def deposit(self, amount):
        if super().deposit(amount):
            interest = amount * self.interest_rate
            self.balance = self.balance + interest
            return "Deposited successfully"
        return False
    
    def withdraw(self, amount):
        if amount <= self.withdrawal_limit and amount <= super().withdraw(amount):
            return "Withdrawal successfull"
        if amount > self.withdrawal_limit:
            return "You have a limit of 700,000"
        return "Cannot withdraw! Insufficient funds"
    
    def __str__(self):
        return f"Savings {super().__str__()}"