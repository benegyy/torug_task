import re


def count_valid_emails(emails):

    if not emails:
        return 0

    email_pattern = re.compile(r'^(?=.{1,254}$)(?=.{1,64}@)[A-Za-z0-9](?:[A-Za-z0-9._%+-]{0,62}[A-Za-z0-9])?@(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+[A-Za-z]{2,63}$')

    count = 0

    for email in emails:
        if not isinstance(email, str):
            continue

        # Reject empty strings
        if not email:
            continue

        # Reject any leading/trailing whitespace
        if email != email.strip():
            continue

        # Reject any whitespace anywhere
        if any(c.isspace() for c in email):
            continue

        if email_pattern.match(email):
            count += 1

    return count