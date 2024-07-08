'''WAP to print out a set containing all the colors from color_list_1 
 which are not present in color_list_2'''
color1 = set(input("Enter Colors in set 1: ").split(" "))
color2 = set(input("Enter Colors in set 2: ").split(" "))
print("Difference is : ",color1.difference(color2))
