""" username = input("what is you username? ")

passions = []

for i in range(2):
    passions.append(input(f"what is your number {i+1} passion?"))

print(f"wecome to python {username}")

for i in range(len(passions)):
    pass_No = i + 1
    pass_index = i
    print(f"your number {pass_No} passion is {passions[pass_index]}") """


""" import random

print("Welcome to Rock, Paper, Scissors!")
choices = ["rock", "paper", "scissors"]

while True:
    player= input("Enter rock, paper, or scissors (or 'quit' to stop the game): ").lower().strip()
    
    if player== 'quit':
        print("Thanks for playing!")
        break

    if player not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer = random.choice(choices)
    print(f"Computer chose {computer}.")

    if player== computer:
        print("It's a tie!")
    elif (player == "rock" and computer== "scissors") or \
         (player== "paper" and computer== "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
        break
    else:
        print("HA HA lol u took a phat L!")
        break
 """
from random import choice

characters = ["Alice", "Bob", "Charlie"]
actions = ["dances", "sings", "jumps"] 
places = ["on a mountain", "in a castle", "unda da sea"]

count = 0
while count < 1:
    character = choice(characters)
    action = choice(actions)
    place = choice(places)
    
    print(f"{character} {action} {place}.") 
    
    count += 1  

empty_list = []


    