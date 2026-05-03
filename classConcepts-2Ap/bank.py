# 2. Create a class BankAccount with:

# . Data members: account_holder, balance
# . A constructor to initialize values
# . Member functions:
# o deposit (amount) ->adds money
# o withdraw (amount) -> deducts money (check sufficient balance)
# o display_balance () -> shows current balance

# Create 2 or 3 account objects. Perform deposit and withdrawal operations. Display final balance


class BankAccount():
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def display_details(self):
        print(f"Name: {self.account_holder}")

    def deposit(self,amount):
        self.balance += amount
        print(f"Your balance is credited by {amount}/-")
    
    def withdraw(self,amount):
        self.balance -= amount
        print(f"Your balance is debited by {amount}/-")

    
    def display_balance(self):
        print(f"Your Current balance is {self.balance}")


customer1 = BankAccount("Nidhi", 500)
customer1.display_details()
customer1.deposit(5000)
customer1.withdraw(100)
customer1.display_balance()