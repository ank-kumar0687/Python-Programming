from errors import InsufficientFundsError, InvalidAmountError

def perform_withdrawal(balance, amount):
    if amount <= 0:
        raise InvalidAmountError(amount)
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount
