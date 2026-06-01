"""Carrot in a box
A very simple and fun game to play"""

import random



print("""
Carrot in a box!
This program is a fun game in which two persons are given two boxes out of which one of the
box contains a carrot.One of the player is being shown if they have carrot or not. Then the 
player tells the second player whether they have carrot or not. Then second player decides 
if they want to swap the boxes.
""")

input("Press Enter to begin") #Let the player read the rules

#Player names
p1_name = input("Human Player 1, Enter your name\n> ")
p2_name = input("Human Player 2, Enter your name\n> ")
player_names = p1_name[:11].center(11) + "    " + p2_name[:11].center(11)


print("""HERE ARE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
""")

#game instructions
print()
print(player_names)
print()
print(p1_name + ', you have a RED box in front of you.')
print(p2_name + ', you have a GOLD box in front of you.')
print()
print(p1_name + ', you will get to look into your box.')
print(p2_name.upper() + ',close your eyes don\'t look')
input('When {} has closed there eyes, press Enter'.format(p2_name))
print()

carrot_in_first_box = random.choice([True, False])

if carrot_in_first_box:
    print('''
   ___VV____
  |   VV    |
  |   VV    |
  |___||____|    __________
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
 (carrot!)''')
    print(player_names)
else:
    print('''
   _________
  |         |
  |         |
  |_________|    __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
(no carrot!)''')


print("\n"* 100) #clears the screen after printing the opened box for the first player to see
print("Player" + p1_name + "tells" + p2_name + "to open their eyes")
input("Press enter to continue...")

print()
print("Player" + p1_name + "tells the other player either of the following")
print("""
1. My box didnt have carrot
2. My box have a carrot
""")

input("Press enter to continue")
print()
print("Player" + p2_name + ",Do you want to swap the boxes with" + p1_name + "or not?(YES/NO)")

while True:
    response = input("> ")
    if not response.startswith("Y") or response.startswith("N"):
        print(p2_name + "Please enter Either YES or NO")
        continue
    break


first_box = "RED "
second_box = "GOLD"

if response.startswith("Y"):
    carrot_in_first_box = not carrot_in_first_box
    first_box, second_box = second_box, first_box #swaps the boxes


print('''HERE ARE THE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   {}  | |  |   {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(first_box, second_box))

print(player_names)

input("Press Enter to reveal the winner")
print()

if carrot_in_first_box:
    print('''
   ___VV____      _________
  |   VV    |    |         |
  |   VV    |    |         |
  |___||____|    |_________|
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|   {}  | |  |   {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(first_box, second_box))

else:
    print('''
   _________      ___VV____
  |         |    |   VV    |
  |         |    |   VV    |
  |_________|    |___||____|
 /         /|   /    ||   /|
+---------+ |  +---------+ |
|   {}  | |  |   {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(first_box, second_box))

print(player_names)

#decide the winner
if carrot_in_first_box:
    print(p1_name + "is the winner")
else:
    print(p2_name + "is the winner")




