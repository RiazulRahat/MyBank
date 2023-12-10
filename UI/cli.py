# Command-Line UI

from banking.account import Account

accounts = {}

def create_account_ui():
    print("Create New Account")
    print("---------------------")

    account_name = input("Enter Account Name: ")
    initial_deposit = float(input("Initial Deposit Amount: "))

    new_account = Account(account_name, initial_deposit)

    accounts[account_name] = new_account

    print(f"Account created successfully! \nAccount Name: {account_name}\nInitial balance: {initial_deposit}\n")



def deposit_ui():
    account_name = input("Enter Account Name: ")

    if account_name in accounts:
        amount = float(input("Enter Deposit Amount: "))
        if(input("Input Category? Y/N: ") == "Y"):
            catBool = True
        else:
            catBool = False
        

        if catBool == True:
            category = input("Category: ")
        else:
            category = "Income"
        
        accounts[account_name].deposit(amount, category)
        print(f"Amount ${amount} deposited successfully.")
    else:
        print("Account Not Found!\n")


def withdraw_ui():
    account_name = input("Enter Account Name: ")

    if account_name in accounts:
        amount = float(input("Enter Withdraw Amount: "))
        if(amount <= 0):
            print("Invalid Withdraw Amount!\n")
            return

        if(input("Input Category? Y/N: ") == "Y"):
            catBool = True
        else:
            catBool = False
        

        if catBool == True:
            category = input("Category: ")
        else:
            category = "General"
        
        accounts[account_name].withdraw(amount, category)
        #print(f"Amount ${amount} deposited successfully.")
    else:
        print("Account Not Found!\n")

def transfer_ui():
    print("Transferring From \n")
    print("----------------------")
    transfer_from = input("Account Name: ")
    amount = float(input("Enter Amount to Transfer: "))
    print("Transferring To \n")
    print("----------------------")
    transfer_to = input("Account Name: ")

    if (transfer_from in accounts) and (transfer_to in accounts):
        accounts[transfer_from].transfer(amount, accounts[transfer_to])
    else:
        print("Invalid Account Name!")

def current_balance():
    account_name = input("Enter Account Name: ")

    if account_name in accounts:
        balance = accounts[account_name].get_balance()
        print(f"Current Balance = ${balance}")
    else:
        print("Invalid Account!")

def get_all_transactions():
    account_name = input("Enter Account Name: ")
    if account_name in accounts:
        print("\n" + accounts[account_name].get_transactions())
    else:
        print("Invalid Account!")

def main_menu():
    while True:
        print("1: Create Account \n2: Deposit \n3: Withdraw \n4: Transfer \n5: Current Balance \n6: Show all transactions \n7: Exit")
        choice = int(input("Enter your choice: "))

        if(choice == 1):
            create_account_ui()
        elif(choice == 2):
            deposit_ui()
        elif(choice == 3):
            withdraw_ui()
        elif(choice == 4):
            transfer_ui()
        elif(choice == 5):
            current_balance()
        elif(choice == 6):
            get_all_transactions()
        elif(choice == 7):
            break
        else:
            print("Invalid choice!")


def login_screen():
    print("Log In To Your Account \n")
    print("--------------------------")

    account_name