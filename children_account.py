from account import Account

class ChildrenAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)
        self.interest_rate = 0.007
    def deposit(self, amount):
        if super().deposit(amount):
            interest = amount * self.interest_rate
            self.balance += interest
            return "Deposited successfully"
        return False
    
    def withdraw(self, amount):
        return "Cannot withdraw. This is a children's account"
    
    def __str__(self):
        return f"Children {super().__str__()}"