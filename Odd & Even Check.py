# Check conditions and print result
n=(input("Enter Number : "))
if n.isnumeric():
    n=int(n)
    if n % 2 == 1:
        print("Odd")# If n is odd
    else:
        print("Even")# If n is even and greater than 20
else:
    print("Invalid Input")

# elif 2 <= n <= 5:  # If n is even and in the inclusive range of 2 to 5
#     print("Even & Number is 2-5  ")
# elif 6 <= n <= 20:  # If n is even and in the inclusive range of 6 to 20
#     print("Even & Number is 6-20 ")

