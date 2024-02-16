# Take values of length and breadth of a rectangle from user and check if it is square or not.

# Taking input from the user for length and breadth
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

# Checking if it is a square or rectangle
if length == breadth:
    print("It is a square.")
else:
    print("It is a rectangle.")
