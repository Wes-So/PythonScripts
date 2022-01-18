print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your meission is to find the treasure")
cross_road = input("You've hit a crossroad, which direction would you like to go? Left or Right? ")

if cross_road.lower() == "left" :
    swim_or_wait = input("You've reached the river but the water is too high, you can wait until the water subsides in the afternoon. Would you swim or wait? ")
else:
    print("Fall into a hole. Game Over")
    quit()


if swim_or_wait.lower() == "wait":
    open_door = input("After crossing the river, there are three doors. Which one will you open, red or blue or yellow? ")
else:
    print("Attacked by trout. Game over")
    quit()

open_door = open_door.lower()

if open_door == "red":
    print("Burned by fire. Game over.")
elif open_door == "blue":
    print("Eaten by beasts. Game over.")
elif open_door == "yellow":
    print("You win!!!")
else:
    print("Game over!!!")