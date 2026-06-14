"""Soduku Solver
This program solves a given sodoku """

# to do :

# ( if more than one has same then choose any
# and mark the other for next iteration )
# 3.
# 4. repeat these rules again for the same row if it solved any of the given thing and break out of that loop
# 5. repeat for each row again

# progress :

#finished
# 1. take the input and store the sodoku as rows and columns 2d structure with each item indexable in some ways
# 2. for each row check the one which has maximum no. of items already filled
# 3. DONE  for choose row, find which one are missing and check for each missing : these three rules
# #    - if the number is present in the periphery atoms, then basically discard those three blocks as well if not present just pass bro do nothing here
# #    - if that number is not present in the given column then tag that position as possible chance if its present then discard that position as almost like nonoe of the other rows filled one there
# #    - if just one possible chance then just fill that in that row
# i want to keep checking for the same row until all the items are being checked again if i found a solution
# if i don't find any solution then no worries so just break


sudoku = {}

def main():
    # asks for the user input
    userinput()
    i = 0
    while i<10: # for each row at a time
        max_filled_row_num = max_filled() # row_num under calculations

        #finding the missing index for the curr_row along with the missing items
        missing_chars = []
        all_possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # getting the remaining char
        for item in all_possibilities:
            if item not in sudoku[max_filled_row_num]:
                missing_chars.append(item)

        #fill the positions
        for missing_char in missing_chars: #for each missing char
            fill_missing_char(missing_char, max_filled_row_num)

        i += 1


def userinput():
    """ asks for the rows of sodoku and stores them in a dictionary """
    for i in range(9):
        print(f"Please enter the numbers of Row {i+1} seperated by comma, use blank space if there is no value for the given place")

        while True:
            row = input("> ")
            row_given = row.split(",")
            if len(row_given) != 9:
                print("Please check your input there must be 9 values")
                continue
            valid_inp = True


            for item in row_given:
                if item not in ["", " "] and not 0 <= int(item) <= 9 :
                    print("Item must be integer or a blank space")
                    valid_inp = False
                    break

            nums_only = [item for item in row_given if item not in ["", " "]]
            if len(set(nums_only)) != len(nums_only):
                print("Duplicate values are not allowed")
                continue

            if valid_inp:
                sudoku[i+1] = row_given
                break

        #prints the solved sudoku
        for rows in sudoku.values():
            for item in rows:
                print(item)
            print('\n')

def max_filled():
    """ returns the row number for the row with maximum number of filled numbers """
    for row_num, row in sudoku.items():

        if row_num == 1:
            max_filled_items = 0
            row_max = 1
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

    # finds the index of the missing char
    ind = 1
    for i, item in enumerate(sudoku[max_filled_row_num]):
        if item == missing_char:
            ind = i
            break
    col = ind + 1

    block_num = (max_filled_row_num - 1) * 3 + col
    block = []  # contains all the items in the given block
    # rows
    if max_filled_row_num in [1, 2, 3]:
        rows = [1, 2, 3]
    elif max_filled_row_num in [4, 5, 6]:
        rows = [4, 5, 6]
    elif max_filled_row_num in [7, 8, 9]:
        rows = [7, 8, 9]

    # columns
    if block_num in [1, 4, 7]:
        cols = [1, 2, 3]
    elif block_num in [2, 5, 8]:
        cols = [4, 5, 6]
    elif block_num in [3, 6, 9]:
        cols = [6, 7, 8]

    # append the items in the block
    for row in rows:
        for column in cols:
            block.append(sudoku[row][column - 1])

    # check for the missing char in block
    if missing_char in block:
        # removes the given three positions from the possible_filling_positions if they are blank
        copy_possible_values = possible_filling_positons.copy()
        for value in cols:
            if value in copy_possible_values:
                possible_filling_positons.remove(value)


    # checks for the possible filling positions if that column has the missing character if yes, then remove the given column from filliing postion
    for col in possible_filling_positons:
        if missing_char in column_return(col,max_filled_row_num):
            possible_filling_positons.remove(col)

    if len(possible_filling_positons) == 1:
        sudoku[max_filled_row_num][possible_filling_positons[0]] = missing_char



def column_return(col_num,row):
    '''returns the list of the values for the given column'''
    column = []
    for row_num, row in sudoku[row]:
        column.append(row[col_num-1])
    return column


main()
