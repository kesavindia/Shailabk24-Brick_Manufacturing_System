'''
44 Bank Loan Approval:

REQUIREMENT GATHERING:

---------------------------------------
| Enter Credit Score: |_________|    |
| Enter Income:       |_________|    |
| Enter Loan Amount:  |_________|    |
|           Submit                    |
|_____________________________________|

ANALYSIS:

Functional Analysis:
User will provide credit score, income, and loan amount.
Empty values: "Invalid input, please enter all details."

Technical Analysis:
Entity Name: LoanApprovalSystem
State: Data types - INT, FLOAT, Error messages - STRING
Behavior: Operators - IF, ELIF, ELSE

DESIGN (Sequence Diagrams):

Mathematics:
1. Check if credit score, income, and loan amount are provided.
2. Use nested if statements to determine loan approval.
3. Print the result.

Programming Language:
State: Define credit score, income, and loan amount given by the user.

Behavior:
1. Check if credit score, income, and loan amount are provided.
2. Use nested if statements to determine loan approval.
3. Print the result.
'''

print("="*30)
print("Q44 LoanApprovalSystem")

# Program to simulate a bank loan approval system

# Input details
credit_score_input = input("Enter Credit Score: ")
income_input = input("Enter Income: ")
loan_amount_input = input("Enter Loan Amount: ")

# Check if credit score, income, and loan amount are provided
if credit_score_input.isdigit() and income_input.isdigit() and loan_amount_input.isdigit():
    credit_score = int(credit_score_input)
    income = int(income_input)
    loan_amount = int(loan_amount_input)

    # Use nested if statements to determine loan approval
    if credit_score >= 700:
        if income >= 50000 and loan_amount <= 200000:
            print("Loan approved!")
        elif income >= 50000 and loan_amount > 200000:
            print("Further evaluation needed.")
        else:
            print("Loan rejected.")
    else:
        print("Loan rejected.")
else:
    print("Invalid input, please enter all details.")
