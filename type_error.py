'''  Write a Python program that prompts the user to input two numbers and raises a
TypeError exception if the inputs are not numerical'''

# Define a function to checking type of inputs

def check(input_str):
    if not input_str.isdigit():
        raise TypeError("Inputs should be numerical")
    else:
        return int(input_str)

def main():
    try:
        num1 = check(input("Enter your first number: "))
        num2 = check(input("Enter your second number: "))
        li = [num1, num2]
    except TypeError as e:
        print(e)
    else:
        print("The sum of the two numbers is:", sum(li))

if __name__ == "__main__":
    main()
