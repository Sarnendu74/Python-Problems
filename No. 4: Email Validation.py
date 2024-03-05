import re

def validate_email(email):
    # Define the regular expression pattern for a valid email address
    pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# Get user input for email
user_email = input("Enter your email address: ")

# Validate the entered email
if validate_email(user_email):
    print("Valid email address.")
else:
    print("Invalid email address. Please enter a valid email.")
