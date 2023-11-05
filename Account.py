""" Create a Account class with methods"""

class Account:
    """A class that represents a bank account.

    Attributes:
        balance (float): The current balance of the account.
        interest (float): The interest rate of the account.

    Methods:
        set_balance(balance: float) -> None: Sets the balance of the account.
        set_interest(interest: float) -> None: Sets the interest rate of the account.
    """
    def __init__(self, balance: float, interest: float):
        self.balance = balance
        self.interest = interest

    def set_balance(self, balance: float) -> None:
        """Sets the balance of the account."""
        self.balance = balance

    def set_interest(self, interest: float) -> None:
        """Sets the interest rate of the account."""
        self.interest = interest
class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest
