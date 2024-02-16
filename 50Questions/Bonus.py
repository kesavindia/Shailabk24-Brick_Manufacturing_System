''' A company decided to give a bonus of 5% to an employee if his/her year of service is more than 5 years.
Ask the user for their salary and years of service and print the net bonus amount.
'''

'''
REQUIREMENT GATHERING:

-------------------------------------------
| Enter Salary: |__________|              |
| Enter Years of Service: |______|         |
|           Submit                        |
|__________________________________________|

ANALYSIS:

Functional Analysis:
User will provide salary and years of service.
Empty values: "Invalid input, please enter both salary and years of service."
Non-numeric values: "Invalid input, please enter numeric values."

Technical Analysis:
Entity Name: BonusCalculator
State: Data types - FLOAT, INT, Error messages - STRING
Behavior: Operators - IF, ELSE

DESIGN (Sequence Diagrams):

Mathematics:
1. Check if both salary and years of service are provided and numeric.
2. Determine the bonus amount based on the provided years of service.
3. Print the result.

Programming Language:
State: Define salary and years of service given by the user.

Behavior:
1. Check if both salary and years of service are provided and numeric.
2. Determine the bonus amount based on the provided years of service.
3. Print the result.
'''


print("Q17 BonusCalculator")

salary_input = input("Enter Salary: ")
service_input = input("Enter Years of Service: ")

if salary_input.isdigit() and service_input.isdigit():
    salary = float(salary_input)
    service_years = int(service_input)

    if salary > 0 and service_years >= 0:
        if service_years > 5:
            bonus = 0.05 * salary
            print(f"Net Bonus Amount: ${bonus:.2f}")
        else:
            print("No bonus for less than 5 years of service.")
    else:
        print("Invalid input, please enter valid salary and years of service.")
else:
    print("Invalid input, please enter numeric values.")