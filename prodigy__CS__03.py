password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1
else:
    print("Your password is too short. Make it at least 8 characters.")

if any(char.isupper() for char in password):
    score += 1
else:
    print("Add at least one uppercase letter (A-Z).")

if any(char.islower() for char in password):
    score += 1
else:
    print("Add at least one lowercase letter (a-z).")

if any(char.isdigit() for char in password):
    score += 1
else:
    print("Add at least one number (0-9).")

if any(char in "!@#$%^&*()_+" for char in password):
    score += 1
else:
    print("Add at least one special character (!, @, #, etc).")

print("\n--- Result ---")
if score == 5:
    print(" Strong Password")
elif score >= 3:
    print("Moderate Password")
else:
    print("Weak Password")
input("Press Enter to exit...")
