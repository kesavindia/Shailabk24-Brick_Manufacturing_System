'''Write a class Time with a constructor that can be initialized
 with either hours and minutes or just hours (minutes default to 0).'''

class Time:
    def __init__(self,hours,minutes=0):
        self.hours = hours
        self.minutes = minutes
time1 = Time(2,30)
time2 = Time(2)

print(f"Time is {time1.hours}:{time1.minutes}")
print(f"Time is {time2.hours}:{time2.minutes:02d}")
