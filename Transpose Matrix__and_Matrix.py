# MATRIX

# INITIALIZE MATRIX LIST
matrix = [[1,2,3],[5,4,9],[8,6,7]]

print("MATRIX IS :----")

# Iterate over the length of list for initialize row
for i in range(len(matrix)):
    # Iterate over the first list elements for initialize column
    for j in range(len(matrix[0])):
        # Displaying Matrix
        print(matrix[i][j],end=" ")
    # Jump to the next line
    print()
    

# TRANSPOSE MATRIX

# INITIALIZE MATRIX LIST
matrix = [[1,2,3],[5,4,9],[8,6,7]]

print("Reverse Matrix IS :----")
# Iterate over the length of list for initialize row
for i in range(len(matrix)):
    # Iterate over the first list elements for initialize column
    for j in range(len(matrix[0])):
        # Displaying Matrix
        print(matrix[j][i],end=" ")
    # Jump to the next line
    print()