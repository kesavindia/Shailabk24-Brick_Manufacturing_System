'''16 A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.
'''

# Taking input from the user for marks
marks = float(input("Enter the marks: "))

# Determining the grade based on the provided rules
if  0 <= marks<=100:
    if marks < 25:
        grade = "F"
    elif 25 <= marks < 45:
        grade = "E"
    elif 45 <= marks < 50:
        grade = "D"
    elif 50 <= marks < 60:
        grade = "C"
    elif 60 <= marks < 80:
        grade = "B"
    else:
        grade = "A"
    print(f"The corresponding grade for {marks:.0f} marks is: {grade}")
else:
    print("Entered mark is not a valid number.")

