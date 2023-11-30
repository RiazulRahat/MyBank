# Contains the structure of Account class

# Account class
from .transaction_log import TransactionLog
from .transaction import Transaction


class Account:

    # initializer
    def __init__(self, account_name, deposit = 0.0):
        self.account_name = account_name
        self.balance = deposit
        self.transaction_log = TransactionLog()

    # deposit amount to account
    def deposit(self, amount, category = "Income"):
        self.balance += amount
        depTran = Transaction(amount, "Deposit", category)    # add transaction class
        self.transaction_log.add_transaction(depTran)   # add transaction to self transactionLog

    # withdraw amount from account
    def withdraw(self, amount, category = "General"):
        # check if withdrawing more than funds available
        if amount <= self.balance:
            self.balance -= amount
            witTran = Transaction(amount, "Withdraw", category)   # add transaction class
            self.transaction_log.add_transaction(witTran)   # add transaction to self transactionLog
            print(f"Amount ${amount} withdrawn successfully.")
        else:
            print("Insufficient Funds...")

    # transfer amount from self account, to another account class
    def transfer(self, amount, to_account):
        if amount <= self.balance:
            self.balance -= amount
            to_account.balance += amount
            self.transaction_log.add_transaction(Transaction(amount, "Transfer In", "Transfer"))
            to_account.transaction_log.add_transaction(Transaction(amount, "Transfer Out", "Transfer"))
            print(f"Amount ${amount} transferred successfully.")
        else:
            print("Insufficient Funds...")
    
    # Print balance
    def get_balance(self):
        return self.balance
    
    def get_transactions(self, category = "None"):
        return self.transaction_log.get_transactions(category)