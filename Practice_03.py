limit = int(input("Enter the limit: "))

sum = 0
iterate = 0

while iterate < limit:
    if iterate%2 == 0:
        print(iterate)
        sum += iterate
    iterate += 1

print(f"The sum is {sum}")