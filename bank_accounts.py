class BalanceException(Exception):
    pass


class BankAccount():
    def __init__(self, initial_amount, account_name):
        self.balance = initial_amount
        self.name = account_name
        print(f"\nAccount created.")
        self.get_balance()

    def get_balance(self):
        print(
            f"Account '{self.name}' balance: {self.balance:.2f} €")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit complete.")
        self.get_balance()

    def check_balance(self, amount):
        if self.balance > amount:
            return
        else:
            raise BalanceException(
                f"Account '{self.name}' balance is only of {self.balance:.2f} €")

    def withdraw(self, amount):
        try:
            self.check_balance(amount)
            self.balance -= amount
            print(f"\nWithdrawal complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted.\n{error}")

    def transfer(self, amount, account):
        print("\n************")
        try:
            print(f"Beginning transfer... 🚀")
            self.check_balance(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\nTransfer complete! ✅")
        except BalanceException as error:
            print(f"\nTransfer interrupted. ❌\n{error}")
        finally:
            print("************")


class InterestAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("Deposit complete.")
        self.get_balance()


class SavingsAccount(InterestAccount):
    def __init__(self, initial_amount, account_name):
        super().__init__(initial_amount, account_name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.check_balance(amount + self.fee)
            self.balance -= amount + self.fee
            print(f"\nWithdrawal complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted.\n{error}")
