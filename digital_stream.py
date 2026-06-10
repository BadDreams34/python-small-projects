"""Digital Stream
This program stimulates the generation of random Stream of binary from the screen to go down below"""

import random
import shutil
import time
import sys

WIDTH = shutil.get_terminal_size()[0] - 1 #to accomodate for the windows automatically printing into a new line
STREAM_CHAR = ['0','1']
PAUSE = 0.1
DENSITY = 0.02
MIN_STRING_LENGTH = 60
MAX_STRING_LENGTH = 140


print("""Digital Stream
This program generates the random stream of binaries as text moves down""")
print("Press Ctrol + C to exit")
time.sleep(2)
try:
    columns = [0] * WIDTH
    while True: #main game loop
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    columns[i] = random.randint(MIN_STRING_LENGTH, MAX_STRING_LENGTH)

            #displays the character on the column
            if columns[i] > 0:
                print(random.choice(STREAM_CHAR), end='')
                columns[i] -=1
            else:
                print(" ", end='')
        print() #prints a newline at the end of the row of columns
        sys.stdout.flush()
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()

