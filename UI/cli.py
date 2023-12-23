# Command-Line UI

from banking.account import Account

accounts = {}

def create_account_ui():
    print(text_center("Create New Account"))

    account_name = input("Enter Account Name: ")
    initial_deposit = float(input("Initial Deposit Amount: "))

    new_account = Account(account_name, initial_deposit)

    accounts[account_name] = new_account

    print(text_center(f"Account created successfully! \n\nAccount Name: {account_name}\nInitial balance: {initial_deposit}"))

def deposit_ui(account_name):
    print(text_center("DEPOSIT"))

    amount = float(input("Enter Deposit Amount: "))
    if(input("Input Category? Y/N: ") == "Y"):
        category = input("Category: ")
    else:
        category = "Income"

    accounts[account_name].deposit(amount, category)
    print(f"Amount ${amount} deposited successfully.")

    end_print()

def withdraw_ui(account_name):
    print(text_center("WITHDRAW"))
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
    end_print()

def transfer_ui(transfer_from):
    print(text_center("Transferring From"))
    print(f"Account Name: {transfer_from}")
    amount = float(input("Enter Amount to Transfer: "))
    print(text_center("Transferring To"))
    transfer_to = input("Account Name: ")

    if verifyAccount(transfer_to):
        accounts[transfer_from].transfer(amount, accounts[transfer_to])
    else:
        print("Invalid Account to Transfer!")

    end_print()

def current_balance(account_name):
    balance = accounts[account_name].get_balance()
    print(text_center(f"Current Balance = ${balance}"))

def get_all_transactions(account_name):
    print(text_center("TRANSACTION HISTORY"))
    print(accounts[account_name].get_transactions())
    current_balance(account_name)

def main_menu(account_name):
    while verifyAccount(account_name):
        print(text_center("MAIN MENU"))
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
            return "switch"
        elif(choice == 7):
            return "logout"
        else:
            print("Invalid choice!")

# Make this the [default UI] - then this account name gets passed to every functions
def login_screen():
    account_name = ""
    while True:
        print(text_center("Log In To Your Account"))

        #Add password definitions later#

        account_name = input("Enter your Account Name: ")
        if(verifyAccount(account_name)):
            print(f"Welcome Back {account_name}")
            action = main_menu(account_name)
            if (action == "logout"):
                exit()
                break

            # if user wants to swtch accounts, go thru login_screen again
            elif (action == "switch"):
                print(f"See you again {account_name}!")
                continue
    
        else:
            print("Account not Found!")
            if(input("Register New Account? Y/N : ") == "Y"):
                create_account_ui()
                continue
            else:
                exit()


def verifyAccount(account_name):
    if account_name in accounts:
        return True
    
    return False


def exit():
    end_print()
    print("\n\n\nThank you for using MyBank!\n\n\n")
    end_print()



def text_center(text):
    text = f"--------------------------\n{text}\n--------------------------"
    return text

def text_top(text):
    text = f"{text}\n--------------------------"
    return text

def end_print():
    print("--------------------------")


def check_negative(number):
    if number <= 0:
        return False
    
    return True