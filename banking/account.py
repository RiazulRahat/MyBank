# Contains the structure of Account class

# Account class
from .transaction_log import TransactionLog
from .transaction import Transaction


class Account:

    # initializer
    def __init__(self):
        self.balance = 0
        self.transaction_log = TransactionLog()

    # deposit amount to account
    def deposit(self, amount, category = "Income"):
        self.balance += amount
        depTran = Transaction(amount, "Deposit", category)    # add transaction to cluster
        self.transaction_log.add_transaction(depTran)   # add transaction to transactionLog

    # withdraw amount from account
    def withdraw(self, amount, category = "General"):
        # check if withdrawing more than funds available
        if amount <= self.balance:
            self.balance -= amount
            witTran = Transaction(amount, "Withdraw", category)   # add transaction to cluster
            self.transaction_log.add_transaction(witTran)   # add transaction to transactionLog
        else:
            print("Insufficient Funds...")
    
    # Print balance
    def get_balance(self):
        return self.balance
    
    def get_transactions(self, category = "None"):
        return self.transaction_log.get_transactions(category)