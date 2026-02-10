import pytest
import task1
import correct_task1

@pytest.mark.parametrize(
    "order,contributes",
    [
        # --- valid contributing orders ---
        ({"status": "completed", "amount": 100}, True),
        ({"status": "completed", "amount": 0}, True),
        ({"status": "completed", "amount": -20}, True),
        ({"status": "completed", "amount": 5.75}, True),
        ({"status": "completed", "amount": "50.5"}, True),
        ({"status": "completed", "amount": "0"}, True),
        ({"status": "completed", "amount": " -10 "}, True),

        # --- cancelled (always ignored) ---
        ({"status": "cancelled", "amount": 100}, False),
        ({"status": "cancelled", "amount": "50"}, False),

        # --- structural issues ---
        ({}, False),
        ({"status": "completed"}, False),
        ({"amount": 100}, False),
        ({"status": None, "amount": 10}, True),
        ({"status": "completed", "amount": None}, False),

        # --- invalid amount ---
        ({"status": "completed", "amount": "abc"}, False),
        ({"status": "completed", "amount": ""}, False),
        ({"status": "completed", "amount": []}, False),

        # --- wrong types ---
        ("not-a-dict", False),
        (123, False),
        (None, False),
        ([], False),
    ],
    ids=lambda x: str(x),
)

def test_order_row_contribution(order, contributes):

    #result = correct_task1.calculate_average_order_value([order])

    result = task1.calculate_average_order_value([order])

    if contributes:
        assert isinstance(result, float)
    else:
        assert result == 0.0
