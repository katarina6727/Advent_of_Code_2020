# import needed modules
import math

# initialize variables
occupiedSeatsList = []
free = True
occupiedSeats = 0
yourSeat = -1

# open the file with all of the seating information and assign it to f
f = open('seat_input.txt')

for line in f.readlines():
    # assign variables with starting values
    binaryRow = line[:7]
    binaryCol = line[7:10]
    botRow = 0
    topRow = 127
    leftCol = 0
    rightCol = 7
    # half the possible rows for each letter in the sequence and then set the row to the row the 
    # sequence ends on
    for i in binaryRow:
        if (i == "F"):
            topRow = math.floor(topRow - (topRow-botRow)/2)
        else:
            botRow = math.ceil(botRow + (topRow-botRow)/2)
    row = botRow
    # half the possible columns for each letter in the sequence and then set the final column to the
    # column the sequence ends on
    for j in binaryCol:
        if (j == "L"):
            rightCol = math.floor(rightCol - (rightCol-leftCol)/2)
        else:
            leftCol = math.ceil(leftCol + (rightCol-leftCol)/2)
    col = leftCol
    # calculate the seat ID and then add it to the list of occupied seats
    seatID = row * 8 + col
    occupiedSeatsList.append(seatID)
    
f.close()

# check every possible seat ID to see if it is your seat
for k in range(1024):
    # if the possible seat ID, k, is occupied, stop checking seat IDs, set the seat as not being free
    # and finish the iteration of the loop to check the next possible seat ID.
    for s in occupiedSeatsList:
        if (s == k):
            free = False
            break
    if free:
        # check if the seats next to the potential seat ID are occupied or not. If they are, set that 
        # as your seat ID and stop the loop from checking any other seat IDs
        for l in occupiedSeatsList:
            if (l == (k-1)):
                occupiedSeats += 1
            if (l == (k+1)):
                occupiedSeats += 1
        if (occupiedSeats == 2):
            yourSeat = k
            break
    # reset the variables for the next potential seat ID
    free = True
    occupiedSeats = 0

# print the your seat ID
print("Your seat ID is", yourSeat)
