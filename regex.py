import re

email_regex = r"[A-Za-z0-9._-]+@[A-Za-z0-9.-]+.(com|edu)(.[A-Za-z]{2,})?"

def is_valid_email(email):
    return bool(re.fullmatch(email_regex, email))

# Testing the function with some example emails
valid_emails = [
    "jemimah@care.com",
    "jemimah98@care.edu",
    "jemimah_jones@pts.care.edu",
    "20s.jemimah_jones-93@happy.go8.lucky.com"
]

invalid_emails = [
    "jemimah_care.com – missing @",
    "jemimah98@care.co.uk – <domain name> must end in “.edu” or “.com",
    "jemimah_jones*@care.edu – ‘*’ is not allowed in <username> or <domain name>",
    "20s.jemimah_jones-93@happy.go8..lucky.com– not well-formed"
]

for email in valid_emails:
    try:
        assert is_valid_email(email)
    except AssertionError:
        print(f"Something wrong in Valid email: {email}")

for email in invalid_emails:
    try:
        assert not is_valid_email(email)
    except AssertionError:
        print(f"Something wrong in Invalid email: {email}")
