def is_strong_password(password: str) -> bool:
    if len(password)<8:
        return False
    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    return has_upper and has_lower and has_digit


password = "Hardik"
print(password)
print("Is the password strong:", is_strong_password(password))