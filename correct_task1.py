def calculate_average_order_value(orders):
    if not orders:
        return 0.0

    total = 0
    count = 0

    for order in orders:
        # validate order is dict
        if not isinstance(order, dict):
            continue

        # check fields exist
        if "status" not in order or "amount" not in order:
            continue

        # skip cancelled orders
        if order["status"] == "cancelled":
            continue

        try:
            amount = float(order["amount"])
            total += amount
            count += 1
        except (ValueError, TypeError):
            # skip orders with invalid amounts
            continue

    # avoid division by zero
    if count == 0:
        return 0.0

    return total / count