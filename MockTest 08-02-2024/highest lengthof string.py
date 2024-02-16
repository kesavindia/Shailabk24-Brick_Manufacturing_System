'''list1 = ['ramnetha','dreams','apple','software','developers'] find highest length of the string
 and the index value and using one for loop?'''

list1 = ['ramnetha', 'dreams', 'apple', 'software', 'developers']

# Initialize variables to store the highest length and its index
highest_length = 0
highest_length_index = None

# Iterate through the list using a for loop
for i, word in enumerate(list1):
    # Check if the current word's length is greater than the highest length found so far
    if len(word) > highest_length:
        highest_length = len(word)
        highest_length_index = i

# Print the highest length and its index
print(f"Highest length: {highest_length}")
print(f"Index: {highest_length_index}")
