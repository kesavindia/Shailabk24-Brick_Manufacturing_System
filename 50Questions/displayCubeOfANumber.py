# Write a program to display the cube of the given number up to an integer.
input1 = int(input("Enter a number: "))
print("Cubes of numbers upto ",input1,":")
for i in range(1,input1+1):
    cube = i**3
    print(f"cube of {i} is {cube}")