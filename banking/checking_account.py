from .account import Account

class CheckingAccount(Account):
    def __init__(self, account_name, deposit=0):
        super().__init__(account_name, deposit)