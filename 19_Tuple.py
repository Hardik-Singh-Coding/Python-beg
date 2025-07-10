tuple1 = ("apple", "banana", "cherry") # Packing a tuple
print(tuple1)


tuple2 = (20,)
print(type(tuple2))


# Adding two tuples
tuple1 += tuple2
print(tuple1)


# Deleting a tuple
del tuple2


# Remove an item from a tuple
duptuple = list(tuple1)
duptuple.remove("banana") # removes banana
duptuple.pop(2) # pops 20 
tuple1 = tuple(duptuple)
print(tuple1)


# Unpacking a tuple
newtuple = ("E1", "AFI Building", "Bombay Hospital", 400020)
(HouseNo, Building, LandMark, Pincode) = newtuple
print(HouseNo, Building)
print(LandMark)
print(Pincode)

newtuple2 = ("flower", "branch", "stem", "root")
(*shootSystem, root) = newtuple2 # shootSystem stored as a list
print(shootSystem)
print(root)


# Tuple methods
newtuple3 = ("car", "bike", "train", "airplane", "bike")
print(newtuple3.count("bike"))

print(newtuple3.index("bike"))