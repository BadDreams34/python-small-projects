"""Digital Clock
Displays the current time in ASCII art"""
import os

import countdown_module_art
import sys, time


print("""This program displays the current time in ascii art !""")

try:
    while True: #main game loop
        print("\n"*50)
        hours = time.strftime("%I")
        mins = time.strftime("%M")
        secs = time.strftime("%S")


        formatted_ascii_hours = countdown_module_art.getSevSegStr(hours)
        formatted_ascii_mins = countdown_module_art.getSevSegStr(mins)
        formatted_ascii_secs = countdown_module_art.getSevSegStr(secs)

        top_hour_row, mid_hour_row, bottom_hour_row = formatted_ascii_hours.splitlines()
        top_min_row , mid_min_row, bottom_min_row = formatted_ascii_mins.splitlines()
        top_sec_row, mid_sec_row, bottom_sec_row = formatted_ascii_secs.splitlines()

        print(f"{top_hour_row} {top_min_row} {top_sec_row}",
              f"{mid_hour_row}:{mid_min_row}:{mid_sec_row}",
              f"{bottom_hour_row}:{bottom_min_row}:{bottom_sec_row}", sep='\n')
        print("Press Ctrl + C to exit")

        time.sleep(1)

except KeyboardInterrupt:
    print("Digital Clock")
    sys.exit()
