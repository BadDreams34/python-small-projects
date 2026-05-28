import random
import time
import sys

try:
    import bext
except ImportError:
    print("This script requires the bext module\nInstall with: sudo pip install bext")
    sys.exit()

#defining constants
WIDTH, HEIGHT = bext.size()
NUMER_OF_LOGOS = 10
PAUSE = 0.1

colors = ['red','green','yellow','blue','magenta','cyan']
UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'

#dictionary key names
COLOR = 'color'
DIR = 'direction'
X = 'x'
Y = 'y'
directions = [UP_RIGHT,UP_LEFT,DOWN_RIGHT,DOWN_LEFT]


def main():

    #generate some logos
    logos = []
    for i in range(NUMER_OF_LOGOS):
        logos.append({X: random.randint(0, WIDTH - 4),
                      Y: random.randint(0, HEIGHT - 4),
                      DIR: random.choice(directions),
                      COLOR: random.choice(colors)})

    corner_bounces = 0
    while True: #main game loop
        for logo in logos:
            #clears the previous logo
            bext.goto(logo[X], logo[Y])
            print("   ", end="")

            original_direction = logo[DIR]

            #check the corner bounces
            if logo[X] == 0 and logo[Y]==0:
                corner_bounces += 1
                logo[DIR] = DOWN_RIGHT
            if logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                corner_bounces += 1
                logo[DIR] = UP_LEFT
            if logo[X] == WIDTH - 3 and logo[Y] == 0:
                corner_bounces += 1
                logo[DIR] = DOWN_LEFT
            if logo[X] == 0 and logo[Y] == HEIGHT - 1:
                corner_bounces += 1
                logo[DIR] = UP_RIGHT

            #checking of right Edge
            # WIDTH-3 since DVD has three symbols
            if logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            if logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            #checking of left Edge
            if logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            if logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            #checking of top edge
            if logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT
            if logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT

            #checking of bottom edge
            if logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT
            if logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT

            if logo[DIR] != original_direction:
                logo[COLOR] = random.choice(colors)

            #Move the logo
            bext.goto(logo[X], logo[Y])
            if logo[DIR] == UP_RIGHT:
                logo[X] +=2
                logo[Y] -=1
            if logo[DIR] == UP_LEFT:
                logo[X] -=2
                logo[Y] -=1
            if logo[DIR] == DOWN_RIGHT:
                logo[X] +=2
                logo[Y] +=1
            if logo[DIR] == DOWN_LEFT:
                logo[X] -=2
                logo[Y] +=1

            #display the corner bounces
            bext.goto(5,0)
            print("Corner bounces", corner_bounces, end="")

            for logo in logos:
                bext.goto(logo[X], logo[Y])
                bext.fg(logo[COLOR])
                print("DVD", end="")
            bext.goto(0,0) # resets the position of cursor after every logo been drawn

            sys.stdout.flush()
            time.sleep(PAUSE)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)













