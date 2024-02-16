# lowercase first n characters in a string
def lower_first_nChars(string,n):
    if n<=0:
        return string
    first_N_lower_chars = string[:n].lower()
    resultString = first_N_lower_chars + string[n:].upper()
    return resultString
string ='KeSavan'
n=3
result = lower_first_nChars(string,n)
print(result)