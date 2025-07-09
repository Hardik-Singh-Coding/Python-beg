from enum import Enum

class Days(Enum):
    Day_1 = "Monday"
    Day_2 = "Tuesday"
    Day_3 = "Wednesday"
    Day_4 = "Thursday"
    Day_5 = "Friday"
    Day_6 = "Saturday"
    Day_7 = "Sunday"

weekends = [Days.Day_6, Days.Day_7]

def show():
    for day in Days:
        if day in weekends:
            print(f"{day.value} is a weekend")
        else:
            print(f"{day.value} is a week day")
    
show()