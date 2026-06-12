'''Duckling game
Generates an animation of ducklings down the screen infinitely
>" )   =^^)    (``=   ("=  >")    ("=
(  >)  (  ^)  (v  )  (^ )  ( >)  (v )
 ^ ^    ^ ^    ^ ^    ^^    ^^    ^^'''


import random, sys, shutil, time



# Set up the constants
WIDTH = shutil.get_terminal_size()[0] - 1
PAUSE = 0.25
DUCKLING_WIDTH = 5
DENSITY = 0.15

HEAD = 'head'
BODY = 'body'
FOOT = 'feet'
CHUBBY = 'chubby'
VERY_CHUBBY = 'very chubby'
LEFT = 'left'
RIGHT = 'right'
WIDE = 'wide'
BEADY = 'beady'
HAPPY = 'happy'
ALOOF = 'aloof'
OPEN = 'open'
CLOSED = 'closed'
OUT = 'out'
DOWN = 'down'
UP = 'up'

def main(): #main function
    print("Duckling Animation")
    print("Press Ctrl+C to quit")
    time.sleep(2)
    duck_lane = [None] * (WIDTH // DUCKLING_WIDTH)
    while True: # main game loop
        for (lane_num, duck_obj) in enumerate(duck_lane): # for each duck_lane of 'duckling_width' size
            if duck_obj is None and random.random() <= DENSITY:
                duck_obj = Duckling()
                duck_lane[lane_num] = duck_obj

            if duck_obj != None:
                print(duck_obj.draw_next(), end='')
                # delete the duckling if we've finished the drawing
                if duck_obj.next_part_to_draw == None:
                    duck_lane[lane_num] = None
            else:
                print(" "* DUCKLING_WIDTH, end='')
        print()
        sys.stdout.flush()
        time.sleep(PAUSE)



# duckling class
class Duckling:
    #assigns various body features randomly
    def __init__(self):
        self.direction = random.choice([LEFT,RIGHT])
        self.body = random.choice([CHUBBY,VERY_CHUBBY])
        self.wing = random.choice([OUT, UP, DOWN])
        self.mouth = random.choice([OPEN,CLOSED])

        if self.body is CHUBBY:
            #chubby ducklings have only beady eyes
            self.eyes = BEADY
        else:
            self.eyes = random.choice([BEADY, WIDE, HAPPY, ALOOF])

        self.next_part_to_draw = HEAD



    def get_head_str(self):
        """Returns the head string"""
        head_str = ''
        if self.direction is LEFT:
            #assigns the mouth
            head_str += ">" if self.mouth is OPEN else "="
            #assign the eyes
            head_str += '"' if self.eyes is BEADY and self.body is CHUBBY else '" ' if self.eyes is BEADY and self.body is VERY_CHUBBY else "''" if self.eyes is WIDE else '^^' if self.eyes is HAPPY else "``"

            head_str += ") "

        if self.direction is RIGHT:
            head_str += "( "
            #assign the eyes
            head_str += '"' if self.eyes is BEADY and self.body is CHUBBY else ' "' if self.eyes is BEADY and self.body is VERY_CHUBBY else "''" if self.eyes is WIDE else '^^' if self.eyes is HAPPY else "``"
            #assigns the mouth
            head_str += "<" if self.mouth is OPEN else "="

        if self.body is CHUBBY:
            head_str += " " #an extra space to make width linear
        return head_str



    def get_body_str(self):
        '''returns the body string of the duckling'''
        body_str = '(' #get the left side of the body
        if self.direction == LEFT:
            if self.body == CHUBBY:
                body_str += ' '
            else:
                body_str += '  '

            # Get the wing
            if self.wing == OUT:
                body_str += '>'
            elif self.wing == UP:
                body_str += '^'
            elif self.wing == DOWN:
                body_str += 'v'

        if self.direction == RIGHT:
            # get the wing
            if self.wing == OUT:
                body_str += '<'
            if self.wing == UP:
                body_str += '^'
            if self.wing == DOWN:
                body_str += 'v'
            # get the internal space
            if self.body == CHUBBY:
                body_str += ' '
            else:
                body_str += '  '
        body_str += ')'
        if self.body == CHUBBY: # an extra space for uniform width
            body_str += " "
        return body_str

    def get_feet_str(self):
        '''returns the string of the duckling's feet'''
        if self.body == CHUBBY:
            return ' ^^  '
        elif self.body == VERY_CHUBBY:
            return ' ^ ^ '

    def draw_next(self):
        """calls the appropriate display method which is needed and None if drawing is done """
        if self.next_part_to_draw == HEAD:
            self.next_part_to_draw = BODY
            return self.get_head_str()
        elif self.next_part_to_draw == BODY:
            self.next_part_to_draw = FOOT
            return self.get_body_str()
        elif self.next_part_to_draw == FOOT:
            self.next_part_to_draw = None
            return self.get_feet_str()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Duckling Animation Aborted")
        sys.exit()