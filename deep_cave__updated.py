"""Deep Cave
Program generate an endless animation simulating a cave"""

import random, sys, time

#Set up the constants
WIDTH = 50
PAUSE_AMOUNT = 0.05


print("Deep Cave")
print("Press Control + C to stop")
time.sleep(2)


left_width = 20
cave_len = 10

while True:
    right_width = WIDTH - left_width - cave_len
    print("#"* left_width + cave_len * " " + "#" * right_width)

    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt: #checks for keyboard interrupt
        print("Program Ended")
        sys.exit()

    #Adjust the left Width
    dice_roll = random.randint(1,6)
    if dice_roll == 1 and left_width > 1:
        left_width -=1 #decreases the left width
    elif dice_roll == 2 and left_width < WIDTH - 1:
        left_width +=1
    else:
        pass

    #Adjust the cave_len
    dice_roll = random.randint(1,6)
    if dice_roll == 1 and cave_len > 1:
        cave_len -= 1
    elif dice_roll == 2 and left_width + cave_len < WIDTH - 1:
        cave_len += 1
    else:
        pass

