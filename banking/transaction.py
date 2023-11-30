# Transaction Cluster


from datetime import datetime


# Transaction class
class Transaction:
    # initializer (account has to be passed everytime)
    def __init__(self, amount, tranType, date = None):
        self.amount = amount
        self.tranType = tranType
        self.date = datetime.now() if date is None else date
        
    def __str__(self):
        print(f"Transaction : {self.tranType} of ${self.amount} on {self.date}")


    def is_Valid(self):
        return self.amount > 0 and self.tranType in ["Deposit", "Withdraw", "Transfer"]
    

    # returns string "amount tranType date" for storage
    def serialize(self):
        return f"{self.amount} {self.tranType} {self.date}"