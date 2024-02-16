def count_digit_alpha(string):
    letter_count = 0
    digit_count = 0
    others = 0
    for char in string:
        if char.isdigit():
            digit_count += 1
        elif char.isalpha():
            letter_count += 1
        else:
            others += 1
    return letter_count,digit_count,others
input_str = input("Enter something to count: ")
result = count_digit_alpha(input_str)  #result in tuple
letter_count,Digit_count,Other_chars = result
print("Letter count: ",letter_count)
print("Digit count: ",Digit_count)
print("Other characters count: ",Other_chars)

