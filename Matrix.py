matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
transpose = [[row[a] for row in matrix] for a in range(3)]
# print(len(matrix[0]))
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=" ")
    print()
    
# Reverse matrix
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
for t in matrix:
    print(t)
transpose = [[row[a] for row in matrix] for a in range(3)]
print(transpose)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(transpose[i][j], end=" ")
    print()