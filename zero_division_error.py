''' Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero'''


# Define a divide function 
def divide(num1,num2):
    # Use exception handling for handle zerodivision error
    try:
        result = num1/num2
        return f'Quotient is : {result} '
    except ZeroDivisionError as zero:
        return ("Error: Division by zero is not allowed")

def main():
    # Get user input for two numbers
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    # Invoke the function
    print(divide(num1,num2))
    
if __name__ == "__main__":
    main()