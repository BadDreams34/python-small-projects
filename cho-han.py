"""Cho-Han
A simple double dice betting game"""

import random

print("""A simple dice game
in which the player sits against the dealer sitting on the floor. 
The dealer rolls the two dice and keeps the result hidden from the
player.
The player has to bet an initial amount and to guess if the sum of 
the numbers appearing on the two dices is odd or even. If their 
guess is correct, they will receive twice the money they bet. 
The dealer takes some proportion of their win in every chance.
The player can play it till whenever they wants to player or if they
ran out of money.""")

#the total money the player have
money = 5000
while True: #main game loop

    #asks for bet
    print("You have " + str(money) + " money, How much do you want to bet?")
    while True:
        bet_amount = input("> ")
        if not bet_amount.isdecimal():
            continue
        if 0 < int(bet_amount) <= money:
            print("Bet of " + str(bet_amount) + " placed successfully.")
            print("Remaining Balance: {}".format(money-int(bet_amount)))
            bet_amount = int(bet_amount)
            money = money-bet_amount
            break
        print("Please enter a valid amount of bet. (1-{})".format(money))

    #Dealer rolls the dice and stores the result in outcome_dice
    print("Dealer rolls the double dices and hides the result from the user")
    possible_outcomes = ["cho","han"]
    outcome_dice = random.choice(possible_outcomes)

    #asks the player for the choice and decide the result
    print("Please select cho or han")
    while True:
        choice_player = input("> ")

        if not choice_player in possible_outcomes:
            print("Please enter the right choice, cho or han")
            continue

        if choice_player == outcome_dice:
            print("Player Won! They received double of their initial Bet")

            print("{} moneys sent to dealer as a fees".format(int((bet_amount) * 0.1)))
            money = (money + 2 * bet_amount) - int((bet_amount) * 0.1)
            print("your current amount = {}".format(money))
            break
        else:
            print("You lost your bet, your current amount = {}".format(money))
            break


    #checks if the player ran out of money
    if money < 0:
        print("You ran out of money! Thanks for playing")
        break

    #asks for betting again
    print("Do you want to bet again?(Y/N)")
    while True:
        play_again_status = input("> ")
        if not play_again_status in ["Y", "N", "Q"]:
            print("Please try again!")
            continue
        break

    if play_again_status == "N":
        print("Your current amount : {}".format(money))
        print("Thanks for playing")
        break

