'''Countdown Timer
This program displays a countdown timer based on given hours, minutes and seconds.'''

import countdown_module_art, time, os,sys

print("This program displays a countdown timer based on given hours, minutes and seconds.")

#takes hours, minutes and seconds from user
print("Please enter the number of hours")
while True:
    h = input("> ")
    if not h.isdecimal():
        print("Please verify your input(0-99)")
        continue
    if 0 <= int(h) <= 99:
        h = int(h)
        break

print("Please enter the number of minutes")
while True:
    m = input("> ")
    if not m.isdecimal():
        print("Please verify your input (0-59)")
        continue
    if 0<= int(m) < 60:
        m = int(m)
        break

print("Please enter the number of seconds")
while True:
    s = input("> ")
    if not s.isdecimal():
        print("Please verify your input (0-59)")
        continue
    if 0 <= int(s) < 60:
        s = int(s)
        break


total_time = h * 3600 + m * 60 + s


while True:
    os.system("cls")
    hr = total_time // 3600
    min = (total_time % 3600) // 60
    sec = total_time % 60

    hours = countdown_module_art.getSevSegStr(hr, 2)
    mins = countdown_module_art.getSevSegStr(min, 2)
    secs = countdown_module_art.getSevSegStr(sec, 2)

    top_hours , mid_hours , bottom_hours = hours.splitlines()
    top_min_row, mid_min_row, bottom_min_row = mins.splitlines()
    top_sec_row, mid_sec_row, bottom_sec_row = secs.splitlines()

    #prints the clock in the terminal
    print(f"{top_hours}  {top_min_row}  {top_sec_row}")
    print(f"{mid_hours}* {mid_min_row}* {mid_sec_row}")
    print(f"{bottom_hours}* {bottom_min_row}* {bottom_sec_row}")
    time.sleep(1)
    total_time -=1
