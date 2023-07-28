# initialize variables
startingSeating = []
changedSeating = []
row = []
totalOccupied = 0
directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

# open the file and then iterate through each line
f = open('ferry_seating_input.txt')

for line in f.readlines():
    # separate each row into its own list and each character to an individual item in the list
    for c in range(len(line)):
        char = line[c:c+1]
        if (char != "\n"):
            row.append(char)
        elif (char == "\n"):
            startingSeating.append(tuple(row))
    # make sure the last line is included in the seating list
    if (line.find("\n") == -1):
        startingSeating.append(tuple(row))
    row = []

f.close()

# set the originalSeating variable to a tuple version of the startingSeating
originalSeating = tuple(startingSeating)

# define a function to check the surrounding seats
def checkSeats(seating, r, c):
    occupiedCount = 0
    # check each direction, stop checking that direction if an edge is reached
    for h, v in directions:
        xh, xv = r+h, c+v
        while (0 <= xh < len(seating)) and (0 <= xv < len(seating[0])):
            if (seating[xh][xv] == '#'):
                occupiedCount += 1
                break
            elif (seating[xh][xv] == 'L'):
                break
            xh += h
            xv += v
    return occupiedCount

# define a function that changes the seating occupancy based on the rules and returns the new seating list
def changeSeating(currentSeating):
    # convert the current seating from a tuple to a list so it can be modified for the new seating
    newSeating = list(currentSeating)
    for i in range(len(newSeating)):
        newSeating[i] = list(newSeating[i])
    # go through every seat in the seating list
    for r in range(len(currentSeating)):
        for c in range(len(currentSeating[r])):
            seat = currentSeating[r][c]
            # pass if the seat is actually the floor
            if (seat == "."):
                pass
            else:
                occupied = checkSeats(currentSeating, r, c)
                # change the occupied state of the seat based on the number of surrounding occupied seats
                if (seat == "L"):
                    if (occupied == 0):
                        newSeating[r][c] = "#"
                else:
                    if (occupied >= 5):
                        newSeating[r][c] = "L"
    return newSeating

# keep running the rules until seats no longer change states
while True:
    changedSeating = changeSeating(originalSeating)
    if (changedSeating == originalSeating):
        break
    originalSeating = changedSeating

# run through every seat and count how many are occupied and then print the total occupied
for a in range(len(changedSeating)):
    for d in range(len(changedSeating[a])):
        if (changedSeating[a][d] == "#"):
            totalOccupied += 1

print(totalOccupied, "seats will end up occupied")
