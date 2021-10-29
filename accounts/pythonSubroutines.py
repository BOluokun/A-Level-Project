from .models import User

def validate_details(email, password):
    valid_password = False
    valid_email = False
    special_characters = [
    '@', '!', '£', '%', '^', '&',
    '*', '(', ')', '-', '_', '=',
    '+', '?', '[', ']', '{', '}'
    ]
    lower = 0
    upper = 0
    digit = 0
    special = 0
    for char in password:
        if char in special_characters:
            special += 1
        elif char.isalpha():
            if char.islower():
                lower += 1
            elif char.isupper():
                upper += 1
        elif char.isdigit():
            digit += 1
    if special > 0 and lower > 0 and upper > 0 and digit > 0 and len(password) >= 8:
        valid_password = True
    if '@' in email and '.' in email and email[-1] != '@' and email[-1] != '.':
        valid_email = True
    if valid_password and valid_email:
        return True
    else:
        return False

def make_record(username, email, password):
    account = User(username = username, email = email, password = password)
    account.save()
    return account

def check_details(username, password):
    found = False
    records = User.objects.all()
    for account in records:
        if account.username == username and account.password == password:
            found = True
    return found
