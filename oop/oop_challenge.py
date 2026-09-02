class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f"Current Balance: {self.balance}")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds") 
        else:    
            self.balance -= amount
            print(f"Current Balance: {self.balance}")

my_account = Account("Jose", 100)
print(my_account.balance)
my_account.deposit(350)
my_account.withdraw(200)
my_account.withdraw(1275)
my_account.deposit(900)
my_account.withdraw(315)