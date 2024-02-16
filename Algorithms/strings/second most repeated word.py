from collections import Counter

def second_most_repeated_word(string):
    words = string.split()
    word_frequency = Counter(words)

    # Find the two highest frequencies
    if len(word_frequency) < 2:
        return "Not enough distinct words for a second most repeated word."

    first_most_freq = max(word_frequency.values())
    second_dict = {word: freq for word, freq in word_frequency.items() if freq < first_most_freq}

    # Check if there is a second most repeated word
    if not second_dict:
        return "No second most repeated word."

    second_most_freq = max(second_dict.values())

    # Find the second most repeated word(s)
    second_most_freq_word = [word for word, freq in second_dict.items() if freq == second_most_freq]

    return second_most_freq_word

# Example usage:
input_string = input("Enter a string: ")
second_max_repeated_word = second_most_repeated_word(input_string)
print("Second Most Repeated Word(s):", second_max_repeated_word)
