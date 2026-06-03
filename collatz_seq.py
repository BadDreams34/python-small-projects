"""Collatz Sequence
3n+1 problem """

import time
import sys
print("Collatz sequence is a sequence of numbers in which \n"
      "The next number is n/2 if n = even \n"
      "The next number is n * 3 + 1 if n = odd \n"
      "The sequence terminates at n = 1 other wise repeats \n"
      "This program generates the Collatz Sequence based on given n \n")

def main(): #main function
    #ask for the number
    print("Enter the number for which Collatz sequence is needed to be generated(greater than 0) or QUIT")
    while True:
        n = input("> ")
        if n.upper().startswith("Q"):
            print("Program terminated")
            sys.exit()
        if not n.isdecimal():
            print("Please enter the correct value for n (It should be integer)")
            continue
        if 0 < int(n):
            n = int(n)
            break

    print(f"{n}", end="")
    #prints the next number in the sequence
    next_num = n
    while True:
        if next_num == 1:
            break
        if next_num % 2 == 0:
            next_num = int(next_num/2)
            print(f", {next_num}", end="", flush=True)
        elif next_num % 2 == 1:
            next_num = int(3 * next_num + 1)
            print(f", {next_num}", end="",flush=True)
        time.sleep(0.1)


if __name__ == '__main__':
    main()