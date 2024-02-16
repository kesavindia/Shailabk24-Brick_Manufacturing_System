def is_pangram(string):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return set(string.lower()) >= alphabet
string ="abcdefghijklmnopqrstuvwxyZ"
print(is_pangram(string))

