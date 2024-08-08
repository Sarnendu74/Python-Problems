'''5. Python program to check the validity of password input by user '''

# Get the password input from the user
password = input("Enter your password: ")

# Initialize criteria flags
length = False
digit = False
uppercase = False
lowercase = False
special_char = False

# Special characters set
special_characters = "!@#$%^&*()-_+="

# Check each character in the password using a for loop
for char in password:
    if char.isdigit():
        digit = True
    elif char.isupper():
        uppercase = True
    elif char.islower():
        lowercase = True
    elif char in special_characters:
        special_char = True

# Check the length of the password
if len(password) >= 8:
    length = True

# Validate if all criteria are met
if length and digit and uppercase and lowercase and special_char:
    print("Password is valid.")
else:
    print("Password is invalid. Please make sure it meets the criteria:")
    if not length:
        print("- At least 8 characters long.")
    if not digit:
        print("- Contains at least one numerical digit.")
    if not uppercase:
        print("- Contains at least one uppercase letter.")
    if not lowercase:
        print("- Contains at least one lowercase letter.")
    if not special_char:
        print("- Contains at least one special character (!@#$%^&*()-_+=).")
