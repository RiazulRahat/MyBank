#-------------------------------------------------------------------------------------#
### NOTES ###
#-------------------------------------------------------------------------------------#
# 1# Contains the structure of Transaction class

#-------------------------------------------------------------------------------------#
### INCLUDES ###
#-------------------------------------------------------------------------------------#
from datetime import datetime

#-------------------------------------------------------------------------------------#
### TRANSACTION CLASS ###
#-------------------------------------------------------------------------------------#
class Transaction:
    #---------------------------------------------------------------------------------#
    ### INITIALIZER ###
    #---------------------------------------------------------------------------------#
    def __init__(self, amount, tranType, category = "Other", date = None):
        self.amount = amount
        self.tranType = tranType
        self.category = category
        self.date = datetime.now() if date is None else date    # Set current date if no date provided
    
    #---------------------------------------------------------------------------------#
    ### OUTPUT STRING ###
    #---------------------------------------------------------------------------------#
    def __str__(self):
        print(f"Transaction : {self.tranType} of ${self.amount} on {self.date} \nCategory: {self.category}")

    #---------------------------------------------------------------------------------#
    ### CHECK IF TRANSACTION TYPE IS VALID ###
    #---------------------------------------------------------------------------------#
    def is_Valid(self):
        return self.amount > 0 and self.tranType in ["Deposit", "Withdraw", "Transfer In", "Transfer Out"]
    

    #---------------------------------------------------------------------------------#
    ### RETURN STRING {AMOUNT TRANTYPE CATEGORY DATE} IN THIS FORMAT ###
    #---------------------------------------------------------------------------------#
    def serialize(self):
        return f"{self.amount} {self.tranType} {self.category} {self.date}"
    
    #---------------------------------------------------------------------------------#
    ### RETURN CATEGORY ###
    #---------------------------------------------------------------------------------#
    def get_category(self):
        return self.category