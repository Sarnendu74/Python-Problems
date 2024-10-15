arr = [-1,-5,1,3]
flag = 1
pos = [x for x in arr if x>0]
while flag in arr:
    flag += 1
print(flag)