# Assume a dictionary
dicti = {x:x**2 for x in range(1,11)}
print("N is Numbers & S is Squares")
print("N :","S")
# Displaying line by line 
for i,j in dicti.items():
    print(f'{i} : {j}')