'''
46 Medical Diagnosis:

REQUIREMENT GATHERING:

---------------------------------------
| Enter Symptoms: |________________|  |
|           Submit                    |
|_____________________________________|

ANALYSIS:

Functional Analysis:
User will provide symptoms.
Empty values: "Invalid input, please enter symptoms."

Technical Analysis:
Entity Name: MedicalDiagnosisSystem
State: Data types - STRING, Error messages - STRING
Behavior: Operators - IF, ELIF, ELSE

DESIGN (Sequence Diagrams):

Mathematics:
1. Check if symptoms are provided.
2. Use nested if statements to suggest possible illnesses or conditions.
3. Print the result.

Programming Language:
State: Define symptoms given by the user.

Behavior:
1. Check if symptoms are provided.
2. Use nested if statements to suggest possible illnesses or conditions.
3. Print the result.

'''

print("Q46 MedicalDiagnosisSystem")

# Program for a medical diagnosis system

# Input symptoms
symptoms_input = input("Enter Symptoms: ")

# Check if symptoms are provided
if symptoms_input:
    symptoms = symptoms_input.lower()
    # Use nested if statements to suggest possible illnesses or conditions
    if "fever" in symptoms:
        print("Possible illnesses: Flu, Cold")
    elif "cough" in symptoms:
        print("Possible illnesses: Respiratory infection, Allergies")
    elif "headache" in symptoms:
        print("Possible illnesses: Migraine, Tension headache")
    else:
        print("No specific diagnosis based on provided symptoms.")
else:
    print("Invalid input, please enter symptoms.")

