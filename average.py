def add(num):
    return sum(num)

def average(num):
    return add(num)/len(num)

num=list(map(int,input().split()))
print(f'Average of {num} is',average(num))
# print(len(num))