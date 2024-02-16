def reverse_string(input_string):
    def reverse_word(word):
        reversed_word = ""
        for char in word:
            reversed_word = char+reversed_word
        return reversed_word
    words = []
    curr_string = ''
    for char in input_string:
        if char.isspace():
            if curr_string:
                words.append(curr_string)
            curr_string = ''
        else:
           curr_string += char
    if curr_string:
        words.append(curr_string)
    reversed_words = [reverse_word(word) for word in words]
    reversed_strings = reversed_words[::-1]
    result_str = ""
    for reversed_string in reversed_strings:
        result_str += reversed_string+" "
    return result_str.strip() #will remove the leading and trailing spaces in the string
input_str = input("Enter a string: ")
res = reverse_string(input_str)
print(res)
