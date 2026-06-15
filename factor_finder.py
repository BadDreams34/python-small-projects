"""Factor finder
This program finds the factor of a given number """

import sys
import math

print("""This program finds the factors of the given number given Number and prints them""")


while True: #main program loop
    #asks for the user input
    print("Enter the number or Q to quit")
    while True:
        number = input("> ")
        if number.lower() == "q":
            print("Program ended ")
            sys.exit()
        if not number.isdecimal():
            print("Please check your input ( it should be positive integer )")
            continue
        if 0 <= int(number):
            number = int(number)
            break

    factors = []
    for num in range(1,number+1):
        if number % num == 0:
            factors.append(num)

    for i, fact in enumerate(factors):
        if i == len(factors)-1:
            print(fact)
            break
        print(f"{fact}, ", end='')
    print()