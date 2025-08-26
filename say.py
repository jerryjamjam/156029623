class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance (self):
        return self.balance

    def __str__(self):
        return f"{self.name}'s balance: ${self.balance:.2f}"

def main():
    accounts = {
        "Jay": BankAccount("Jay"),
        "Tee": BankAccount("Tee")
    }

    while True:
        account_name = input("Which account (Jay/Tee)?").strip().lower()

        if account_name in accounts:
            account = accounts[account_name]
        else:
            print("Invalid account")
            continue

        action = input("What would you like to do?")

        if action == "deposit":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(account)
            print(f"deposited ${amount:.2f}. new balance ${account}")

        if action == "withdraw":
            amount = float(input("Enter amount to withdraw: "))
            if account.withdraw(account):
                print(f"Withdrew ${amount:.2f}. new balance ${account}")
            else:
                print("Insufficient funds")
        elif action == "balance":
            print(account)
        elif action == "quit":
            print("Exiting...")
            break
        else:
            print("Invalid action")

if __name__ == "__main__":
    main()
