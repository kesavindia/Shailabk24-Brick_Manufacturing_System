'''write about control statements with examples and diff. between break, continue and pass'''

'''Control statements allow us to manipulate the flow of execution of our program, making it more 
flexible and dynamic. '''
#Example for control statements:
age = 25
if age >= 18:
    print("You are eligible to vote.")
elif age >= 60:
    print("You are a senior citizen and eligible to vote.")
else:
    print("You are not eligible to vote.")


for num in range(10):
    if num == 5:
        break  # Exits the loop when num reaches 5
    print(num)

for num in range(10):
    if num % 2 == 0:
        continue  # Skips even numbers
    print(num)

if age >= 18:
    # proogram to grant access
    pass  # Placeholder for future implementation
else:
    print("Access denied.")
