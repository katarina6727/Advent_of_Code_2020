# import needed modules
import math

# initialize variables
highestSeatID = 0

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
    # calculate the seat ID and then check if that seat ID is higher than the current highest seat ID.
    # If it is, set the highest seat ID to that seat ID
    seatID = row * 8 + col
    if (seatID > highestSeatID):
        highestSeatID = seatID

f.close()

# print the highest seat ID
print("The highest seat ID is", highestSeatID)
