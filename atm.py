from datetime import datetime

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.transactions.append((time, "Deposit", amount))
            print(f"✅ Deposited: {amount} | Balance: {self.balance} | Time: {time}")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient balance.")
        elif amount <= 0:
            print("❌ Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.transactions.append((time, "Withdraw", amount))
            print(f"💸 Withdrawn: {amount} | Balance: {self.balance} | Time: {time}")

    def check_balance(self):
        print(f"📊 {self.owner}'s Balance: {self.balance}")

    def print_transactions(self):
        print(f"\n📄 Transaction History for {self.owner}:")
        for time, t_type, amount in self.transactions:
            print(f"{time} - {t_type}: {amount}")

# Example usage
account = BankAccount("Arif Hussain", 10000000)
account.deposit(500)
account.withdraw(200)
account.check_balance()
account.print_transactions()
