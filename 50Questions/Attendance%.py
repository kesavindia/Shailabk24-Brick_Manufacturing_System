
# A student will not be allowed to sit in exam if his/her attendence is less than 75%

# Taking input from the user
classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

# Calculating the attendance percentage
attendance_percentage = (classes_attended / classes_held) * 100

# Displaying the percentage of classes attended
print(f"Percentage of classes attended: {attendance_percentage:.2f}%")

# Checking if the student is allowed to sit in the exam
if attendance_percentage >= 75:
    print("The student is allowed to sit in the exam.")
else:
    print("The student is not allowed to sit in the exam due to low attendance.")
