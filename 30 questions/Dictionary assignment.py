# students = [
#     {'name': 'Kesavan', 'age': 41, 'grades': {'math': 90, 'science': 85, 'history': 92},
#      'clubs': ['Chess Club', 'Coding Club']},
#     {'name': 'Basava', 'age': 29, 'grades': {'math': 85, 'science': 88, 'history': 95}, 'clubs': ['Chess Club']},
#     # Add more student information as needed
# ]
# grades = students[0]['grades']
# print(grades)
def calculate_average_grade(student_info):#dict
    grades = student_info['grades']# grades is a  dict
    average_grade = sum(grades.values()) / len(grades)
    return average_grade

def average_grades_list(students):# list of dictionaries
    average_grades = []
    for student_info in students:
        name = student_info['name']
        average_grade = calculate_average_grade(student_info)
        average_grades.append({'name': name, 'average_grade': average_grade})
    return average_grades

def unique_club_names(students):
    all_clubs = set()
    for student_info in students:
        all_clubs.update(student_info['clubs'])
    return all_clubs

def coding_club_members(students):
    coding_club_members_set = set()
    for student_info in students:
        if 'Coding Club' in student_info['clubs']:
            coding_club_members_set.add(student_info['name'])
    return coding_club_members_set

def age_grouping(students):
    age_groups_dict = {}
    for student_info in students:
        age = student_info['age']
        age_group = f"{(age // 3) * 3 + 1}-{(age // 3) * 3 + 3}"
        if age_group not in age_groups_dict:
            age_groups_dict[age_group] = []
        age_groups_dict[age_group].append(student_info['name'])
    return age_groups_dict

# Example usage:
students = [
{'name': 'kesavan', 'age': 41, 'grades': {'math': 90, 'science': 85, 'history': 92}, 'clubs': ['Chess Club', 'Coding Club']},
{'name': 'basava', 'age': 30, 'grades': {'math': 85, 'science': 88, 'history': 95}, 'clubs': ['Chess Club']},
{'name': 'arya', 'age': 38, 'grades': {'math': 90, 'science': 85, 'history': 92}, 'clubs': ['Chess Club', 'Coding Club']},
{'name': 'Shaila', 'age': 26, 'grades': {'math': 90, 'science': 85, 'history': 92}, 'clubs': ['Chess Club', 'Coding Club']},
{'name': 'Akshay', 'age': 25, 'grades': {'math': 90, 'science': 85, 'history': 92}, 'clubs': ['Chess Club', 'Coding Club']},
{'name': 'Nithish', 'age': 24, 'grades': {'math': 90, 'science': 85, 'history': 92}, 'clubs': ['Chess Club', 'Coding Club']},
{'name': 'Veena', 'age': 26, 'grades': {'math': 90, 'science': 85, 'history': 92}, 'clubs': ['Chess Club', 'Coding Club']},
    # Add more student information as needed
]
print(len(students[0]))
average_grades = average_grades_list(students)
print("Average Grades:")
for student in average_grades:
    print(f"{student['name']}: {student['average_grade']:.2f}")

unique_clubs = unique_club_names(students)
print("Unique Club Names:", unique_clubs)

coding_club_members_set = coding_club_members(students)
print("Coding Club Members:", coding_club_members_set)

age_groups = age_grouping(students)
print("Age Grouping:", age_groups)

