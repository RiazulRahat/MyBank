#-------------------------------------------------------------------------------------#
### NOTES ###
#-------------------------------------------------------------------------------------#
# 1# Contains the structure of Account class

#-------------------------------------------------------------------------------------#
### INCLUDES ###
#-------------------------------------------------------------------------------------#
from .transaction_log import TransactionLog
from .transaction import Transaction

#-------------------------------------------------------------------------------------#
### ACCOUNT CLASS ###
#-------------------------------------------------------------------------------------#
class Account:

    #---------------------------------------------------------------------------------#
    ### INITIALIZER ###
    #---------------------------------------------------------------------------------#

    def __init__(self, account_name, deposit = 0.0):
        self.account_name = account_name    # Necessary parameter
        self.balance = deposit
        self.transaction_log = TransactionLog() # Account's Transaction Log
        self.transaction_log.add_transaction(Transaction(deposit, "Deposit", "Initial Deposit"))

    #---------------------------------------------------------------------------------#
    ### DEPOSIT ###
    #---------------------------------------------------------------------------------#

    def deposit(self, amount, category = "Income"):
        self.balance += amount  # ADD deposit amount to account balance
        depTran = Transaction(amount, "Deposit", category)    # CREATE new Transaction
        self.transaction_log.add_transaction(depTran)   # ADD Transaction to TransactionLog

    #---------------------------------------------------------------------------------#
    ### WITHDRAW ###
    #---------------------------------------------------------------------------------#

    def withdraw(self, amount, category = "General"):
        # CHECK if balance available to Withdraw
        if amount <= self.balance and (amount > 0):  # TRUE
            self.balance -= amount  # SUBTRACT withdraw amount
            witTran = Transaction(amount, "Withdraw", category)   # CREATE new Transaction
            self.transaction_log.add_transaction(witTran)   # ADD Transaction to TransactionLog
            print(f"Amount ${amount} withdrawn successfully.")
        else:   # FALSE
            print("Insufficient Funds...")

    #---------------------------------------------------------------------------------#
    ### TRANSFER ###
    #---------------------------------------------------------------------------------#

    def transfer(self, amount, to_account):
        # CHECK if balance available to Transfer
        if amount <= self.balance:  # TRUE
            self.balance -= amount  # Take funds from THIS ACCOUNT
            to_account.balance += amount    #   DEPOSIT to OTHER ACCOUNT
            #-------------------------------------------------------------------------#
            ### ADD TRANSACTION TO BOTH ACCOUNTS ###
            #-------------------------------------------------------------------------#
            self.transaction_log.add_transaction(Transaction(amount, "Transfer In", "Transfer"))
            to_account.transaction_log.add_transaction(Transaction(amount, "Transfer Out", "Transfer"))

            #-------------------------------------------------------------------------#
            print(f"Amount ${amount} transferred successfully.")
        else:   # FALSE
            print("Insufficient Funds...")
    
    #---------------------------------------------------------------------------------#
    ### CURRENT BALANCE ###
    #---------------------------------------------------------------------------------#

    def get_balance(self):
        return self.balance
    
    #---------------------------------------------------------------------------------#
    ### LIST OF TRANSACTIONS (PER ACCOUNT)###
    #---------------------------------------------------------------------------------#
    def get_transactions(self, category = "None"):
        return self.transaction_log.get_transactions(category)
    
    #---------------------------------------------------------------------------------#