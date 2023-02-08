class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts = []
    def __init__(self, int_rate, balance = 0):
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)


    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self

    def withdraw(self, amount):
        # your code here
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds: charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        # your code here
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance += self.balance*self.int_rate
        return self
    
    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            account.display_account_info()



# account 1 with interest rate 0.01
account_1 = BankAccount(0.01)

# account 2 with interest rate 0.01
account_2 = BankAccount(0.01)

# deposit 10, deposit 20, deposit 30, withdraw 25,
# yield interest, and display account info for account 1
account_1.deposit(10).deposit(20).deposit(30).withdraw(25).yield_interest().display_account_info()

# deposit 10, deposit 20, withdraw 50, withdraw 50, withdraw 50,
# withdraw 50, yield interest, and display account info for account 2
account_2.deposit(10).deposit(20).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()


BankAccount.all_balances()
