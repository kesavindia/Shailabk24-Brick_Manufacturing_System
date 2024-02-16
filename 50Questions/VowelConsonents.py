'''Write a program that requires the user to enter a single character from the alphabet.
Print Vowel or Consonant, depending on user input.
If the user input is not a letter (between a and z or A and Z), or is a string of length > 1,
print an error message.
'''

'''
REQUIREMENT GATHERING:

---------------------------------------
| Enter Character: |_______________|   |
|           Submit                    |
|______________________________________|

ANALYSIS:

Functional Analysis:
User will provide a single character from the alphabet.
Empty value: "Invalid input, please enter a character."
Multiple characters: No
Numbers allowed: No
Special characters allowed: No

Technical Analysis:
Entity Name: CharacterTypeChecker
State: Data types - STRING, Error messages - STRING
Behavior: Operators - IF, ELIF, ELSE; Loops - None

DESIGN (Sequence Diagrams):

Mathematics:
1. Check if a character is provided and it's a single character.
2. Check if the character is a letter.
3. Determine if the letter is a vowel or consonant.
4. Print the result.

Programming Language:
State: Define a character given by the user.

Behavior:
1. Check if a character is provided and it's a single character.
2. Check if the character is a letter.
3. Determine if the letter is a vowel or consonant.
4. Print the result.
'''

print("Q6 CharacterTypeChecker")

character_input = input("Enter Character: ")

if not character_input or len(character_input) != 1 or not character_input.isalpha():
    print("Invalid input, please enter a character.")
else:
    character = character_input.lower()
    vowels = ["a", "e", "i", "o", "u"]
    if character in vowels:
        print("Vowel")
    else:
        print("Consonant")