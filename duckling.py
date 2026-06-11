'''Duckling Screensaver
A screensaver of many ducklings with a minor difference in between each'''

import random

# [PC] this program generates ducklings by slight variations but there should be a general format of all the ducklings
# using random firstly assign the ducks which are to be printed
# then determine the location where each duckling is to be printed
# then just display a canvas NO THIS IS NOT HOW I AM GONNA THINK ABOUT IT LOL

# you have a canvas with given width and height in which you will generate ducklings randomly which will be shown on this canvas and
# the ducklings can be of various types that should be managed and gneerated with slight variation in the symbols of a constant dictionary
# it must have a time pause which will decide the amount to delay between the next item
# ducklings size will determine the maximum ducklings it can fit on the canvas
# there should be a dictionary which holds the speicified duckling on the given x,y position so
# specified_duckling how will that be stored ?
# in a while loop it should be of per line like per row decide how many and which type of ducklings will be tehre
# select random positions and same number of random ducklings and assign them both in a seperate dictionary

# duckling generation

# setting up the constants
CANVAS_WIDTH = 100
CANVAS_HEIGHT = 80
DUCKLING_WIDTH = 5
DUCKLING_HEIGHT = 3
EYES = [r'"', r"``", r"''",r"^^"]
SIZE = {1: ' ^ ^', 2: ' ^^ '}
WINGS = ["v","^",">"]
MAX_DUCKLINGS = CANVAS_WIDTH // DUCKLING_WIDTH

#duckling generator
def duckling_gen():
    duckling = []
    eye = random.choice(EYES)
    alignment = random.choice(["L","R"])
    size = random.choice([1,2])
    wing = random.choice(WINGS)
    if alignment == "L":
        if size == 1:
            duckling.append(f"{random.choice([">","="])}{eye.ljust(2)})")
            duckling.append(f"(  {wing})")
            duckling.append(SIZE.get(1))
        else:
            duckling.append(f"{random.choice([">", "="])}\")")
            duckling.append(f"( {wing})")
            duckling.append(SIZE.get(2))
    else:
        if size == 1:
            duckling.append(f"({eye.rjust(2)}{random.choice(["<", "="])}")
            duckling.append(f"({wing}  )")
            duckling.append(SIZE.get(1))
        else:
            duckling.append(f"(\"{random.choice(["<", "="])}")
            duckling.append(f"({wing} )")
            duckling.append(SIZE.get(2))
    return duckling




print('''Duckling Screensaver
Press Ctrl+C to quit''')

def main(): #main function
    while True: #for each row
        #decide the position of generation on canvas
        num_duck = random.randint(0, MAX_DUCKLINGS) # number of ducklings in the given row
        # for each duck in the given row
        pos_duck = [] #stores tuples of x and y positions of the ducklings
        for i in range(num_duck):
            pos_x = random.randint(0, CANVAS_WIDTH - DUCKLING_WIDTH)
            pos_y = random.randint(0, CANVAS_HEIGHT - DUCKLING_HEIGHT)
            top_right_x = pos_x + DUCKLING_WIDTH
            top_right_y = pos_y
            bottom_right_x = pos_x + DUCKLING_WIDTH
            bottom_right_y = pos_y + DUCKLING_HEIGHT
            bottom_left_x = pos_x
            bottom_left_y = pos_y + DUCKLING_HEIGHT


            #check for overlaps
            overlap_flag = False
            for (prev_x, prev_y) in pos_duck:
                prev_right = prev_x + DUCKLING_WIDTH
                prev_bottom = prev_y + DUCKLING_HEIGHT
                for x, y in ((pos_x,pos_y),(top_right_x,top_right_y),(bottom_right_x,bottom_right_y),(bottom_left_x,bottom_left_y)):
                    if prev_x <= x <= prev_right and prev_y <= y <= prev_bottom:
                        overlap_flag = True
                        break
            if not overlap_flag:
                pos_duck.append((pos_x, pos_y))







