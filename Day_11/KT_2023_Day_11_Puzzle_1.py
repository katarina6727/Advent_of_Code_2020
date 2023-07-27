# initialize variables
startingSeating = []
originalSeating = []
changedSeating = []
row = []
totalOccupied = 0

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

# check if the seat is at an edge or corner and check the surrounding seats accordingly
def checkSurroundingSeats(currentSeats, row, col):
    occupiedSeats = 0
    seatsToCheck = []
    # check if the seat is on the top edge
    if (row == 0):
        # check if the seat is in the top left or right corner
        if (col == 0):
            seatsToCheck = [currentSeats[row][col+1], currentSeats[row+1][col], currentSeats[row+1][col+1]]
        elif (col == len(currentSeats[row])-1):
            seatsToCheck = [currentSeats[row][col-1], currentSeats[row+1][col], currentSeats[row+1][col-1]]
        else:
            seatsToCheck = [currentSeats[row][col-1], currentSeats[row][col+1], currentSeats[row+1][col-1], currentSeats[row+1][col], currentSeats[row+1][col+1]]
    # check if the seat is on the bottom edge
    elif (row == len(currentSeats)-1):
        # check if the seat is in the bottom left or right corner
        if (col == 0):
            seatsToCheck = [currentSeats[row][col+1], currentSeats[row-1][col], currentSeats[row-1][col+1]]
        elif (col == len(currentSeats[row])-1):
            seatsToCheck = [currentSeats[row][col-1], currentSeats[row-1][col], currentSeats[row-1][col-1]]
        else:
            seatsToCheck = [currentSeats[row][col-1], currentSeats[row][col+1], currentSeats[row-1][col-1], currentSeats[row-1][col], currentSeats[row-1][col+1]]
    # check if the seat is on the left edge
    elif (col == 0):
        seatsToCheck = [currentSeats[row-1][col], currentSeats[row-1][col+1], currentSeats[row][col+1], currentSeats[row+1][col], currentSeats[row+1][col+1]]
    # check if the seat is on the right edge
    elif (col == len(currentSeats[row])-1):
        seatsToCheck = [currentSeats[row-1][col-1], currentSeats[row-1][col], currentSeats[row][col-1], currentSeats[row+1][col-1], currentSeats[row+1][col]]
    # seat is completely surrounded so check all surrounding 8 seats
    else:
        seatsToCheck = [currentSeats[row-1][col-1], currentSeats[row-1][col], currentSeats[row-1][col+1], currentSeats[row][col-1], currentSeats[row][col+1], currentSeats[row+1][col-1], currentSeats[row+1][col], currentSeats[row+1][col+1]]
    # check all required seats, count how many are occupied, and return the final number of occupied seats
    for s in seatsToCheck:
        if (s == "#"):
            occupiedSeats += 1
    return occupiedSeats

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
                occupied = checkSurroundingSeats(currentSeating, r, c)
                # change the occupied state of the seat based on the number of surrounding occupied seats
                if (seat == "L"):
                    if (occupied == 0):
                        newSeating[r][c] = "#"
                else:
                    if (occupied >= 4):
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
    for b in range(len(changedSeating[a])):
        if (changedSeating[a][b] == "#"):
            totalOccupied += 1

print(totalOccupied, "seats will end up occupied")
