# #Voter assignment:

# print("Check your voting eligibility.")
# name = (input("Enter your name: "))
# age = int(input("Enter your age: "))
# if 0 > age > 130:
#     print(f"{name} have entered invalid age.")
# elif age < 18:
#     print(f"{name} is not an adult and not eligible to vote")
# elif age < 60:
#     print(f"{name} is an adult  and eligible to vote")
# else:
#     print(f"{name} is a senior citizen and eligible to vote")

# #Grades assignment
def check_grade():
    student_name = input("Enter the student's name: ")
    subjects = ["Math", "Science", "English", "History", "Computer Science"]
    marks = []
    total_marks = 0
    for subject in subjects:
        while True:
            try:#for this problem, we can do even without try and except.
                student_mark = int(input(f"Enter marks for {subject}: "))
                if 0 <= student_mark <= 100:
                    marks.append(student_mark)
                    break  # Valid mark entered, break out of the loop
                # else:
                #     print(f"Invalid marks entered for {subject}. Please enter a value between 0 and 100.")
            except Exception:
                print("Please enter a valid numerical value for marks.")
    for i in marks:
        total_marks += i
    average_marks = total_marks/len(subjects)
    percetage_of_marks = total_marks/500*100
    if any(mark < 35 for mark in marks):
        print("You are fail")
    else:
        print(f"{student_name}'s percentage =",percetage_of_marks)
        if average_marks < 50:
            print(f"{student_name}'s grade is D")
        elif average_marks < 60:
            print(f"{student_name}'s grade is C")
        elif average_marks < 70:
            print(f"{student_name}'s grade is B")
        elif average_marks < 80:
            print(f"{student_name}'s grade is A")
        else:
            print(f"{student_name}'s grade is Distinction")
check_grade()

# stone,rock, paper
# print("Enter the object name as stone or paper or scissor")
# first_object = input("Enter a first object:")
# second_object = input("Enter a second object:")
# if first_object == second_object:
#     print('Tie')
# elif first_object == 'stone' and second_object == 'paper':
#     print("paper will win.")
# elif first_object == 'paper' and second_object == 'stone':
#     print("paper will win.")
# elif first_object == 'paper' and second_object == 'scissor':
#     print("scissor will win.")
# elif first_object == 'scissor' and second_object == 'paper':
#     print("scissor will win.")
# elif first_object == 'scissor' and second_object == 'stone':
#     print("stone will win.")
# elif first_object == 'stone' and second_object == 'scissor':
#     print("stone will win.")
# else:print("You have entered invalid input.")













