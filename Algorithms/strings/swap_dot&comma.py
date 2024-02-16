# swap comma and dot in a string
def swap_comma_and_dot(input_string):
    # Define a translation table to swap commas and dots
    translation_table = str.maketrans({',': '.', '.': ','})

    # Use translate to perform the swap
    swapped_string = input_string.translate(translation_table)

    return swapped_string

# Example usage
original_string = "1,000.25 is the result."
swapped_string = swap_comma_and_dot(original_string)

print(f"Original string: {original_string}")
print(f"Swapped string: {swapped_string}")
