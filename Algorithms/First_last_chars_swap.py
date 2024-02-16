'''
I. REQUIREMENT GATHERING: Swapping the First and Last Characters of a String.
        ------------------------------------
        | Enter String: |______________|    |
        |     Submit                        |
        |___________________________________|

        Output: Swapped String: olloWorlH
    Notes:
        The customer will provide a string containing any characters.
        The string might consist of a single character, a single word, multiple words, or multiline statements.
        The requirement is to swap the first and last characters of the input string and display the result.
     
     1. Functional Analysis:   
        Input: A string containing any characters.
        Output: The swapped string with the first and last characters swapped.
            Scenarios:
                i. Empty string: "Invalid String"
                ii. Single character: "Enter at least 2 characters"
                iii. Single word: Swap the first and last characters.
                iv. Multiple words: Swap the first and last characters of each word.
                v. Combining characters: Swap the first and last characters.
                vi. Multiline string: Swap the first and last characters in multiline strings.
                vii. Including spaces: Include spaces in the swapping operation.
    2. Technical Analysis:
    
    Entity Name: SwapFirstLastChars
    State:
    Data Types: STRING
    Behavior:
    Operators: =, +=
    Decision Making: if
    Loops: Yes (For Loop)
    
    III. DESIGN (Sequence Diagrams):
    Mathematics:
        Write it on paper
        'Hello World'
        Initialize variables: swapped_string = ""
        Traverse through each character
        Swap the first and last characters and append to swapped_string
    '''

# STATE:
input_str = 'Hello World'
swapped_string = ""

# BEHAVIOR:
for char in input_str:
    if len(input_str) < 2:
        swapped_string = "Enter at least 2 characters"
        break
    else:
        swapped_string += input_str[-1]  # Append last character
        for i in range(1, len(input_str) - 1):
            swapped_string += input_str[i]  # Append middle characters
        swapped_string += input_str[0]  # Append first character

print("Swapped String:", swapped_string)
