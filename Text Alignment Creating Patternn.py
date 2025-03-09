c = "H"
r = 1
thickness = int(input())

# Top Plane
for i in range(thickness):
    print((c * (2 * i + 1)).center(thickness * 2 - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).rjust(thickness +(thickness//2)  ) + (c * thickness).rjust((thickness *5)-thickness))
    
# Middle Part
# Middle Part (Shifted by 2 Spaces)
for i in range((thickness // 2) + 1):
    print((c * (thickness * 5)).rjust(thickness*5 + (thickness//2)))  # Increased padding by 2

    
# Down Part
for i in range(thickness + 1):
    print((c * thickness).rjust(thickness + (thickness//2)) + (c * thickness).rjust((thickness * 5)-thickness))  # Increased padding by 1                                                                 ))
# Last Plane (Adjusted for Correct Positioning)
# Last Plane (Proper Alignment)
for i in range(thickness):
    print((c * (2 * (thickness - i) - 1)).center(thickness * 10))  # Increase padding width


