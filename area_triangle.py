# Declare three variables which store 3 sides value of triangle
first_Side = 3
second_Side = 6
third_Side = 9

# Calculate the semi-perimeter
s = (first_Side + second_Side + third_Side) / 2

# Apply Heron's formula
area = (s * (s - first_Side) * (s - second_Side) * (s -third_Side)) ** 0.5

# Print the result
print("The area of the triangle with sides",first_Side,",",second_Side,"and", third_Side,"is",area,"square units.")