i=int(input())
m=int(input())
for j in range(1,min(i,m)+1):
    if i % j ==0 and m % j == 0:gcd=j
print(gcd)
