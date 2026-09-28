def process_transactions(transactions):
    """
    Process transaction records and return normalized totals by user.

    Expected input:
    [
        {"user_id": "u1", "amount": 100},
        {"user_id": "u2", "amount": 50},
    ]
    """
    totals = {}

    for transaction in transactions:
        user_id = transaction["user_id"]
        amount = transaction["amount"]

        # BUG: assumes amount is always numeric.
        # A transaction containing None causes TypeError.
        totals[user_id] = totals.get(user_id, 0) + amount

    return totals
