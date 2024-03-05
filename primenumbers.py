import math
n=int(input("Enter range: "))
for i in range(1,n):
    k=int(math.sqrt(i))
    for j in range(2,k+1):
        if i % j == 0:
            break
    else:
        print(i)
            