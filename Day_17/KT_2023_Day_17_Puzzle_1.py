# initialize variables
side = []
changingGrid = []
nextGrid = []
neighbors = [(-1, -1, -1),(-1, -1, 0),(-1, -1, 1),(-1, 0, -1),(-1, 0, 0),(-1, 0, 1),(-1, 1, -1),(-1, 1, 0),(-1, 1, 1),(0, -1, -1),(0, -1, 0),(0, -1, 1),(0, 0, -1),(0, 0, 0),(0, 0, 1),(0, 1, -1),(0, 1, 0),(0, 1, 1),(1, -1, -1),(1, -1, 0),(1, -1, 1),(1, 0, -1),(1, 0, 0),(1, 0, 1),(1, 1, -1),(1, 1, 0),(1, 1, 1)]
counter = 0
active = 0

f = open('energy_input.txt')

# set the first changingGrid to have the 2d array from the file input
for line in f.readlines():
    row = []
    if (line.find("\n") != -1):
        for i in range(len(line)-1):
            row.append(line[i:i+1])
    else:
        for i in range(len(line)):
            row.append(line[i:i+1])
    side.append(row)
changingGrid.append(side)

f.close()

# define a function to expand the dimension once in every direction
def expandGrid(curGrid):
    newGrid = list(curGrid)
    x, y, z = len(curGrid[0][0]), len(curGrid[0]), len(curGrid)
    for cell in range(z):
        # expand the left and right of the old grid (x)
        for r in range(len(newGrid[cell])):
            newGrid[cell][r].insert(x, '.')
            newGrid[cell][r].insert(0, '.')
        # expand the top and bottom of the grid (y)
        newGrid[cell].insert(y, ['.']*(y+2))
        newGrid[cell].insert(0, ['.']*(y+2))
    # add new cells (z)
    newGrid.insert(z, [['.']*(x+2)]*(y+2))
    newGrid.insert(0, [['.']*(x+2)]*(y+2))
    return newGrid

# define a function that changes the state of a cube to active or inactive based on its neighbors
def changeCube(cube, zloc, yloc, xloc):
    activeCount = 0
    # check each of the cube's neigbors and count if they are active or not
    for z, y, x in neighbors:
        nz, ny, nx = zloc+z, yloc+y, xloc+x
        if (0 <= nz < len(changingGrid)-1) and (0 <= ny < len(changingGrid[0])) and (0 <= nx < len(changingGrid[0][0])):
            if (changingGrid[nz][ny][nx] == '#'):
                activeCount += 1
    # Change if cube is active or not based on how many of its neighbors are active or not and return the cube's state
    if (cube == '#'):
        if not (2 <= activeCount <= 3):
            cube = '.'
    else:
        if (activeCount == 3):
            cube = '#'
    return cube

# perform the six-cycle bootup process
while (counter != 6):
    counter += 1
    changingGrid = expandGrid(changingGrid)
    nextGrid = list(changingGrid)
    for c in range(len(changingGrid)):
        for v in range(len(changingGrid[c])):
            for h in range(len(changingGrid[c][v])):
                nextGrid[c][v][h] = changeCube(changingGrid[c][v][h], c, v, h)
    changingGrid = list(nextGrid)

print(changingGrid)
# count how many cubes are active after the bootup process and print the result
for c in range(len(changingGrid)):
        for v in range(len(changingGrid[c])):
            for h in range(len(changingGrid[c][v])):
                if (changingGrid[c][v][h] == '#'):
                    active += 1

print("There are", active, "active cubes")
