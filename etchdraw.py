'''Etching Drawer
This program draws line on the canvas with the keys W A S D'''
import shutil,sys

WIDTH = shutil.get_terminal_size()[0]
HEIGHT = 50
X = 'x'
Y = 'y'

#char constants
UP_DOWN_CHAR         = chr(9474)  # Character 9474 is '│'
LEFT_RIGHT_CHAR      = chr(9472)  # Character 9472 is '─'
DOWN_RIGHT_CHAR      = chr(9484)  # Character 9484 is '┌'
DOWN_LEFT_CHAR       = chr(9488)  # Character 9488 is '┐'
UP_RIGHT_CHAR        = chr(9492)  # Character 9492 is '└'
UP_LEFT_CHAR         = chr(9496)  # Character 9496 is '┘'
UP_DOWN_RIGHT_CHAR   = chr(9500)  # Character 9500 is '├'
UP_DOWN_LEFT_CHAR    = chr(9508)  # Character 9508 is '┤'
DOWN_LEFT_RIGHT_CHAR = chr(9516)  # Character 9516 is '┬'
UP_LEFT_RIGHT_CHAR   = chr(9524)  # Character 9524 is '┴'
CROSS_CHAR           = chr(9532)  # Character 9532 is '┼'

# i will ask w a s d if w then i will do what ? i need a canvas dictionary # WRONG APPROACH TO THINK thinkk of irl first without pytho
# wasd to move if w then draw one up if a thne at that position draw one left same for s and d
# it should be within the canvas i.e. if it exceeded the length that key should do nothing
# also it should handle the other respective keywords as well
# it should save the given canvas in a file if pressed s

# now how will you draw a canvas say the hash is # is my curr x, curr y coordinate
# WASD will change my hash as well as draw a line
# how will i store where the hash is ? by curr x and curr y
# how will i store where the lines are ? we will have a dictionary of rows and columns perhaps tuples with each value storing
# the current char which it will get pushed by curr x and curr y due to move ment of w a s d



def main(): #main function
    board = {}  # stores the x,y position and the respective character at that point
    canvas = [] # the actual board
    curr_pos = {X: 0, Y: 0} # stores the current pointer positions
    key_strokes = [None, None] # stores the two consecutive keystrokes

    # ask for input
    while True:

        print("W A S D to move, C to clear the screen, F to save the game, H for Help")
        key = input("> ")

        #checks for the presence of key in the combined words
        if key.upper() not in ["W","A","S","D","C","F","H"]:
            continue
        key = key.upper()

        # draw movements and move cursor accordingly
        if key == "W":
            key_strokes.pop(0)
            key_strokes.append(key)
            draw_line(key_strokes,curr_pos, board)
            print_board(curr_pos, board)
        elif key == "A":
            key_strokes.pop(0)
            key_strokes.append(key)
            draw_line(key_strokes,curr_pos, board)
            print_board(curr_pos, board)
        elif key == "S":
            key_strokes.pop(0)
            key_strokes.append(key)
            draw_line(key_strokes,curr_pos, board)
            print_board(curr_pos, board)

        elif key == "D":
            key_strokes.pop(0)
            key_strokes.append(key)
            draw_line(key_strokes,curr_pos, board)
            print_board(curr_pos, board)
        elif key == "C":
            board = {}
            curr_pos[X] = 0
            curr_pos[Y] = 0
            print_board(curr_pos, board)

        elif key == "H":
            print("""This game draws on the board based the input given by W A S D
             It draws the line based on the given keystrokes 
             Press W to draw up line
             Press S to draw a line downwards
             Press A to draw left line
             Press D to draw a line right
             Press F to save the file 
             Press C to clear the screen
             Press H for this help page""")

        elif key == "F":
            print("Enter the filename to save it")
            file_name = input("> ")

            #make sure the file name ends with .txt
            if not file_name.endswith(".txt"):
                file_name += ".txt"
            try:
                with open(file_name, "w", encoding='utf-8') as file:
                    file.write(save_file(board))
                    print(f"🎨 Canvas successfully saved to '{file_name}'!")
            except Exception as e:
                print(f"Error : {e}")



def draw_line(keys,curr_pos ,board):
    """updates the dictionary values of board according to the curr_mouse position and the given key and updates the curr_mouse accordingly"""
    if curr_pos[X] < 0:
        curr_pos[X] = 0
    if curr_pos[Y] < 0:
        curr_pos[Y] = 0
    if curr_pos[X] > WIDTH:
        curr_pos[X] = WIDTH
    if curr_pos[Y] > HEIGHT:
        curr_pos[Y] = HEIGHT

    x = curr_pos[X]
    y = curr_pos[Y]
    prev_key, curr_key = keys


    print(f"X: {x}, Y : {y}")
    if (x,y) not in board.keys():
        if curr_key == "W":
            curr_pos[Y] -= 1
            if prev_key is None:
                board[(x, y)] = UP_DOWN_CHAR
            elif prev_key == "W":
                board[(x, y)] = UP_DOWN_CHAR
            elif prev_key == "A":
                board[(x, y)] = UP_RIGHT_CHAR

            elif prev_key == "S":
                pass
            elif prev_key == "D":
                board[(x, y)] = UP_LEFT_CHAR


        elif curr_key == "D":
            curr_pos[X] += 1
            if prev_key is None:
                board[(x, y)] = LEFT_RIGHT_CHAR
                print(f"x: {x}")
            elif prev_key == "W":
                board[(x, y)] = DOWN_RIGHT_CHAR
            elif prev_key == "D":
                board[(x, y)] = LEFT_RIGHT_CHAR
                print(f"x: {x}")
            elif prev_key == "A":
                pass
            elif prev_key == "S":
                board[(x, y)] = UP_RIGHT_CHAR


        elif curr_key == "A":
            curr_pos[X] -= 1
            if prev_key is None:
                board[(x, y)] = LEFT_RIGHT_CHAR
            elif prev_key == "W":
                board[(x, y)] = DOWN_LEFT_CHAR
            elif prev_key == "A":
                board[(x, y)] = LEFT_RIGHT_CHAR
            elif prev_key == "S":
                board[(x, y)] = UP_LEFT_CHAR
            elif prev_key == "D":
                pass

        elif curr_key == "S":
            curr_pos[Y] +=1
            if prev_key is None:
                board[(x, y)] = UP_DOWN_CHAR
            elif prev_key == "S":
                board[(x, y)] = UP_DOWN_CHAR
            elif prev_key == "A":
                board[(x, y)] = DOWN_RIGHT_CHAR
            elif prev_key == "W":
                pass
            elif prev_key == "D":
                board[(x, y)] = DOWN_LEFT_CHAR

    else:
        if curr_key == "W":
            curr_pos[Y] -= 1
        elif curr_key == "D":
            curr_pos[X] += 1
        elif curr_key == "A":
            curr_pos[X] -= 1
        elif curr_key == "S":
            curr_pos[Y] +=1






def print_board(curr_pos,board):
    '''prints the given characters as per x and y values on the screen '''
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x == curr_pos[X] and y == curr_pos[Y]:
                print("#", end='')
            else:
                print(board.get((x,y), " "), end='')
        print()

def save_file(board):
    save_text = []
    for y in range(HEIGHT):
        for x in range(WIDTH):
            save_text.append(board.get((x, y), " "))
        save_text.append("\n")
    return "".join(save_text)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program Ended")
        sys.exit()