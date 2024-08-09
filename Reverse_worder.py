'''3. Write a Python program to reverse words in a string String = “Deeptech Python Training'''

def reverse_words(input_string):
    # Split the string into words
    words = input_string.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the reversed list back into a string
    reversed_string = ' '.join(reversed_words)
    return reversed_string

# Test the function
input_string = "Deeptech Python Training"
result = reverse_words(input_string)
print(result)
