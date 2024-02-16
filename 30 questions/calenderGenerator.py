import calendar

def generate_calendar(year, month):
    # Get the calendar for the specified year and month
    cal = calendar.monthcalendar(year, month)

    # Define the days of the week
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    # Print the header
    print(f"Calendar for {calendar.month_name[month]} {year}")
    print(" ".join(days_of_week))

    # Print the calendar
    for week in cal:
        for day in week:
            if day == 0:
                print("    ", end=" ")  # Print empty space for days outside the month
            else:
                print(f"{day:2d} ", end=" " if day < 10 else " ")  # Adjust spacing for single-digit and double-digit days
        print()  # Move to the next line after printing a week

# Get user input for the year and month
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

# Call the function to generate and print the calendar
generate_calendar(year, month)
