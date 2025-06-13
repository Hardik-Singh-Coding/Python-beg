from enum import Enum

# class State(Enum):
#     ACTIVE = 1
#     INACTIVE = 0

# print(State.ACTIVE)
# print(State.ACTIVE.value)
# print(list(State))
# print(len(State)) 

class clock(Enum):
    seven = 7
    eight = 8
    nine = 9

def action(time):
    if time == clock.seven:
        return "Wake up"
    elif time == clock.eight:
        return "Go to gym"
    elif time == clock.nine:
        return "Go to college"
    
print(action(clock.seven))