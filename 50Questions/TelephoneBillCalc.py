'''11 Write a program to calculate the monthly telephone bills as per the following rule:

Minimum Rs. 200 for up to 100 calls.

Plus Rs. 0.60 per call for next 50 calls.

Plus Rs. 0.50 per call for next 50 calls.

Plus Rs. 0.40 per call for any call beyond 200 calls. '''

def monthlyBill(calls):
    billAmount = 200
    if 100 < calls <= 150:
        billAmount += (.60*(calls-100))
    elif 150 < calls <= 200:
        billAmount += (0.60*50 + 0.50 * (calls - 150))
    elif calls>200:
        billAmount += .60*50 + 0.50 * 50 + .40 * (calls-200)
    return billAmount
calls = int(input("Enter your no. of calls to know your bill amount: "))
bill = monthlyBill(calls)
print(f"Your bill amount for {calls} calls =Rs.{bill:.2f}")
