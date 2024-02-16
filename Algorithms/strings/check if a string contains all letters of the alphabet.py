import string

def contains_all_alphabet_letters(input_string):
    # Convert the input string to lowercase for case-insensitive comparison
    input_string_lower = input_string.lower()

    # Check if the set of lowercase alphabet letters is a subset of the input string
    return set(string.ascii_lowercase).issubset(set(input_string_lower))

# Example usage
test_string = "The quick brown fox jumps over lazy dog"
result = contains_all_alphabet_letters(test_string)

print(f"Test string: {test_string}")
print(f"Contains all alphabet letters: {result}")
