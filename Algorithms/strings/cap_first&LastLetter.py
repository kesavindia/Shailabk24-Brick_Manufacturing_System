# capitalize first and last letters of each word of a given string
def capitalise_first_last(word):
    if len(word) > 0:
        capword = word[0].capitalize()+word[1:-1]+word[-1].capitalize()
    else:
        return ''
    return capword
def cap_sentence(sentence):
    list_of_sentence = sentence.split()
    capletter = [capitalise_first_last(word) for word in list_of_sentence]
    cap_sentence = ' '.join(capletter)
    return cap_sentence
text= "Hello "
capitalised_text = cap_sentence(text.strip())
print(capitalised_text)