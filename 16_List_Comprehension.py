# list1 = ["summer", "winter", "autumn", "spring", "monsoon"]
# [print(i) for i in list1]
# [print(j) for j in range(len(list1))]


list2 = ["apple", "banana", "pineapple", "grape", "cherry", "plum"]
fruits = [i for i in list2 if "a" in i]
print(fruits)
fruits2 = [fruit.upper() for fruit in list2 if "apple" not in fruit]
print(fruits2)