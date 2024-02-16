# Write a program to convert temperature from Celsius to Fahrenheit and vice versa.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Prompt the user to select the conversion direction
print("Select conversion direction:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

conversion_choice = int(input("Enter your choice (1 or 2): "))

# Perform the conversion based on the user's choice
if conversion_choice == 1:
    celsius_value = float(input("Enter temperature in Celsius: "))
    fahrenheit_result = celsius_to_fahrenheit(celsius_value)
    print(f"{celsius_value} Celsius is equal to {fahrenheit_result:.2f} Fahrenheit.")
elif conversion_choice == 2:
    fahrenheit_value = float(input("Enter temperature in Fahrenheit: "))
    celsius_result = fahrenheit_to_celsius(fahrenheit_value)
    print(f"{fahrenheit_value} Fahrenheit is equal to {celsius_result:.2f} Celsius.")
else:
    print("Invalid choice. Please select 1 or 2 for the conversion direction.")
