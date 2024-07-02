# Mini Project - 2 : Banking System
class colors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

import os
class Account:
    def __init__(self,account_number,name,balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    def display_details(self):
        print(f"{colors.CYAN}Account number = {self.account_number}\nName = {self.name}\nBalance = {self.balance}\n")
class Bank:
    def __init__(self,filename="accounts.txt"):
        self.fname = filename
        self.accounts = self.load_accounts()

    def load_accounts(self):
        if not os.path.exists(self.fname):
            return []
        with open(self.fname,"r") as file:
            lines = file.readlines()
        accounts = []
        for line in lines:
            account_number,name,balance = line.strip().split(",")
            accounts.append(Account(account_number,name,str(balance)))
        return accounts
    def save_account(self):
        with open(self.fname,"w") as file:
            for account in self.accounts:
                file.write(f"{account.account_number},{account.name},{str(account.balance)}\n")

    def add_accounts(self,account):
        self.accounts.append(account)
        self.save_account()
    def account_number_exists(self,account_number):
        a = 0
        for account in self.accounts:
            if account.account_number == str(account_number):
                a = 1
        if a == 0:
            return False
        else:
            return True

    def deposit(self,account_number,amount):
        if not self.account_number_exists(account_number):
            print(f"{colors.RED}Cant Deposit becuase account_number doesn't exists !!!")
            return
        for account in self.accounts:
            if account.account_number == account_number:
                new_balance = int(account.balance) + amount
                account.balance = str(new_balance)
                print(f"**\nDeposited {amount}\- to Account number : {account_number}\nTotal Balance = {account.balance}\-\n**")
                self.save_account()

    def with_draw(self,account_number,amount):
        if not self.account_number_exists(account_number):
            print(f"{colors.RED}Cant withdraw becuase account_number doesn't exists !!!")
            return
        for account in self.accounts:
            if account.account_number == account_number:
                if int(account.balance) < amount:
                    print(f"{colors.RED}!!\nCan't withdraw, because you didn't have enough money to with draw\nTotal Balance = {account.balance}\-\n!!")
                    return
                else:
                    new_balance = int(account.balance) - amount
                    account.balance = str(new_balance)
                    print(f"{colors.GREEN}**\nWith drawn {amount}\- from Account Number : {account_number}\nRemaining balance : {account.balance}\-\n**")
                    self.save_account()

    def check_balance(self,account_number):
        if not self.account_number_exists(account_number):
            print(f"{colors.RED}!!\nAccount Number doesn't exists\n!!")
            return
        for account in self.accounts:
            if account.account_number == account_number:
                print(f"{colors.GREEN}**\nBalance = {account.balance}\- in Account Number : {account_number}\n**")

    def show_account_details(self,account_number):
        if not self.account_number_exists(account_number):
            print(f"{colors.RED}!!\nAccount Number doesn't exists\n!!")
            return
        for account in self.accounts:
            if account.account_number == account_number:
                print(f"{colors.GREEN}--------------------------\nAccount Number = {account_number}\nName = {account.name}\nAmount = {account.balance}\n--------------------------")

    def show_all_bank_account_details(self):
        print("########################")
        for account in self.accounts:
            print(f"{colors.GREEN}Account Number = {account.account_number}\nName = {account.name}\nAmount = {account.balance}")
            print("########################")

acc = Bank()

# acc.add_accounts(Account("2214101","Person1",1000))
# acc.add_accounts(Account("2214102","Person2",2000))
# acc.add_accounts(Account("2214103","Person3",0))

# acc.deposit("2214101",150)

# acc.with_draw("2214102",799)

# acc.with_draw("2214103",299)

# acc.check_balance("2214102")

# acc.show_account_details("2214101")

acc.show_all_bank_account_details()