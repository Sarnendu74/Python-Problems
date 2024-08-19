''' Program to count the number of vowels and consonants, digits and special characters '''

# Initialize string
string = input("Enter string: ").lower()  # Convert string to lowercase for easy comparison
vowels = consonants = digits = special_characters = 0

# Assumed the vowels, consonants, digits, special_characters
vo = "aeiou"
co = "bcdfghjklmnpqrstvwxyz"
di = "0123456789"
spe = "!@~#$%^&*()_+:?/<.>,"

# Iterate over the string
for char in string:
    if char in vo:
        vowels += 1
    elif char in co:
        consonants += 1
    elif char in di:
        digits += 1
    elif char in spe:
        special_characters += 1

# Displaying numbers of vowels, consonants, digits, special_characters
print(f'Your string is "{string}"')
print(f'No. of vowels in the string: {vowels}')
print(f'No. of consonants in the string: {consonants}')
print(f'No. of digits in the string: {digits}')
print(f'No. of special characters in the string: {special_characters}')
