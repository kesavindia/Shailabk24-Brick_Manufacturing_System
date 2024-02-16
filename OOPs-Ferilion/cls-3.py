'''Implement an instance method get_length() in a
class called StringUtils that takes a string as input and
returns its length using self.'''
class StringUtils:
    def get_length(self,string):
        return len(string)
str = StringUtils()
length = str.get_length("Kesavan")
print(length)
