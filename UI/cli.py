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

    return account_name

def deposit_ui(account_name):
    amount = float(input("Enter Deposit Amount: "))
    if(input("Input Category? Y/N: ") == "Y"):
        category = input("Category: ")
    else:
        category = "Income"

    accounts[account_name].deposit(amount, category)
    print(f"Amount ${amount} deposited successfully.")

def withdraw_ui(account_name):

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
    print(f"Amount ${amount} withdrawn successfully.")

def transfer_ui(transfer_from):
    print("Transferring From \n")
    print("----------------------")
    print(f"Account Name: {transfer_from}")
    amount = float(input("Enter Amount to Transfer: "))
    print("Transferring To \n")
    print("----------------------")
    transfer_to = input("Account Name: ")

    if verifyAccount(transfer_to):
        accounts[transfer_from].transfer(amount, accounts[transfer_to])
    else:
        print("Invalid Account to Transfer!")

def current_balance(account_name):
    balance = accounts[account_name].get_balance()
    print(f"Current Balance = ${balance}")

def get_all_transactions(account_name):
    print("\n" + accounts[account_name].get_transactions())

def main_menu(account_name):
    while verifyAccount(account_name):
        print(f"Account Name: {account_name}\n1: Deposit \n2: Withdraw \n3: Transfer \n4: Current Balance \n5: Show all transactions \n6: Switch Accounts \n7: Log Out")
        choice = int(input("Enter your choice: "))

        if(choice == 1):
            deposit_ui(account_name)
        elif(choice == 2):
            withdraw_ui(account_name)
        elif(choice == 3):
            transfer_ui(account_name)
        elif(choice == 4):
            current_balance(account_name)
        elif(choice == 5):
            get_all_transactions(account_name)
        elif(choice == 6):
            login_screen()
        elif(choice == 7):
            exit()
            break
        else:
            print("Invalid choice!")

# Make this the [default UI] - then this account name gets passed to every functions
def login_screen():
    print("Log In To Your Account \n")
    print("--------------------------")

    #Add password definitions later#

    account_name = input("Enter your Account Name: ")
    if(verifyAccount(account_name)):
        main_menu(account_name)
    
    else:
        print("Account not Found! \n")
        if(input("Register New Account? Y/N : ") == "Y"):
            account_name = create_account_ui()
            main_menu(account_name)
        else:
            exit()


def verifyAccount(account_name):
    if account_name in accounts:
        return True
    
    return False


def exit():
    print("\n\n\nThank you for using MyBank!\n\n\n")