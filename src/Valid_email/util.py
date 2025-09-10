import re

def validate_email(s):
    
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    if re.match(pattern, s):
        return True
    return False

def filter_mails(email_list):
    """
    Filter valid emails and return them in lexicographical order.
    """
    valid_emails = []
    for email in email_list:
        if validate_email(email):
            valid_emails.append(email)
    return sorted(valid_emails)