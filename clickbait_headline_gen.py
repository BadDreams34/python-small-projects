"""Clickbait headline generator
Generates clickbait headlines for any content from your website"""

print("This program generates specified number of clickbait headlines")

import random

#set up the constants:
OBJECT_PRONOUNS = ['her','him','them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
            'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
         'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
         'Plastic Straw','Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
          'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']


def main():


    # asks for number of clickbaits
    print("Enter the number of headlines to generate")
    while True:
        num_headlines = input("> ")
        if not num_headlines.isdecimal():
            print("Please Enter the correct number of headlines (it should be a whole number)")
        elif 0 < int(num_headlines):
            num_headlines = int(num_headlines)
            break

    for i in range(num_headlines):
        clickbait_type = random.randint(1,8)
        if clickbait_type == 1:
            headline = generate_are_millennials_killing_headline()
        elif clickbait_type == 2:
            headline = generate_what_you_dont_know_headline()
        elif clickbait_type == 3:
            headline = generate_big_companies_hate_her_headline()
        elif clickbait_type == 4:
            headline = generate_you_wont_believe_headline()
        elif clickbait_type == 5:
            headline = generate_you_dont_want_to_know_headline()
        elif clickbait_type == 6:
            headline = generate_gift_idea_headline()
        elif clickbait_type == 7:
            headline = generate_reasons_why_headline()
        elif clickbait_type == 8:
            headline = generate_job_automated_headline()
        print(headline)
    print()


# initial warnings
website = random.choice(['wobsite', 'blag', 'Facebuuk', 'Googles',
                         'Facesbook', 'Tweedie', 'Pastagram'])
when = random.choice(WHEN).lower()
print(f"Post to {website} {when} or you're fired")


#each of the following functions returns a different type of headline

def generate_what_you_dont_know_headline():
    noun = random.choice(NOUNS)
    plural_noun = f"({random.choice(NOUNS)}s)"
    when = random.choice(WHEN)
    return f"Without this {noun}, {plural_noun} could kill you {when}."

def generate_are_millennials_killing_headline():
    noun = random.choice(NOUNS)
    return f"Are millennials_killing the {noun} industry?"

def generate_big_companies_hate_her_headline():
    return f"Big companies Hate {random.choice(OBJECT_PRONOUNS)}! See How This {random.choice(STATES)} {random.choice(NOUNS)} invented a cheaper {random.choice(NOUNS)}"

def generate_you_wont_believe_headline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)
    return f"You wont believe What this {state} {noun} Found in {pronoun} {place}"

def generate_you_dont_want_to_know_headline():
    plural_noun_1 = f"{random.choice(NOUNS)}s"
    plural_noun_2 = f"{random.choice(NOUNS)}s"
    return f"Why {plural_noun_1} don't want to know about {plural_noun_2}?"

def generate_gift_idea_headline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return f'{number} Gift Ideas to Give Your {noun} From {state}'

def generate_reasons_why_headline():
    number_1 = random.randint(3, 19)
    plural_noun = f'{random.choice(NOUNS)}s'
    # number2 should be no larger than number1:
    number_2 = random.randint(1, number_1)
    return '{} Reasons Why {} Are More Interesting Than You Think (Number {} Will Surprise You!)'.format(number_1,
                                                                                                         plural_noun,
                                                                                                         number_2)
def generate_job_automated_headline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0,2)
    pronoun_1 = POSSESIVE_PRONOUNS[i]
    pronoun_2 = PERSONAL_PRONOUNS[i]
    if pronoun_1 == 'Their':

        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Were Wrong.'.format(state, noun, pronoun_1,
                                                                                          pronoun_2)
    else:
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Was Wrong.'.format(state, noun, pronoun_1,
                                                                                         pronoun_2)



if __name__ == '__main__':
    main()