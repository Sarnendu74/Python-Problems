import random as rd
num=rd.randrange(1,10)
a=int(input("Enter number between 0-10: "))
while num != a:
    if num>a:
        print("Too Small !")
        a=int(input("Enter number between 0-10: "))
    elif num<a:
        print("Too High")
        a=int(input("Enter number between 0-10: "))
    else:
        break        
print("Correct Choice")
    