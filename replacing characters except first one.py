name = input("Enter Name: ")
char = name[0]
name = name.replace(char,"$")
name = char + name[1:]
print(name)

# output is 
# Enter Name: onion
# oni$n
