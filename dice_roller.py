"""Dice Roller
A Program which roles the dice as specified and prints the result"""

import re
import random

print("""Dice Roller
This programs take input of the dice specifications from the user and prints the 
output of the specified dice's roll
For Example, for the dice specification 45d8+3 
It will throw 45 Eight Faced Dices and will add Three in the result to produce the output.
""")


#[PC] this program first checks the user input and then rolls the dices accordingly and prints the output
def main():
    # user input is needed to be of this form :
    input_form = re.compile(r'''
        ^
        (\d*)   #matches the initial digits which corresponds to the number of dices to be thrown 
        d       #matches the literal letter d after the digits 
        (\d+)   #matches the number of faces
        ([+-]\d{1,2}|)     #matches the optional sign followed by the digit
        $
        ''', re.VERBOSE)

    while True: #main game loop
        #taking the user input
        print("Enter the configuration of the given dice for which dice is needed to be rolled !")
        while True:
            user_input = input("> ")
            if match:= input_form.search(user_input):
                if match.group(1) == '':
                    times = 1
                else:
                    times = match.group(1)
                #checks for the faces num
                face_num = int(match.group(2))
                #checks for the final_operation presence
                if match.group(3) == '':
                    final_operation = '0'
                else:
                    final_operation = match.group(3)
                break
            else:
                print("Failed to enter the correct dice specification. Please retry")

        # calculating the result
        result_str = ''
        result = 0
        for i in range(int(times)):
            die_val = random.randint(1, face_num)
            result_str += f"{die_val}, "
            result += die_val
        if final_operation != '0':
            result_str += final_operation
            final_operand = final_operation[0]
            final_dig = int(final_operation[1:])
            if final_operand == "+":
                result += final_dig
            elif final_operand == "-":
                result -= final_dig

        #printing the final string
        print(f"{result} ({result_str})")














main()