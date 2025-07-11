x = int(input("Enter the value of x: "))

match x:
    case 0: print("x is zero")

    case 1: print("x is one")

    case _: print(f"Number is {x}")



day = 4
month = 5
match day:
    case 1|2|3|4|5 if month == 5:
        print("It's a weekday in May")
    case 1|2|3|4|5 if month == 4:
        print("It's a weekday in April")
    case _:
        print("Error")