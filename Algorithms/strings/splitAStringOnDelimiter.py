def split_last_occurrence(input_string, delimiter):
    # Find the last occurrence of the delimiter in the string
    last_occurrence_index = input_string.rfind(delimiter)

    # Check if the delimiter is found in the string
    if last_occurrence_index != -1:
        # Split the string into two parts using the last occurrence of the delimiter
        part1 = input_string[:last_occurrence_index]
        part2 = input_string[last_occurrence_index+len(delimiter):]

        return part1, part2
    else:
        # If the delimiter is not found, return the original string
        return input_string

# Example usage:
input_string = "one,two,three,four,five"
delimiter = ","
result = split_last_occurrence(input_string, delimiter)

print("Part 1:", result[0])
print("Part 2:", result[1])













