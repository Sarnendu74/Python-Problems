def computes(num):
    n1 = int("%i"%num)
    n2 = int("%i%i"%(num,num))
    n3 = int("%i%i%i"%(num,num,num))
    print(f'n1: {n1}\nn2: {n2}\nn3: {n3}')
    value = n1 + n2 + n3
    return value
num = int(input("Enter your number: "))
print("Sum:",computes(num))
