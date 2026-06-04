"""Conway's Game of life
A terminal game in which each cell gets passed or reproduce on the next generation"""


import time, copy, sys, random,os

#defining constants
ALIVE = 'O' #symbol for alive cells
DEAD = ' ' #symbol for dead cells
WIDTH = 25 #width of the grid
HEIGHT = 25 #height of the grid

print('''This program generates the pattern of Conway Game Of Life
by following these simple rules,
1) any cell can be either dead or living in a two dimensional grid
2) each cell has 8 neighbours
3) if a live cell has less than 2 or greater than 3 alive neighbours it will become dead in the next generation
4) if a live cell has 2 or 3 neighbors which are alive then it will stay alive in the next generation
5) if a dead cell has exactly 3 neighbours then it will be alive in the next generation
6) new cells position are being determined by their relative position in the previous generation and all the other previous generation are being discarded
''', flush=True)


#cells and next_cells are the dictionary which holds the current states of cells

next_cells = {}

# Put random alive and dead cells in next generation
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0,1) == 1:
            next_cells[(x,y)] = ALIVE
        else:
            next_cells[(x,y)] = DEAD


while True: # iteration over each generation
    os.system("cls")

    cell = copy.deepcopy(next_cells)

    #prints the current generation
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cell[(x,y)],end='', flush=True)
        print(flush=True)
    print("Press Ctrl + C to quit")

    for x in range(WIDTH):
        for y in range(HEIGHT):
            # wrap around for finding neighbours
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            top = (y - 1) % HEIGHT
            bottom = (y + 1) % HEIGHT

            #counts the number of neighbour
            num_neighbours = 0

            if cell[(left, top)] == ALIVE:
                num_neighbours +=1
            if cell[(x, top)] == ALIVE:
                num_neighbours += 1
            if cell[(right, top)] == ALIVE:
                num_neighbours +=1
            if cell[(x, bottom)] == ALIVE:
                num_neighbours += 1
            if cell[(left, y)] == ALIVE:
                num_neighbours +=1
            if cell[(right, y)] == ALIVE:
                num_neighbours += 1
            if cell[(left, bottom)] == ALIVE:
                num_neighbours +=1
            if cell[(right, bottom)] == ALIVE:
                num_neighbours += 1
            #updates the current generation based on games rule
            if cell[(x,y)] == ALIVE and (num_neighbours == 3 or num_neighbours == 2):
                next_cells[(x,y)] = ALIVE
            elif cell[(x,y)] == DEAD and num_neighbours == 3:
                next_cells[(x,y)] = ALIVE
            else:
                next_cells[(x,y)] = DEAD
    time.sleep(1) #buffering to let the cells load


