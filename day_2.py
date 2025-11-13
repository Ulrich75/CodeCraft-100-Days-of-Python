password = input("Enter your password: ")

length_ok = len(password) >= 8
has_digit = any(c.isdigit() for c in password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)

if length_ok and has_digit and has_upper and has_lower:
    print("\n Secure password ")
else:
    print("\n Weak password ")
    print("- Password must  be at least 8 characters long,one digit, one uppercase letter,one   lowercase letter")
    
