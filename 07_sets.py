# set1 = {"apple", "banana", "cherry"}
# print(set1)

# set2 = {"army", "navy", "air force", "army"}
# print(set2) # does not print duplicate values

# set3 = {"voice", "sound", "music", True, 1, 2, 0, False}
# print(set3) # (True and 1)  AND (False and 0) are the same in a set





# # Accessing values
# for i in set1:
#     print(i)




# # To check the element in the set
# print("navy" in set2)




# # Addind items
# set1.add("plum") # Can only add a single item
# print(set1)




# # Adding two sets
# set4 = {"pineapple", "dragon fruit"}
# set1.update(set4)
# print(set1)




# # Adding another iterable
# list1 = [20, 30, 498, 309]
# set1.update(list1)
# print(set1)





# # Removing an item 
# set1.remove(20) # Can remove only one item 
# print(set1)
# set1.discard("pineapple") # Can remove only one item 
# print(set1)
# set1.pop() # Removes random item
# print(set1)
# set1.clear() # Clears the set
# print(set1)
# del set1 # Deletes the set





# Union or | ( Adds two or more sets to give a new set )
newset = {"Hardik", "Rohan", "Aditya", "Kshitij"}
newset2 = {"Vansh", "Krish", "Rohan", "Aditya"}
# result = newset.union(newset2)
# result = newset | newset2
# print(result)



# # Intersection or & ( Returns the common values of the two sets )
# # result2 = newset.intersection(newset2)
# result2 = newset & newset2
# print(result2)




# # Intersection update or &= ( Changes the original set )
# # newset.intersection_update(newset2)
# # newset &= newset2
# # print(newset)




# # Difference or - ( Returns the LHS set )
# # result3 = newset.difference(newset2)
# result3 = newset - newset2
# print(result3)




# # Difference update or -= ( Changes the original set )
# # newset.difference_update(newset2)
# # newset -= newset2
# # print(newset)




# # Symmetric difference or ^ ( Excludes the common values )
# # result4 = newset.symmetric_difference(newset2)
# result4 = newset ^ newset2
# print(result4)




# Symmetric difference update or ^= ( Changes the original set )
newset.symmetric_difference_update(newset2)
print(newset)
print(newset2)