# x, y, z, n = map(int, input().split())
x=int(input())
y=int(input())
z=int(input())
n=int(input())

# List comprehension to generate coordinates
coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]

# Print the result
print(coordinates)
