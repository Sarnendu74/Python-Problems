numbers=[25,50,25,30,20]
sum=0
for i in numbers:
    mean=0
    sum=i+sum
    mean=sum/len(numbers)
print(f'mean of {numbers} is {mean}')