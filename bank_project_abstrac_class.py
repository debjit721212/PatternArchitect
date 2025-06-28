from abc import ABC, abstractmethod
import random

# ------------------------------
# Abstract Base Class
# ------------------------------

class BankAccount(ABC):
    def __init__(self, account_holder, account_bal, bank_code, user_secret_code):
        self.account_holder = account_holder
        self._account_bal = account_bal
        self.__bank_code = bank_code
        self._user_secret_code = user_secret_code
        self.account_number = random.randint(10000000, 99999999)
        self.transaction_history = []

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount, user_secret_code):
        pass

    def _log_transaction(self, message):
        if len(self.transaction_history) >= 5:  # Keep only last 5 transactions
            self.transaction_history.pop(0)
        self.transaction_history.append(message)

    def check_balance(self):
        print(f"{self.account_holder} has ${self._account_bal:.2f} in the account.")

    def apply_interest(self, rate=0.03):
        interest = self._account_bal * rate
        self._account_bal += interest
        self._log_transaction(f"Interest added: +${interest:.2f}")
        print(f"Interest of ${interest:.2f} added. New balance: ${self._account_bal:.2f}")

    def print_transactions(self):
        print(f"Last transactions for {self.account_holder}:")
        for txn in self.transaction_history:
            print(f"  - {txn}")


# ------------------------------
# Concrete Savings Account
# ------------------------------

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self._account_bal += amount
            self._log_transaction(f"Deposited +${amount:.2f}")
            print(f"Deposited ${amount:.2f} successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount, user_secret_code):
        if user_secret_code != self._user_secret_code:
            print("❌ Wrong secret code. Access denied.")
            return
        if 0 < amount <= self._account_bal:
            self._account_bal -= amount
            self._log_transaction(f"Withdrawn -${amount:.2f}")
            print(f"Withdrawn ${amount:.2f} successfully.")
        else:
            print("❌ Insufficient balance or invalid amount.")


# ------------------------------
# Bank System Manager
# ------------------------------

class BankSystem:
    def __init__(self):
        self.accounts = {}

    def register_account(self):
        name = input("Enter account holder name: ")
        balance = float(input("Enter initial balance: "))
        bank_code = "BANKX1234"  # Can be random/fixed for now
        secret_code = input("Set your secret code (password): ")

        account = SavingsAccount(name, balance, bank_code, secret_code)
        self.accounts[account.account_number] = account
        print(f"Account created successfully! Your account number is {account.account_number}")

    def login(self):
        acc_num = int(input("Enter your account number: "))
        secret_code = input("Enter your secret code: ")

        account = self.accounts.get(acc_num)
        if not account:
            print("❌ No account found with that number.")
            return None

        if account._user_secret_code != secret_code:
            print("❌ Incorrect secret code.")
            return None

        print(f"✅ Welcome {account.account_holder}!")
        return account


# ------------------------------
# CLI Interface
# ------------------------------

def main():
    bank = BankSystem()

    while True:
        print("\n🏦 Welcome to Humba Bank 🏦")
        print("1. Register New Account")
        print("2. Login to Existing Account")
        print("3. Exit")

        choice = input("Choose option (1/2/3): ")

        if choice == "1":
            bank.register_account()
        elif choice == "2":
            account = bank.login()
            if account:
                while True:
                    print("\n--- Account Menu ---")
                    print("1. Deposit Money")
                    print("2. Withdraw Money")
                    print("3. Check Balance")
                    print("4. Apply Interest")
                    print("5. Print Transactions")
                    print("6. Logout")

                    user_choice = input("Choose option: ")

                    if user_choice == "1":
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                    elif user_choice == "2":
                        amount = float(input("Enter amount to withdraw: "))
                        code = input("Enter your secret code: ")
                        account.withdraw(amount, code)
                    elif user_choice == "3":
                        account.check_balance()
                    elif user_choice == "4":
                        rate = float(input("Enter interest rate (default 0.03): ") or 0.03)
                        account.apply_interest(rate)
                    elif user_choice == "5":
                        account.print_transactions()
                    elif user_choice == "6":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid option. Try again!")
        elif choice == "3":
            print("Thank you for using Humba Bank. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")

# ------------------------------
# Run the App
# ------------------------------

if __name__ == "__main__":
    main()
