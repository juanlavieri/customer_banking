# Inside savings_account.py

from Account import Account

def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    This function creates a savings account with the given balance and interest rate, calculates the interest earned
    over the given number of months, and updates the account balance accordingly. The updated balance and interest
    earned are returned as a tuple.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        tuple: A tuple containing the updated savings account balance and the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    savings_account = Account(balance, 0)  # Initially, the interest is set to 0

    # Calculate interest earned
    interest_earned = balance * (interest_rate / 100) * (months / 12)

    # Update the savings account balance by adding the interest earned
    updated_balance = balance + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the Account class.
    savings_account.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the Account class.
    savings_account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return updated_balance, interest_earned
