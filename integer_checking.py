''' Write a Python program that prompts the user to input an integer and raises a
ValueError exception if the input is not a valid integer.'''

def integer_check(var):
    if not isinstance(var, int):
        raise ValueError("Input must be an integer.")
    else:
        return f'Your input {var} is an integer.'

try:
    var = int(input("Enter an integer: "))
    print(integer_check(var))
except ValueError:
    print("Input must be an integer.")
