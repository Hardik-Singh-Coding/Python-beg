# Arbitrary Arguments
def my_function(*kids): # Arguments passed as a tuple
    print("Eldest kid: " + kids[1])

my_function("Emily", "Catherine", "Lily")





# Keyword Arguments
def my_func1(kid1, kid2, kid3):
    print("Youngest kid: " + kid3)

my_func1(kid1 = "Emily", kid2 = "Catherine", kid3 = "Lily")




# Arbitrary keyword arguments
def details(**kid):
    print(f"The last name of Will is", kid["lname"])

details(fname = "Will", lname = "Smith")





# Default arguments
def my_country(country = "Germany"):
    print("My favourite country is", country)

my_country("India")
my_country()





# Positional-only arguments
def my_func2(x, /):
    print(x)

my_func2(3)




# Keyword-only arguments:
def my_func3(*, x):
    print(x)

my_func3(x=10)




# Combine Keyword-only and Positional-only arguments:
def my_func4(a,b,c,/,*,d,e):
    print(a+b+c+d+e)

my_func4(1,2,3,d=4,e=5)