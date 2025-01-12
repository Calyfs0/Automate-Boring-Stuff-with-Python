# Conways' Game of Life
__version__ = 0
import random, time, copy, sys

WIDTH = 79
HEIGHT = 20
DEAD = ' '
ALIVE = 'O'

# Create a list of list for the cells:
nextCells = {}
# Put random dead and alive cells into nextCells:
for x in range(WIDTH):  # Loop over every possible column.
    for y in range(HEIGHT):  # Loop over every possible row.
        # 50/50 chance for starting cells being alive or dead.
        # if random.randint(0, 1) == 0:
        if (x, y) in ((1, 0), (2, 1), (0, 2), (1, 2), (2, 2)):
            nextCells[(x, y)] = ALIVE  # Add a living cell.
        else:
            nextCells[(x, y)] = DEAD  # Add a dead cell.

# Main program


while True:  # Main program loop.
    # Each iteration of this loop is a step of the simulation.

    print('\n' * 50)  # Separate each step with newlines.
    cells = copy.deepcopy(nextCells)

    # Print cells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end='')  # Print the # or space.
        print()  # Print a newline at the end of the row.
    print('Press Ctrl-C to quit.')

    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get the neighboring coordinates of (x, y), even if they
            # wrap around the edge:
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            # Count the number of living neighbors:
            numNeighbours = 0
            if cells[(left, above)] == ALIVE:
                numNeighbours += 1  # Top-left neighbor is alive.
            if cells[(x, above)] == ALIVE:
                numNeighbours += 1  # Top neighbor is alive.
            if cells[(right, above)] == ALIVE:
                numNeighbours += 1  # Top-right neighbor is alive.
            if cells[(left, y)] == ALIVE:
                numNeighbours += 1  # Left neighbor is alive.
            if cells[(right, y)] == ALIVE:
                numNeighbours += 1  # Right neighbor is alive.
            if cells[(left, below)] == ALIVE:
                numNeighbours += 1  # Bottom-left neighbor is alive.
            if cells[(x, below)] == ALIVE:
                numNeighbours += 1  # Bottom neighbor is alive.
            if cells[(right, below)] == ALIVE:
                numNeighbours += 1  # Bottom-right neighbor is alive.

            if cells[(x, y)] == ALIVE and (numNeighbours == 2 or numNeighbours == 3):
                nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and numNeighbours == 3:
                nextCells[(x, y)] = ALIVE
            else:
                nextCells[(x, y)] = DEAD
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        # print('By Al Sweigart al@inventwithpython.com')
        sys.exit()  # When Ctrl-C is pressed, end the program.
