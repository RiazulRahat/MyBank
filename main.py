# interact with Account class and handle user input/output

from banking.account import Account

def main():
    account = Account() # create an account
    account2 = Account()

    account.deposit(100)
    print(f"Balance: {account.get_balance()}")

    account.withdraw(50)
    print(f"Balance: {account.get_balance()}")


    account2.withdraw(100)
    account2.deposit(200)
    account2.withdraw(66)
    account2.deposit(128)

    print(account2.get_balance())

    print(account2.get_transactions())
    print(account.get_transactions())

    


if __name__ == "__main__":
    main()