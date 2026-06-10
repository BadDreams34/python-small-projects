"""Dice Roller
Stimulates dice rolls using Dungeons and Dragons dice roll notation."""

import random, sys

print("""Dice Roller
Enter what kind and how many dice to roll, 
Format of the input should be starting from the integer which denotes the number of dices
Followed by 'd' alphabet which is followed by an integer which denotes the number of faces of each dice 
Which is followed by an optional addition or substraction.""")

while True: #main game loop
    try:
        dice_str = input("> ") # the prompt to enter the dice string.
        if dice_str.upper() == "QUIT":
            print("Thanks for playing")
            sys.exit()

        dice_str = dice_str.lower().replace(" ", "") # refine the string

        #checks for the 'd'
        d_ind = dice_str.find('d')
        if d_ind == -1:
            raise Exception("Missing d in the string")

        #checks for the number of dices
        num_dice = dice_str[:d_ind]
        if not num_dice.isdecimal():
            raise Exception("Missing the number of dice.")
        num_dice = int(num_dice)

        #checks for a '+' or a '-'
        mod_ind = dice_str.find("+")
        if mod_ind == -1:
            mod_ind = dice_str.find("-")

        #find the number of sides
        if mod_ind == -1:
            num_side = dice_str[d_ind + 1 : ]
        else:
            num_side = dice_str[d_ind + 1: mod_ind]
        if not num_side.isdecimal():
            raise Exception("Missing the number of sides")
        num_side = int(num_side)

        #find the modifier value
        if mod_ind == -1:
            modifier_val = 0
        else:
            modifier_val = int(dice_str[mod_ind + 1 : ])
            if dice_str[mod_ind] == '-':
                modifier_val = -modifier_val

        #stimulates the dice rolls
        rolls = []
        for i in range(num_dice):
            roll_result = random.randint(1, num_side)
            rolls.append(roll_result)


        #prints the result
        print("Total: ", sum(rolls) + modifier_val, "Each die: (", end= '')

        #display individual rolls
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(", ".join(rolls), end='')

        # Display the modifier amount
        if modifier_val != 0:
            mod_sign = dice_str[mod_ind]
            print(", {}{}".format(mod_sign,abs(modifier_val)), end='')
        print(')')

    except Exception as exc:
        #catch any exception and display the message to the user
        print("Invalid input. Enter something like 3d0 ")
        print("Input was Invalid because:", str(exc))
        continue # go back to the dice string prompt







