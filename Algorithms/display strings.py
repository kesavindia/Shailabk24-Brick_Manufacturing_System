def display_strings(strings):
    for s in strings:
        print(s,end='  ')
display_strings(strings:="hello")
display_strings(strings:=["hello","Rama","Rama"])


# Example usage:
display_strings("hello")
print()  # Add a new line between the calls for better separation
display_strings(["hello", "Rama", "Rama"])