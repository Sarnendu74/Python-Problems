''' Qn. Python program to check if the given string is a palindrome '''

# Initialize input_str to taking input from users
# input_str = input("Enter your string for checking Palindrome:")

# Initialize given input

input_str = "Racecar"

# Remove whitespaces and converting to lower case & storing
str_without_spaces = input_str.replace(" ", "").lower()

# Create variable for storing copy of the original
str_copy = str_without_spaces

# Initialize reverse_str
reverse_str = ""

# Use for loop reverse string
for i in str_without_spaces:
    reverse_str = i + reverse_str

# Checking Palndrome and Display
if reverse_str == str_copy:
    print(f'Your {str_copy.capitalize()} string is Palindrome')
else:
    print(f"{str_copy.capitalize()} string isn't Palindrome")
    