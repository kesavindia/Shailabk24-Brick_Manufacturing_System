'''function to check a number is palindrome or not'''
def is_palindrome(num):
    """Checks if a number is a palindrome.
    Returns True if the number is a palindrome, False otherwise.
    """

    if num < 0:
        return False

    original_num = num
    reversed_num = 0
    while num > 0:
        remainder = num % 10
        reversed_num = reversed_num * 10 + remainder
        num //= 10

    return original_num == reversed_num

# Test cases
num = int(input("Enter a number: "))
print(is_palindrome(num))
