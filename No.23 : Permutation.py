def factorial1(num):
  fact = 1
  for i in range(1,num+1):
     fact = fact*i
  return fact

def factorial2(diff):
    fact2 = 1
    for j in range(1,diff+1):
        fact2 = fact2*j
    return fact2
G,Y,R = map(int,input().split())
num  = (G + Y + R)
r = num
diff = ( num - r )
num_fact = factorial1(num)
r_fact = factorial2(diff)
permutation = (num_fact / r_fact)
# print(factorial1(num))
# print(factorial2(diff))
print (permutation)
