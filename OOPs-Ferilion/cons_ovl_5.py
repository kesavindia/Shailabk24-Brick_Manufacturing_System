'''Write a class Date with a constructor that can be
initialized with either day, month, and year or no values
(defaults to the current date).'''
from  datetime import datetime
class Date:
    def __init__(self,day=None,month=None,year=None):
        if day is None or month is None or year is None:
            #If any of the values is not provided,use te current date
            current_date = datetime.now()
            self.day = current_date.day
            self.month = current_date.month
            self.year = current_date.year
        else:
            self.day = day
            self.month = month
            self.year = year
date1 = Date(10,2,2024)
print(f"Date 1: {date1.day}/{date1.month}/{date1.year}")
date2 = Date()
print(f"Date 2: {date2.day}/{date2.month}/{date2.year}")
