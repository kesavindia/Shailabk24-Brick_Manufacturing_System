'''Write a program that requires the user to enter a single character from the alphabet. Print Vowel
or Consonant, depending on user input. If the user input is not a letter (between a and z or A and Z),
or is a string of length > 1, print an error message.'''

# Taking input from the user
character = input("Enter a single character from the alphabet: ")

# Checking the conditions and printing the appropriate message
if len(character) == 1 and character.isalpha():
    # Converting the input to lowercase for easier comparison
    character = character.lower()

    if character in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Error: Please enter a single alphabet character.")
