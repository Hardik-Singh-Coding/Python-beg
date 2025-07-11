# Built-in data type
# Two ways of creating a list:- 
# 1
list_1 = ["apple", "banana", "orange", "plum"]
# print(list_1)

# 2
list_2 = list(("Mom", "Dad", "Brother", "Sister", 20, True))
# print(list_2)



# A list can be multi dimensional:
list_3 = [
    [0,1,1,1], 
    [1,0,1,0],
    [1,1,0,0],
    [1,0,0,0]
    ]
# for row in list_3:
#     print(row) 
# Above is a 2-D list ( equivalent to a 2-D array )



# Accessing list elements 
print(list_1[0])
print(list_2[-3])
print(list_2[1:4]) # Excludes last index
print(list_1[:3]) 
print(list_1[1:])



# Check for item in list
if "Brother" in list_1:
    print("Item present")
else:
    print("Item not present")



# To change an item in the list
list_1[1] = "cherry"
print(list_1)
list_2[0:2] = ["blackcurrant", "muskmelon"]
print(list_2)
list_2[0:2] = ["blackcurrant", "muskmelon", "Cousin"]
print(list_2)



# To append an item in the list
list_1.append("watermelon")
list_1.insert(1, "cherry")
list_1.extend(list_2) 
print(list_1)



# Removing items
list_1.remove("apple")
print(list_1)
list_1.pop(1)
print(list_1)
list_1.pop()
print(list_1)
del list_1[0]
print(list_1)

list_3.clear()
print(list_3)



# Deleting a list
del list_2
# print(list_2)