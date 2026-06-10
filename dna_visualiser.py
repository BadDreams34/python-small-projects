"""DNA Visualiser
A simple animation of DNA double helix"""

import random
import time
import sys

print("DNA Visualiser")
time.sleep(2)

#set up the constants
TIME_PAUSE = 0.09 # waiting time in the animation to continue further printing

BASES = ["G", "C", "A", "T"]

#structure of the dna
STRUCTURE = [
'         ##',
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##',
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#'
]

try:
    while True: #main animation loop
        for i in range(len(STRUCTURE)):
            if i == 0 or i == 9:
                print(STRUCTURE[i])
            else:
                base_1 = random.choice(BASES)
                if base_1 == "G":
                    base_2 = "C"
                elif base_1 == "C":
                    base_2 = "G"
                elif base_1 == "A":
                    base_2 = "T"
                elif base_1 == "T":
                    base_2 = "A"
                print(STRUCTURE[i].format(base_1,base_2))
            time.sleep(TIME_PAUSE)
except KeyboardInterrupt:
    print("DNA Visualiser")
    sys.exit()