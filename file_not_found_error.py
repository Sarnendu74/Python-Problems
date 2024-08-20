''' Write a Python program that opens a file and handles a FileNotFoundError exception
if the file does not exist'''

def write_to_file(filename, details):
    try:
        with open(filename, 'w+') as file:
            file.write(details)
            file.seek(0)  # Move the pointer to the beginning of the file
            print("File Details are: ")
            lines = file.read()  # Read the contents of the file
            return lines
    except FileNotFoundError:
        return "Error! File not found."

filename = input("Enter your file name: ")
details = input("Enter the details you want to add to your file: ")
print(write_to_file(filename, details))

                
            