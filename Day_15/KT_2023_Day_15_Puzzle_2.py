# initialize variables
nbrsSpoken = []
turnNbr = 0
newNbr = 0
last = 0

# open the input file and set line to be the string of starting numbers in the file
f = open('memory_nbrs_input.txt', 'r')

line = f.readline()
# organize the starting numbers into the nbrsSpoken list as separate lists with the number first and then the turn
while (len(line) != 0):
    turnNbr += 1
    index = line.find(',')
    if (index != -1):
        nbrsSpoken.append([int(line[:index]), turnNbr])
        line = line[index+1:]
    # if it's the last number in the given starting numbers, subtract one from the turnNbr, set the last number to the starting number, and empty the line variable
    else:
        turnNbr -= 1
        startNbr = int(line)
        line = ""

f.close()

# define a function that returns the next number that you should speak to follow the sequence
def nextNbr(lastNbr, turn):
    nextNbr = 0
    # check if the last number is repeated, if so determine the next number based on the turn and the last turn the number was said on
    for i in range(len(nbrsSpoken)):
        if (nbrsSpoken[i][0] == lastNbr):
            nextNbr = turn - nbrsSpoken[i][1]
            # change the most recent mention of the number to the current turn and return the next number to be spoken
            nbrsSpoken[i][1] = turn
            return nextNbr
    # if the number is repeated add it and its corresponding turn to the list and return 0
    nbrsSpoken.append([lastNbr, turn])
    return 0

# set newNbr to the last starting number to be compatible with the loop
newNbr = startNbr

# keep looping the game until the 30000000 number has been assigned to newNbr
while (turnNbr != 29999999):
    turnNbr += 1
    last = newNbr
    newNbr = nextNbr(last, turnNbr)
    print(turnNbr)

# print the result
print("The 30000000th number spoken will be", newNbr)
