# count and display the vowels of a given text
def count_vowels(String):
    vowels = "aeiouAEIOU"
    vowel_count = {vowel:0 for vowel in vowels}
    for char in String:
        if char in vowels:
            vowel_count[char] += 1
    print("vowel counts:")
    for char,count in vowel_count.items():
        print(f"{char}:{count}")
    print("Vowels in String:")
    for char in String:
        if char in vowel_count:
            print(char, end=" ")
Input_text = input("enter a string: ")
count_vowels(Input_text)


