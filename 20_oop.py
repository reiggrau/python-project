from bank_accounts import *

# Create accounts
dave = BankAccount(1000, 'Dave')
sarah = BankAccount(2000, 'Sarah')

# Get balance
dave.get_balance()
sarah.get_balance()

# Deposit
sarah.deposit(500)

# Withdraw
dave.withdraw(1500)

# Transfer
sarah.transfer(500, dave)

###
jim = InterestAccount(1000, 'Jim')

jim.deposit(100)

jim.transfer(100, dave)

###
blaze = SavingsAccount(1000, 'Blaze')

blaze.withdraw(200)
