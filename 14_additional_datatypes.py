# range creates an iterable object
# Does not store the values, generates them on demand
x = range(6) 
for i in x:
    print(i)



# memoryview prints the memory allocated to the variable 
y = memoryview(bytes(5))
print(y)