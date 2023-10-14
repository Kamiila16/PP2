class Account:
    def __init__ (self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
    def balancecheck(self):
        return self.balance
    

account=Account("Symbat")


plus = int(input())
account.deposit(plus)
print(f"Current balance for {account.owner}: {account.balancecheck()}")

minus = int(input())
account.withdraw(minus)

print(f"Updated balance for {account.owner}: {account.balancecheck()}")

