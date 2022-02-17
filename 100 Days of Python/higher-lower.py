from bdb import Breakpoint
from game_data import data
from art2 import logo,vs
from os import system
import random
import json

# function to get 2 random choices
def get2Choices(): 
    return random.sample(data, 2)

score = 0
system('cls')

while True:
   
    # Get 2 choices
    choices = get2Choices()

    # Display Higher Lower logo
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")

    # Display first choice Compare A: <name>, a <description>, from <country>
    choiceA = choices[0]
    print(f"Compare A: {choiceA['name']}, a {choiceA['description']}, from {choiceA['country']}")

    # Display vs art
    print(vs)

    # Display second choice
    choiceB = choices[1]
    print(f"Compare B: {choiceB['name']}, a {choiceB['description']}, from {choiceB['country']}")

    response = input("Who has more followers? Type 'A' or 'B': ").upper()

    system('cls')
    if response == 'A' and choiceA['follower_count'] > choiceB['follower_count']:
        score += 1 
    else: 
        #clear screen -> display higher/lower logo
        print(logo)
        print(f"Sorry that's wrong. Final score: {score}")
        break

