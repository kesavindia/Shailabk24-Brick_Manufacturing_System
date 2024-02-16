'''
45 Flight Booking System:

REQUIREMENT GATHERING:

---------------------------------------
| Enter Passenger Age: |_________|    |
| Enter Class Preference: |______|    |
|           Submit                    |
|_____________________________________|

ANALYSIS:

Functional Analysis:
User will provide passenger age and class preference.
Empty values: "Invalid input, please enter all details."

Technical Analysis:
Entity Name: FlightBookingSystem
State: Data types - INT, STRING, Error messages - STRING
Behavior: Operators - IF, ELIF, ELSE

DESIGN (Sequence Diagrams):

Mathematics:
1. Check if passenger age and class preference are provided.
2. Use nested if statements to determine booking success and calculate ticket price.
3. Print the result.

Programming Language:
State: Define passenger age and class preference given by the user.

Behavior:
1. Check if passenger age and class preference are provided.
2. Use nested if statements to determine booking success and calculate ticket price.
3. Print the result.
'''


print("Q45 FlightBookingSystem")


passenger_age_input = input("Enter Passenger Age: ")
class_preference_input = input("Enter Class Preference(economy/business): ")

if passenger_age_input.isdigit() and class_preference_input.lower() in ["economy", "business"]:
    passenger_age = int(passenger_age_input)
    class_preference = class_preference_input.lower()
    if 18 <= passenger_age <= 60:
        if class_preference == "economy":
            print("Booking successful! Ticket price: $500")
        elif class_preference == "business":
            print("Booking successful! Ticket price: $1000")
    elif 60 < passenger_age <= 80:
        if class_preference == "economy":
            print("Booking successful! Ticket price: $300")
        elif class_preference == "business":
            print("Booking successful! Ticket price: $700")
    else:
        print("Booking not available for passengers above 80 years.")
else:
    print("Invalid input, please enter all details.")
