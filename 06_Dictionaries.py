# Syntax
person = {"name": "Jimmy", "age": 19}


# Adding a key value pair
person["class"] = 8
print(person)


# # Updating a dictionary
person.update({"fav_sub": "Geography", "fav_sport": "Basketball"})
print(person)
person.update({"name": "John", "fav_sub": "History"})
print(person.get("fav_sub"))


# Adding then accessing the key value pair
print(person.get("fav_color", "green"))


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


# Deleting a key pair
del person['age']


# Accessing item via key
print(person['name'])


# Changing the value of a key
person["name"] = "John"