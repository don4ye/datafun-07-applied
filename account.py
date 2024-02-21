class Account:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit funds into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        """Withdraw funds from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. Current balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def check_balance(self):
        """Check the current balance."""
        print(f"Current balance: ${self.balance}")
