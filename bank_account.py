# Author: Abe
# Description: BankAccount class. Stores the customer's name, account number
#              and balance, and handles deposits and withdrawals.

import random


class BankAccount:
    # Runs when a new account is created: save the name, assign a random
    # 5-digit account number, and start the balance at $0.00
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.account_number = random.randint(10000, 99999)
        self.balance = 0.0

    # Add money to the balance. Returns True if it worked.
    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance = round(self.balance + amount, 2)   # round to cents
        return True

    # Take money out, but never more than the balance. Returns True if it worked.
    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance = round(self.balance - amount, 2)   # round to cents
        return True

    # Build the account information as text for display
    def get_info(self):
        return (f"Name: {self.owner_name}\n"
                f"Account #: {self.account_number}\n"
                f"Balance: ${self.balance:,.2f}")
