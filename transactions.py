def process_transactions(transactions):
    """
    Process transaction records and return normalized totals by user.

    Expected input:
    [
        {"user_id": "u1", "amount": 100},
        {"user_id": "u2", "amount": 50},
    ]
    """
    if not isinstance(transactions, list):
        return {}

    totals = {}

    for transaction in transactions:
        if not isinstance(transaction, dict):
            continue

        user_id = transaction.get("user_id")
        amount = transaction.get("amount", 0)

        # Skip if user_id is None or empty
        if not user_id:
            continue

        # Ensure amount is numeric and not a boolean (bool is subclass of int)
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            continue

        totals[user_id] = totals.get(user_id, 0) + amount

    return totals
