# Comman-Line UI

from banking.account import Account

def create_account_ui():
    print("Create New Account")
    print("---------------------")

    account_name = input("Enter Account Name: ")
    initial_deposit = float(input("Initial Deposit Amount: "))

    new_account = Account(account_name, initial_deposit)

    print(f"Account created successfully! \nAccount Name: {account_name}\nInitial balance: {initial_deposit}\n")

    return new_account


def deposit_ui():
    pass

def withdraw_ui():
    pass

def transfer_ui():
    pass


def main_menu():
    while True:
        print("1: Create Account \n2: Deposit \n3: Withdraw \n4: Transfer \n5: Exit \n")
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
            break
        else:
            print("Invalid choice!")

        