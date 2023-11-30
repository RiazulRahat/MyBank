# Transaction Cluster


from datetime import datetime


# Transaction class
class Transaction:
    # initializer (account has to be passed everytime)
    def __init__(self, amount, tranType, category = "Other", date = None):
        self.amount = amount
        self.tranType = tranType
        self.category = category
        self.date = datetime.now() if date is None else date
        
    def __str__(self):
        print(f"Transaction : {self.tranType} of ${self.amount} on {self.date} \nCategory: {self.category}")


    def is_Valid(self):
        return self.amount > 0 and self.tranType in ["Deposit", "Withdraw", "Transfer In", "Transfer Out"]
    

    # returns string "amount tranType date" for storage
    def serialize(self):
        return f"{self.amount} {self.tranType} {self.category} {self.date}"
    
    def get_category(self):
        return self.category