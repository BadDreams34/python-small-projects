"""Conway Game Of life
Generates the cell based on orthogonal grid and the pattern as described by conway"""
import copy
import random
import time
import os

#defining constants:
CELLS_ALIVE = 123
ROWS = 25
COLUMNS = 25


print('''This program generates the pattern of Conway Game Of Life
by following these simple rules,
1) any cell can be either dead or living in a two dimensional grid
2) each cell has 8 neighbours
3) if a live cell has less than 2 or greater than 3 alive neighbours it will become dead in the next generation
4) if a live cell has 2 or 3 neighbors which are alive then it will stay alive in the next generation
5) if a dead cell has exactly 3 neighbours then it will be alive in the next generation
6) new cells position are being determined by their relative position in the previous generation and all the other previous generation are being discarded
''')

#say the grid column and rows define them
#define the number of live cells initially
# arrange them randomly initially
# use.find and thus calculate the number of neighbours if they match live cell then replace that index with "O" else with " "

def main():
    #creates an initial grid
    grid = []
    for i in range(ROWS):
        for j in range(COLUMNS-1):
                grid.append(" ")
        grid.append("\n")

    #assign cells initially to the grid
    for i in range(CELLS_ALIVE):
        row_random = random.randint(0,ROWS-1)
        column_random = random.randint(0, COLUMNS-2)
        grid[row_random * COLUMNS + column_random] = "O"


    #displays the initial grid
    print("".join(grid))
    time.sleep(2)
    generation = 1
    while True: #iteration over each generation
        os.system("cls")
        old_grid = copy.deepcopy(grid)

        for i in range(ROWS):
            for j in range(COLUMNS-1):
                neighbour = cell_neighbour_calc(old_grid,i,j)
                if old_grid[i*COLUMNS+ j] == "O": #for each live cell
                    if neighbour < 2 or neighbour > 3:
                        grid[i*COLUMNS+ j] = " "
                elif old_grid[i*COLUMNS+ j] == " ": #for each dead cell
                    if neighbour == 3:
                        grid[i*COLUMNS+ j] = "O"
        current_state = "".join(grid)
        print(f"Generation : {generation}")
        generation+=1
        print(f"{current_state}", flush=True)
        print("Hi")
        time.sleep(2)
    


def cell_neighbour_calc(grid,i,j):
    num_neighbour = 0
    if i>0 and j>0 and grid[(i-1)*COLUMNS + (j-1)]== "O" :
        num_neighbour +=1
    if i>0 and grid[(i-1)*COLUMNS + j]== "O"  :
        num_neighbour +=1
    if j < COLUMNS - 2  and i>0 and grid[(i-1)*COLUMNS + (j+1)] == "O":
        num_neighbour +=1
    if j < COLUMNS - 2 and grid[i*COLUMNS + (j+1)] == "O":
        num_neighbour +=1
    if j>0 and grid[i*COLUMNS + (j-1)] == "O":
        num_neighbour +=1
    if i < ROWS-1 and j < COLUMNS - 2 and grid[(i+1)*COLUMNS + (j+1)] == "O":
        num_neighbour +=1
    if i < ROWS-1 and grid[(i+1)*COLUMNS + j] == "O":
        num_neighbour +=1
    if i < ROWS-1 and j>0 and grid[(i+1)*COLUMNS + (j-1)] == "O":
        num_neighbour +=1
    return num_neighbour


if __name__ == "__main__":
    main()
