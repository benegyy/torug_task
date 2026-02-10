import math


def average_valid_measurements(values):
    if not values:
        return 0.0

    total = 0
    count = 0

    for v in values:
        if v is None:
            continue

        try:
            numeric_value = float(v)

            # Exclude infinity and NaN
            if math.isnan(numeric_value) or math.isinf(numeric_value):
                continue

            total += numeric_value
            count += 1
        except (ValueError, TypeError):
            continue

    if count == 0:
        return 0.0

    return total / count