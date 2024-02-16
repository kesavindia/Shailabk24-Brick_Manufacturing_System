def firstrepeatedword(string):
    words = string.split()
    seen_words = set()
    for word in words:
        if word in seen_words:
            return word
        seen_words.add(word)
    return None
input_string = input("Enter a string: ")
repeated_word = firstrepeatedword((input_string))
print("Repeated word:",repeated_word)