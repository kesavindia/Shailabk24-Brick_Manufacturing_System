'''generate all the permutation of a given string
	Input: S = “ABC”
	Output: “ABC”, “ACB”, “BAC”, “BCA”, “CBA”, “CAB”'''
def permutation(string):
    if len(string) == 1:
        return [string]
    else:
        perms = []
        for i in range(len(string)):
            char = string[i]
            rest = string[:i] + string[i+1:]
            for p in permutation(rest):
                perms.append(char+p)
        return perms

s = input("Enter a string: ")
print(permutation(s))

