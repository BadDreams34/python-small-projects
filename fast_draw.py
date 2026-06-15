"""Fast Draw
Reaction speed checker"""

import random
import string
import sys
import time

UPPER_CASE = list(string.ascii_uppercase)

print("""Fast draw
Time to test your reflexes and see if you are the fastest
draw in the west
Press Enter whenever you see DRAW within 0.3 seconds to win
If you press enter before DRAW appears, you will lose !""")

print("Press enter to begin", flush=True)
input()

while True:

    print("Here is so high")
    time_random = random.uniform(1,5) # number of seconds in which the time is needed to pause
    time.sleep(time_random)
    print("DRAW", flush=True)
    time_start = time.time()
    input()
    time_end = time.time()
    time_de = time_end - time_start
    if f"{time_de:.2f}" == "0.00":
        print(f"ermm! You lost, you have to press enter after DRAW appears")
    elif time_de < 0.4:
        print(f"You won, your guess time was {time_de:.2f}")
    else:
        print(f"Too Slow! your guess time was {time_de:.2f}")

    # check for keyboard enter for exactly next 0.3 seconds
    print("Press ENTER to play again  ?")
    wish = input()
    if wish == "":
        continue
    else:
        sys.exit()



