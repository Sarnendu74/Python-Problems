i=int(input('Enter Number: '))
if i>1:
    for j in range(2,int(i/2)+1):
        if i % j == 0:
            print("not")
            break
    else:
        print("prime")
else:
    print("not prime")
