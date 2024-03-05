#Style
print("********************************************* Welcome To Ghosh's Calculator***********************************************************")
def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def divide(num1,num2):
    if num2 != 0:
        return num1/num2
    else :
        return ("can't divide by zero") 
def multiplication(num1,num2):
    return num1*num2
def exponentiation(num1,num2):
    return num1**num2
def modulus(num1,num2):
    return num1%num2
def floordivision(num1,num2):
    return num1//num2
def invalid(num1,num2):
    return("Invalid Input")
num1=float(input("Enter your first number: "))
num2=float(input("Enter your second number: "))
print("Operations are :'+','-','/','*','**','%','//'")
#Extra test
# print("-")
# print("/")
# print("*")
# print("**")
# print("%")
# print("//")
operation=input("Enter Operation: ")
if operation=='+':
    result = add(num1,num2)
elif operation=='-':
    result = subtract(num1,num2)
elif operation=='/':
    result = divide(num1,num2)
elif operation=='*':
    result= multiplication(num1,num2)
elif operation=='**':
    result = exponentiation(num1,num2)
elif operation=='%':
    result=modulus(num1,num2)
elif operation=='//':
    result=floordivision(num1,num2)
elif operation != "+" "-" '/' '*' '**' '%' '//':
    result=invalid(num1,num2)
print(f"Result: {result}")
