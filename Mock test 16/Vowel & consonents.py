def count_vowel(string):
    vowel_count = 0
    consonant_count = 0
    for char in string:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            vowel_count += 1
        else:
            consonant_count += 1
    print("Vowel count: ",vowel_count)
    print("Consonant count: ",consonant_count)

string = input("Enter a string: ")
print(count_vowel(string))