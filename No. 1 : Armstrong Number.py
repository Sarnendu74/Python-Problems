num=int(input("Enter number: "))
order=len(str(num))
copy_n=num
sum=0
while num>0:
    digit=num%10
    sum += digit **order
    num = num//10
if sum==copy_n:
    print("Armstrong")
else:
    print("Not Armstrong")
