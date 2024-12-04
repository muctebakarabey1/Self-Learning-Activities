# user_data.py
import re

def is_valid_age(age):
    if age < 18 or age > 100:
        return False
    return True

def is_valid_email(email):
    # Basit bir e-posta doğrulama düzeni (regex ile)
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(regex, email):
        return True
    return False

def validate_user_data(users):
    invalid_users = []
    for user in users:
        if not is_valid_age(user['age']):
            invalid_users.append(f"Invalid age for {user['name']}")
        if not is_valid_email(user['email']):
            invalid_users.append(f"Invalid email for {user['name']}")
    return invalid_users


def validate_age(age):
    if age>100 or age<1:
        return False
    else:
        return True