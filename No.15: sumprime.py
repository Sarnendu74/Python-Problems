n=int(input())
a=list(map(int,input().split()))
def sum(a):
    j = 0
    for i in a:
        if i % 2 == 0:
            j += i 
    return j
r=sum(a)
print(r)
