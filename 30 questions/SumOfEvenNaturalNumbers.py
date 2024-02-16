# Write a program to display the sum of n terms of even natural numbers

# Get user input for the number of terms (n)
n = int(input("Enter the number of terms: "))

# # Calculate the sum of the first n even natural numbers
# sum_of_even_numbers = n * (n + 1)
# sum_of_odd_numbers = n**2
# sum_of_n_natural_numbers = n*(n+1)//2
#
# # Display the result
# print(f"The sum of the first {n} even natural numbers is: {sum_of_even_numbers}")
# print(f"The sum of the first {n} odd natural numbers is: {sum_of_odd_numbers}")
# print(f"The sum of the first {n} natural numbers is: {sum_of_n_natural_numbers}")
i=1
evensum = 0
while i<=n:
    evensum += 2*i
    i += 1
print(f"The sum of the first {n} even natural numbers is: {evensum}")
odd_sum = 0
#odd sum
for i in range(1,2*n+1,2):
    odd_sum += i
print(odd_sum)