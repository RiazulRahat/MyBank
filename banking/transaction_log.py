# This file will keep a log of the transactions

class TransactionLog:

    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transactions(self, category):
        # print transactions for now
        tranStr = ""
        if category == "None":
            for object in self.transactions:
                tranStr += object.serialize()
                tranStr += "\n"
        else:
            for object in self.transactions:
                if object.get_category() == category:
                    tranStr += object.serialize()
                    tranStr += "\n"

        return tranStr