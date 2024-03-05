num=int(input("Enter number: "))
reverse=0
copy_n=num
while(num != 0 ):
    digit=num % 10
    reverse=reverse*10 + digit
    num=num//10
if reverse==copy_n:
    print('Its palindrome')
else:
    print('Not palindrome')
