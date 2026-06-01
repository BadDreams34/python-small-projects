"""Carrot in a box
this program assigns two boxes to both the players and only one has carrot in it"""

import random

print("Enter the name of the first player")
p1 = input("> ")
print("Enter the name of the second player")
p2 = input("> ")

print("Both of you are given boxes")


#prints the closed boxes initially
print("------    ------")
print("|    |    |     |")
print("|    |    |     |")
print("|    |    |     |")
print("------    ------")
print("Box A      Box B")

#waits for a player to close their eyes
print("Wait for {} to close their eyes".format(p2))
while True:
    if not input("Press Enter to conitnue") == "":
        continue
    break

#assigns the carrot to a box
carrot_holder = random.choice([p1,p2])

#shows the other player if they have carrot or not
if carrot_holder == p1:

    print("""
------    ------
|  W |    |     |
|  W |    |     |
------    ------
CARROT!        
  p1        p2""")

else:
    print("""
------    ------
|    |    |  W  |
|    |    |  W  |
------    ------
           CARROT!        
  p1        p2""")
