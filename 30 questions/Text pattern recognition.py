'''30.	Pattern Recognition in Text: Develop a program that takes a text input and identifies
patterns such as repeated words, palindromes, or specific sequences. Use loops to analyze the
text and provide relevant information.'''
def identify_patterns(text):
    words = text.lower().split()

    # Identify repeated words
    repeated_words = set()
    unique_words = set()

    for word in words:
        if word in unique_words:
            repeated_words.add(word)
        else:
            unique_words.add(word)

    # Identify palindromes
    palindromes = [word for word in words if word == word[::-1]]

    # Print results
    print("\nIdentified Patterns:")
    print(f"Repeated Words: {', '.join(repeated_words)}")
    print(f"Palindromes: {', '.join(palindromes)}")
    print(words)
    print(unique_words )


# Get user input for the text
text_input = input("Enter text: ")

# Call the function to identify patterns
identify_patterns(text_input)
