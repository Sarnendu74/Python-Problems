rows = int(input())
matrix = []
for i in range(rows):
    name = input()
    marks = float(input())
    matrix.append([name,marks])
numbers = [x[1] for x in matrix]
uniq = sorted(set(numbers))
if len(uniq) > 1:
    second_lowest = uniq[1]
else:
    second_lowest = None

name = [x[0] for x in matrix if x[1] == second_lowest]
name.sort()
for x in name:
    print(x)