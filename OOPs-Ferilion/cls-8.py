'''.Write a class method get_max() in a
class called MathUtils that takes a list of numbers
 as input and returns the maximum value using cls.'''

class MathUtils:

    @classmethod
    def get_max(cls,list):
        if not list:
            raise ValueError("Empty list provided.")
        max_value = list[0]
        for num in list:
            if num > max_value:
                max_value = num
        return  max_value
    #Example usage with dynamic input
numbers =[]
while True:
    num_str = input("Enter a number(or 'done' to finish): ")
    if num_str == 'done':
        break;
    try:
        numbers.append(float(num_str))
    except ValueError:
        print("Invalid input. Please enter a number.")
max_number = MathUtils.get_max(numbers)
print(max_number)
