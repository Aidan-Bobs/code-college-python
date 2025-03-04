class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


""" my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit() """



""" class Restaurant:

    def __init__(self, name, cuisine):
        self.name = name.lower().title().strip()
        self.cuisine = cuisine.lower().strip()
    
    def describe_restaurant(self):
        print(f"This restaurant's name is {self.name}, and it serves {self.cuisine} cuisine.")

    def open_restaurant(self):
        print(f"The restaurant {self.name} is open! ")
    


nomu = Restaurant("nomu", "asian fusion")

nomu.describe_restaurant()
nomu.open_restaurant() """


""" class Team:

    def __init__(self, team_name, members=None):
        self.name = team_name
        self.members = members

    def addMember(self, member):
        self.members.append(member)  

    def removeMember(self, member):
        if member in self.members:
            self.members.remove(member)
        else:
            print(f"{member} is not a member of {self.name}")

    def displayInfo(self):
        print(f"Team: {self.name}")

        if self.members:
            print("Members:", ", ".join(self.members))
        else:
            print("There are no members in this team.")

team = Team("Function Junction", ["Aidan", "Mieke", "Cadee", "Sibu", "Asanda"])


team.displayInfo()


team.addMember("Jordan")
team.displayInfo()


team.removeMember("Cadee")
team.displayInfo()


team.removeMember("Alex")
team.displayInfo() """

from random import randint
from random import choice

print(randint(1, 6))

print(choice(("a", "b", "c", "d")))