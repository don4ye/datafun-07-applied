from account import Account

# Create an account
my_account = Account("123456789", "John Doe", 1000)

# Check initial balance
my_account.check_balance()

# Make a deposit
my_account.deposit(500)

# Check balance after deposit
my_account.check_balance()

# Withdraw some funds
my_account.withdraw(200)

# Check balance after withdrawal
my_account.check_balance()
