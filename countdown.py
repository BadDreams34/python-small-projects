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
    hours = countdown_module_art.getSevSegStr(h, 2)
    mins = countdown_module_art.getSevSegStr(m, 2)
    secs = countdown_module_art.getSevSegStr(s, 2)
    for rows in zip(hours.splitlines(), mins.splitlines(), secs.splitlines()):
        print(" : ".join(rows),flush=True)
    time.sleep(1)

    if s > 0:
        s -= 1
    elif s == 0 and m > 0:
        s = 59
        m -= 1
    elif s == 0 and m == 0 and h> 0:
        h -= 1
        m = 59
        s = 59
    elif s == 0 and m == 0 and h == 0:
        sys.exit()








