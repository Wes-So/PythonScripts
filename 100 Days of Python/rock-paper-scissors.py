import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ascii_list = [rock, paper, scissors] 
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_choice > 2:
    print("You typed an invalid number and you lose")
    quit()

print(ascii_list[player_choice])


print("Computer chose:")
cpu_choice = random.randint(0,2) 
print(cpu_choice)
print(ascii_list[cpu_choice])

if player_choice == 0: 
    if cpu_choice == 1:
        print("You lose")
    elif cpu_choice == 2:
        print("You win")
elif player_choice == 1:
    if cpu_choice == 0:
        print("You win")
    elif cpu_choice == 2:
        print("You lose")
elif player_choice == 2:
    if cpu_choice == 0:
        print("You lose")
    elif cpu_choice == 1:
        print("You win")
elif player_choice == cpu_choice:
    print("Draw")
 
    