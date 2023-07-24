# initialize variables
encodedNbrsList = []
preamble = []

# open the file and put all of the encoded input into a list before closing the file
f = open('encoded_input.txt')

for line in f.readlines():
    data = int(line[:len(line)-1])
    encodedNbrsList.append(data)

f.close()

# fill the preamble with the starting 25 numbers
for b in range(25):
    preamble.append(encodedNbrsList[b])
# change encodedNbrsList so it doesn't include the 25 numbers that went into the preamble
encodedNbrsList = encodedNbrsList[25:]

# define a function to make the preamble only encompass the past 25 numbers and return the updated preamble
def editPreamble(index):
    preamble.pop(0)
    preamble.append(encodedNbrsList[index])

# define a function to fill and return a set with all of the sums of two different numbers in the preamble
def findValidNbrs():
    validNbrsSet = set()
    for nbr1 in preamble:
        for nbr2 in preamble:
            if (nbr1 != nbr2):
                validNbrsSet.add(nbr1+nbr2)
    return validNbrsSet

# run through all the encoded numbers until an invalid number is found
for i in range(len(encodedNbrsList)):
    # assign nbr to the current number being tested for its validity and reset the valid boolean and 
    # reassign the validNbrs set with the changed preamble
    nbr = encodedNbrsList[i]
    valid = False
    validNbrs = findValidNbrs()
    # check if the nbr is one of the valid numbers
    for n in validNbrs:
        if (nbr == n):
            valid = True
            break
    # if the number was valid, change what the preamble encompasses in preparation for checking the next number
    if valid:
        editPreamble(i)
    # if the number was not valid, print the number and its index and then stop the loop
    else:
        print("The number", nbr, "at index", i, "is invalid")
        break

