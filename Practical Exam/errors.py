

class BankingError(Exception):
    """Banking application ki sabhi errors ke liye base class."""
    pass

class InsufficientFundsError(BankingError):
    """Jab balance withdrawal amount se kam ho."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Transaction Failed: Insufficient Funds. Balance: {balance}, Attempted: {amount}"
        super().__init__(self.message)

class InvalidAmountError(BankingError):
    """Jab amount zero ya negative ho."""
    def __init__(self, amount):
        self.amount = amount
        self.message = f"Transaction Failed: {amount} is an invalid amount. Please enter a positive value."
        super().__init__(self.message)
