def validate_password(password):
    if not isinstance(password, str):
        print("Password must be a string")
        return False

    if len(password) <= 8 or len(password) >= 20:
        print("Password length must be between 8 and 20 characters")
        return False

    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isspace():
            print("Password must not contain spaces")
            return False
        
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        # Checking special character
        elif not char.isalnum():
            has_special = True

    if not has_uppercase:
        print("Password must contain at least one uppercase letter")
        return False
    if not has_lowercase:
        print("Password must contain at least one lowercase letter")
        return False
    if not has_digit:
        print("Password must contain at least one digit")
        return False
    if not has_special:
        print("Password must contain at least one special character")
        return False

    return True

if __name__ == '__main__':
    password = input("Input your password: ")
    if validate_password(password):
        print(f"{password} is valid.")
    else:
        print(f"{password} is not valid.")