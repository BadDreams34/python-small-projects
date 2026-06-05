"""Deep Cave
Program generate an endless animation simulating a cave"""

import time
#defining constants
AREA_LENGTH = 30
CAVE_WIDTH_INDEX = 4
CAVE_FLUCTUATION = 15
PAUSE = 0.05

#initials
i = 0
direction = 'right'
shaking_delay = 3
while True:
    area = list(AREA_LENGTH * "#")
    cave_start = int(AREA_LENGTH * 0.3) + i
    for j in range(CAVE_WIDTH_INDEX):
        area[cave_start+j] = " "
    if shaking_delay == 0:
        shaking_delay = 3
        if direction == 'right':
            i+=1
        elif direction == 'left':
            i-=1
    if cave_start + CAVE_WIDTH_INDEX +1 == AREA_LENGTH: #checks if the cave is on the right edge
        direction = 'left'
    if cave_start == 0: #checks for the left edge
        direction = 'right'
    shaking_delay -= 1

    #prints the current cave position
    print("".join(area))
    time.sleep(PAUSE)


# shacking_compromise