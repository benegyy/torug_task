import pytest
import math
import correct_task3
import task3
@pytest.mark.parametrize(
    "value,contributes",
    [
        # --- valid numeric ---
        (10, True),
        (5.5, True),
        (0, True),
        (-3, True),
        (1e6, True),
        (-1e-6, True),
        ("123", True),
        (" 45.6 ", True),
        (True, True),
        (False, True),

        # --- invalid ---
        (None, False),
        ("invalid", False),
        ("", False),
        (" ", False),
        (float("nan"), False),
        (float("inf"), False),
        (float("-inf"), False),
        ([], False),
        ({}, False),
        (object(), False),
    ],
    ids=lambda x: str(x),
)

def test_measurement_row_contribution(value, contributes):

    #result = correct_task3.average_valid_measurements([value])

    result = task3.average_valid_measurements([value])

    if contributes:
        assert isinstance(result, float)
    else:
        assert result == 0.0
