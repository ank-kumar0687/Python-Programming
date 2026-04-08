
from deposite_mod import perform_deposit


import withdraw_mod as wm


import errors

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        try:
            self.balance = perform_deposit(self.balance, amount)
            print(f"Deposited {amount}. New Balance: {self.balance}")
        except errors.InvalidAmountError as e:
            print(e)

    def withdraw(self, amount):
        try:
            
            self.balance = wm.perform_withdrawal(self.balance, amount)
            print(f"Withdrew {amount}. New Balance: {self.balance}")
        except (errors.InsufficientFundsError, errors.InvalidAmountError) as e:
            print(e)

    def check_balance(self):
        print(f"Account Owner: {self.owner} | Current Balance: {self.balance}")


if __name__ == "__main__":
    acct = BankAccount("Ankit", 500)
    
    acct.check_balance()
    acct.deposit(200)   
    acct.withdraw(1000) 
    acct.withdraw(-50)  
    acct.check_balance()
