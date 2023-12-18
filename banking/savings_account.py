from .account import Account

class SavingsAccount(Account):
    def __init__(self, account_name, deposit=0, interest_rate = 0.1):
        super().__init__(account_name, deposit)
        self.interest_rate = interest_rate


    def add_interest(self):
        self.balance += self.balance * self.interest_rate