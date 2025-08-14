
def validate_amount(amount):
    """Amount positive number validation."""
    return amount.isdigit()and int(amount) > 0

def validate_account_number(acc_num):
    """Account number format validation."""
    return acc_num.isdigit() and len(acc_num) == 10

def mask_account_number(acc_num):
    """Mask all but the last four digits of the account number."""
    return"****" + acc_num[-4:]