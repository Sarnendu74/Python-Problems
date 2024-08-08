'''Qn 4. Python program to get the Fibonacci series between 0 to 50'''
# Initialize the first two Fibonacci numbers
a, b = 0, 1

# Print the Fibonacci series between 0 and 50 using a for loop
print("Fibonacci series between 0 and 50:")

for _ in range(50):
    if a > 50:
        break
    print(a, end=" ")
    # Update the values of a and b
    a, b = b, a + b
