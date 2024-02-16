'''Develop a program with a dynamic menu system where users can navigate through different options.
 Use nested if statements to handle user input and execute the corresponding functionality.'''

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Error: Division by zero.")
        return None

# Dynamic menu
while True:
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = add(num1, num2)
        print(f"The sum is: {result}")
    elif choice == '2':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = subtract(num1, num2)
        print(f"The difference is: {result}")
    elif choice == '3':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = multiply(num1, num2)
        print(f"The product is: {result}")
    elif choice == '4':
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        result = divide(num1, num2)
        if result is not None:
            print(f"The quotient is: {result}")
    elif choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
