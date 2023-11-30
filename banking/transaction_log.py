# This file will keep a log of the transactions

class TransactionLog:

    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transactions(self):
        # print transactions for now
        tranStr = ""
        for object in self.transactions:
            tranStr += object.serialize()
            tranStr += "\n"

        return tranStr
    
