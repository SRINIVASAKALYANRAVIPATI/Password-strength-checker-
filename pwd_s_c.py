def check_password_strength(password):
 if len(password) < 8:
 return "Weak"
 has_upper = any(c.isupper() for c in password)
 has_lower = any(c.islower() for c in password)
 has_digit = any(c.isdigit() for c in password)
 has_special = any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?/~`' for c in password)
 complexity = sum([has_upper, has_lower, has_digit, has_special])
 if complexity == 4:
 return "Very Strong"
 elif complexity == 3:
 return "Strong"
 elif complexity == 2:
 return "Moderate"
else:
 return "WEAK“
password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"The strength of your password is: {strength}")
