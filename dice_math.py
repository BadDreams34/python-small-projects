'''Dice Math
A flashcard addition game where user has to guess the sum of dices'''

import random, sys, time


#Set up the constants
TIME_EACH_GUESS = 10 #time given to the user to guess the sum
#Dictionary for holding ASCII ART FOR VARIOUS DICE FACES
DICE_FACE = {
    1: '''
-----
| 0 |
|   |
-----''',
    2: '''
-----
| 0 |
| 0 |
-----
    ''',
    3: '''
-----
|0 0|
| 0 |
-----
    ''',
    4: '''
-----
|0 0|
|0 0|
-----
    ''',
    5: '''
-----
|0 0|
|000|
-----
    ''',
    6: '''
-----
|000|
|000|
-----
    '''
    }



print('''Dice Math
This program randomly throws two to six dices and we need to calculate the sum of dices as fast as possible,
If we guessed it right, our score will increase by 4,
If we guessed it wrong it will be reduced by 1''')

input("Press Enter to Begin.")

def main():
    score = 0
    while True: #for each round
        die_rolls = []
        num_dice = random.randint(2,6)
        sum = 0

        #rolling for each round
        for i in range(num_dice):
            die_rolls.append(random.randint(1,6))
        for roll in die_rolls: #displays the ascii art for each round
            print(DICE_FACE[roll], end = ' ')
            sum += roll
        print(f"Guess the sum, You have {TIME_EACH_GUESS} to guess it.")
        print("Enter Your guess")
        #taking guess as input
        while True:
            guess = input("> ")
            if guess.isdecimal():
                guess = int(guess)
                break


        #input check
        if guess == sum:
            score +=4
            print(f"You guessed it, Your total score is now {score}")
        else:
            score -= 1
            print(f"Its not the correct guess, Your score is {score}")
        time.sleep(TIME_EACH_GUESS)
        

main()


