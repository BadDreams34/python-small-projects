"""Soduku Solver
This program solves a given sodoku """



sudoku = {
            1: [" ", "2", "7", " ", "6", " ", "3", "4", " "],
            2: [" ", " ", " ", "2", " ", "9", " ", " ", " "],
            3: ["9", " ", " ", " ", "5", " ", " ", " ", "2"],
            4: ["4", " ", " ", "8", "2", "3", " ", " ", "5"],
            5: [" ", "5", " ", " ", "4", " ", " ", "6", " "],
            6: ["3", "7", " ", " ", " ", " ", " ", "1", "4"],
            7: [" ", " ", "1", " ", " ", " ", "5", " ", " "],
            8: [" ", "3", "5", " ", " ", " ", "9", "7", " "],
            9: [" ", " ", " ", " ", "7", " ", " ", " ", " "]
        }

def main():
    filled_row = 0
    # asks for the user input
    # sudoku = userinput()
    while True: #until the sudoku is complete
        # check for winning condition
        #removes the filled row
        sudoku_shot = sudoku.copy()
        sudoku_shot_test = sudoku_shot.copy()
        for row_num, row in sudoku_shot_test.items():
                if all(item not in ['', ' '] for item in row):
                    del sudoku_shot[row_num]

        if len(sudoku_shot) == 0:
            print("All solved")
            break

        solvable = False

        for row_ind in sudoku_shot.keys(): # for each row at a time
            max_filled_row_num = row_ind # row_num under calculations

            #finding the missing index for the curr_row along with the missing items
            missing_chars = []
            all_possibilities = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

            # getting the remaining char
            for item in all_possibilities:
                if item not in sudoku[max_filled_row_num]:
                    missing_chars.append(item)

            #fill the positions
            for missing_char in missing_chars: #for each missing char
                if fill_missing_char(missing_char, max_filled_row_num):
                    solvable = True

        # if not solvable with the current algorithm
        if not solvable:
            print("The given sudoku can't be solved further with the current logic !")
            break




# def userinput():
    # """ asks for the rows of sodoku and stores them in a dictionary """
    # for i in range(9):
    #     print(f"Please enter the numbers of Row {i+1} seperated by comma, use blank space if there is no value for the given place")
    #
    #     while True:
    #         row = input("> ")
    #         row_given = row.split(",")
    #         if len(row_given) != 9:
    #             print("Please check your input there must be 9 values")
    #             continue
    #         valid_inp = True
    #         for item in row_given:
    #             if item not in ["", " "] and not 0 <= int(item) <= 9 :
    #                 print("Item must be integer or a blank space")
    #                 valid_inp = False
    #                 break
    #         nums = [item for item in row_given if item not in ["", " "]]
    #         if len(set(nums)) != len(nums):
    #             print("Duplication present")
    #             continue
    #         if valid_inp:
    #             sudoku[i+1] = row_given
    #             break



def max_filled():
    """ returns the row number for the row with maximum number of filled numbers """
    row_max = 1
    max_filled_items = 0
    for row_num, row in sudoku.items():

        if row_num == 1:
            for item in row:
                if item not in ["", " "]:
                    max_filled_items +=1
        else:
            curr_filled_items = 0
            for item in row:
                if item not in ["", " "]:
                    curr_filled_items +=1

            if curr_filled_items > max_filled_items:
                max_filled_items = curr_filled_items
                row_max = row_num

    return row_max


def fill_missing_char(missing_char,max_filled_row_num):
    '''fills the char in the missing positions if possible for a given row'''
    # finding the positions where character can be filled
    possible_filling_positons = []
    for item_pos, item in enumerate(sudoku[max_filled_row_num]):
        if item in ["", " "]:
            possible_filling_positons.append(item_pos+1)
    # check for the missing char presence in that block if its already present and removes the possible filling positons if found
    copy_filling_pos = possible_filling_positons.copy()
    for ind in copy_filling_pos:
        #rows
        if max_filled_row_num in [1,2,3]:
            rows = [1,2,3]
        elif max_filled_row_num in [4,5,6]:
            rows = [4,5,6]
        elif max_filled_row_num in [7,8,9]:
            rows = [7,8,9]

        #columns
        if ind in [1,2,3]:
            cols = [1,2,3]
        elif ind in [4,5,6]:
            cols = [4,5,6]
        elif ind in [7,8,9]:
            cols = [7,8,9]

        block = []  # contains all the items in the given block

        # append the items in the block
        for row in rows:
            for column in cols:
                block.append(sudoku[row][column-1])

        # check for the missing char in block
        if missing_char in block:
            # removes the given three positions from the possible_filling_positions if they are blank
            if ind in possible_filling_positons:
                    possible_filling_positons.remove(ind)



    # checks for the possible filling positions if that column has the missing character if yes, then remove the given column from filliing postion
    copy_fil_pos = possible_filling_positons.copy()
    for col in copy_fil_pos:
        if missing_char in column_return(col):
            possible_filling_positons.remove(col)


    if len(possible_filling_positons) == 1:
        sudoku[max_filled_row_num][possible_filling_positons[0]-1] = missing_char
        return True
    else:
        return False



def column_return(col_num):
    '''returns the list of the values for the given column'''
    column = []
    for row_num, row in sudoku.items():
        column.append(row[col_num-1])
    return column

def pretty_print(sudoku: dict[int, list[str]]):
    for row_num, row in sorted(sudoku.items(), key=lambda x: x[0]):
        print(f"{row_num}: ", end='')
        print(*row, sep=' ')



main()
pretty_print(sudoku)