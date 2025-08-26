import json

class BankAccount:
    bankname = "RCU"

    def __init__(self, account_name: str, balance: float, log: str):
        self.account_name = account_name
        self.balance = balance
        self.log = []

    def __repr__(self):
        return(f"BankAccount: {self.account_name}'s balance = {self.balance}")

    def account_creation(self, account_name: str):
        self.log.append("Account created")

    def withdraw(self, amount: float):
        if amount > self.balance:
            self.log.append("failed withdraw")
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.log.append(f"withdrew: {amount}")

    def deposit(self, amount: float):
        self.balance += amount
        self.log.append(f"deposited: {amount}")

    def historylog(self):
        for record in self.log:
            print(record)


username = str(input("username? "))
with open("accounts.json", "r") as file:
    accounts = json.load(file)
    if username not in accounts:
        balance = float(input("how much do you have? "))
        accounts[username] = BankAccount(username, balance, [])
        accounts[username].account_creation(username)
        choice = input("What would you like to do? ")
    else:
        input(f"hello, {username}. What would you like to do? ")






