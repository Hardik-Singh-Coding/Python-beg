set1 = {"apple", "banana", "cherry"}
print(set1)

set2 = {"army", "navy", "air force", "army"}
print(set2) # does not print duplicate values

set3 = {"voice", "sound", "music", True, 1, 2, 0, False}
print(set3) # (True and 1)  AND (False and 0) are the same in a set


# Accessing values
for i in set1:
    print(i)

# To check the element in the set
print("navy" in set2)


# Addind items
set1.add("plum") # Can only add a single item
print(set1)

# Adding two sets
set4 = {"pineapple", "dragon fruit"}
set1.update(set4)
print(set1)

# Adding another iterable
list1 = [20, 30, 498, 309]
set1.update(list1)
print(set1)


# Removing an item 
set1.remove(20) # Can remove only one item 
print(set1)
set1.discard("pineapple") # Can remove only one item 
print(set1)

# Removing random item
set1.pop()
print(set1)

# Clearing a set
set1.clear()
print(set1)


# Union or | 
newset = {"Hardik", "Rohan", "Aditya", "Kshitij"}
newset2 = {"Vansh", "Krish"}

# result = newset.union(newset2)
result = newset | newset2
print(result)

