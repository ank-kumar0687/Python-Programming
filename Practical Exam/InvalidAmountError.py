class BankingError(Exception):
    pass

class InsufficientFundsError(BankingError):
    
    def __init__(self, balance, amount):
        self.message = f"Transaction failed: Balance is {balance}, but tried to withdraw {amount}."
        super().__init__(self.message)

class InvalidAmountError(BankingError):
   
    def __init__(self, amount):
        self.message = f"Transaction failed: {amount} is not a valid amount."
        super().__init__(self.message)
