pythagoras = [(x,y,z) for x in range(1,10) for y in range(x,10) for z in range(y,10) if z**2 == x**2 + y**2]
print(pythagoras)
