from context import context
from validations import mask_account_number

def deposit_agent(amount):
    """Deposit amount to the user's balance."""
    context["balance"] += amount
    return f"Deposited successfully ! New balance is {context['balance']}"

def withdraw_agent(amount):
    """Withdraw amount if balance is sufficient."""
    if amount > context["balance"]:
        return "Insufficient balance"
    context["balance"] -= amount
    return f"Withdrawn successfully ! Remaining balance is {context['balance']}"

def check_balance_agent():
    """Return masked account number and current balance."""
    acc = mask_account_number(context["account_number"])
    return f"Account {acc} has balance: ${context['balance']}"