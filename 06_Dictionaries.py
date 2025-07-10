# Syntax
person = {"name": "Jimmy", "age": 19}




# Adding a key value pair
person["class"] = 8
print(person)




# Updating a dictionary
person.update({"fav_sub": "Geography", "fav_sport": "Basketball"})
print(person)
person.update({"name": "John", "fav_sub": "History"})
print(person.get("fav_sub"))




# Adding then accessing the key value pair
print(person.get("fav_color", "green"))




# Deleting a key value pair
del person['age']




# Deleting key value pairs
person.pop("name")
print(person)
person.popitem()
print(person)
del person["fav_sub"]
print(person)




# Listing keys, key values, and key value pairs
print(person.keys())
print(list(person.keys()))
print(list(person.values()))
print(list(person.items()))




# No of item pairs in dictionary
print(len(person))




# Copying a dictionary
person_copy = person.copy()
print(person_copy)




# Accessing item via key
print(person['name'])




# Changing the value of a key
person["name"] = "John"




# Nested dictionaries 
myfamily = {
    "Mom":{
        "name": "Emily",
        "age": 30
    },

    "Dad": {
        "name": "Coby",
        "age": 37
    },

    "Me": {
        "name": "Tara",
        "age": 10
    },

    "Brother": {
        "name": "Jimmy",
        "age": 12
    }
}





car1 = {"name": "Mustang", "Company": "Ford"}
car2 = {"name": "Viper", "Company": "Dodge"}
car3 = {"name": "Hector", "Company": "MG"}

Dealership = {
    "car_Ford": car1,
    "car_Dodge": car2,
    "car_MG": car3
}

print(Dealership["car_Ford"]["Company"])

for x, value in Dealership.items():
    print(x + ":")
    for y in value:
        print(f"y : {value[y]}")





# dict.fromkeys(x,y) method returns a dictionary with the specified keys (x) and the specified (single) value (y)
x = ('key1', 'key2', 'key3')
y = 20

newdict = dict.fromkeys(x,y)
print(newdict)




# .setdefault(x,y) method returns the value of the key (x), if the key doesn't exist, it is added to the dictionary with the value y
a = newdict.setdefault('key4', '30')
print(a)
print(newdict)