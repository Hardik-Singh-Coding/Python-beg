ingridients = True
meal_cooked = False

result1 = all([ingridients, meal_cooked])
print(result1)
result2 = any([ingridients, meal_cooked])
print(result2)


# Any empty string is considered False 
# Any variable with value 0 is False 