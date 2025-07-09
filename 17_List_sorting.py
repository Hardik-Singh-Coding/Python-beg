list1 = ["Agra", "Hyderabad", "Mumbai", "Banglore", "Chennai"]
list1.sort()
print(list1)

list2 = [100, 90, 78, 23, 2, 67]
list2.sort()
print(list2)

list2.sort(reverse = True)
print(list2)


# Customized sort function
def myfunc(n):
    return abs(n - 50)
    
list2.sort(key = myfunc)
print(list2)


# To reverse the current order of the list
list2.reverse()
print(list2)