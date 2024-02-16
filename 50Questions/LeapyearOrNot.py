'''Write a program to determine whether the year is a leap year or not.'''
year = int(input("Enter any year to check:"))
if (year %4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"Year {year} is leap year.")
else:
    print(f"The given year {year} is not a leap year.")