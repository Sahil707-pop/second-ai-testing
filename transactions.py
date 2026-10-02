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
        user_id = transaction.get("user_id")
        amount = transaction.get("amount", 0)

        # Ensure amount is numeric; treat None or non-numeric as 0
        if isinstance(amount, (int, float)):
            totals[user_id] = totals.get(user_id, 0) + amount
        else:
            totals[user_id] = totals.get(user_id, 0) + 0

    return totals


def calculate_average(transactions):
    """
    Calculate the average transaction amount.
    Returns 0 for empty lists to avoid ZeroDivisionError.
    """
    if not transactions:
        return 0
    totals = process_transactions(transactions)
    total_amount = sum(totals.values())
    if not totals:
        return 0
    return total_amount / len(totals)
