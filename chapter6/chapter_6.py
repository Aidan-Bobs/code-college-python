my_Person = {
    "name" : "Aidan",
    "Age" : 20,
    "language" : "English"
}
my_Person["gender"] = "male"

print(my_Person)

my_Person["Age"] = 21

my_name=my_Person.pop("name")
print(my_name)
#making a dict with names for keys and programming langs for values
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'Javascript',
 }

#making a for loop that itterates ofver the values of 
#the favorite_languages dict using the .value() dict method
for name in favorite_languages.values():
    #every value will be checked to see if it says js, and when it is it will print forbidden
    if name == "Javascript":
        print("Forbidden...")
    #else it will print the name and noice
    else:
        print(f"{name}, noice")


dad ={
    "name" : "pete",
    "age" : 61
}

mom = {
    "name" : "Lee",
    "age" : 61
}

Bro = {
    "name" : "Jords",
    "age" : 29
}

family = [dad, mom, Bro]

for member in family:
    for key, value in member.items():
        print(f"{key}: {value}")
    print()



