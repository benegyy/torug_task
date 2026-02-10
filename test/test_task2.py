import pytest
import task2
import correct_task2

@pytest.mark.parametrize(
    "email,expected_valid",
    [
        # --- valid ---
        ("user@example.com", True),
        ("first.last@example.co.uk", True),
        ("user+tag@domain.org", True),
        ("u.ser_123@sub.domain.com", True),
        ("a@b.co", True),
        ("john..doe@example.com", True),

        # --- invalid format ---
        ("john.@example.com", False),
        (".john@example.com", False),
        ("invalid-email", False),
        ("@domain.com", False),
        ("user@", False),
        ("userdomain.com", False),
        ("user@@domain.com", False),
        ("user@domain", False),
        ("user@.com", False),
        ("user@domain.", False),
        ("user@gmail", False),
        ("@@", False),
        ("@", False),

        ("@gmail.com", False),
        ("user@", False),
        ("usergmail.com", False),
        ("user@@gmail.com", False),

        # --- whitespace (strict) ---
        (" user@domain.com", False),
        ("user@domain.com ", False),
        (" user@domain.com ", False),
        ("user @domain.com", False),
        ("user@ domain.com", False),
        ("user@domain .com", False),

        # --- empty / non-string ---
        ("", False),
        (" ", False),
        (None, False),
        (123, False),
        ([], False),
        ({}, False),
    ],
    ids=lambda x: str(x),
)

def test_email_validity(email, expected_valid):
    #result = correct_task2.count_valid_emails([email])
    result = task2.count_valid_emails([email])
    assert (result == 1) == expected_valid
