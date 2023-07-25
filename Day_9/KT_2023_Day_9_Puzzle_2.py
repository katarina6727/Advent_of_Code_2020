# initialize variables
encodedNbrsList = []
preamble = []
found = False

# open the file and put all of the encoded input into a list before closing the file
f = open('encoded_input.txt')

for line in f.readlines():
    data = int(line[:len(line)-1])
    encodedNbrsList.append(data)

f.close()

# fill the preamble with the starting 25 numbers
for b in range(25):
    preamble.append(encodedNbrsList[b])
# set encodedNbrs to be the encodedNbrsList but without the 25 numbers that went into the preamble
encodedNbrs = encodedNbrsList[25:]

# define a function to make the preamble only encompass the past 25 numbers and return the updated preamble
def editPreamble(index):
    preamble.pop(0)
    preamble.append(encodedNbrs[index])

# define a function to fill and return a set with all of the sums of two different numbers in the preamble
def findValidNbrs():
    validNbrsSet = set()
    for nbr1 in preamble:
        for nbr2 in preamble:
            if (nbr1 != nbr2):
                validNbrsSet.add(nbr1+nbr2)
    return validNbrsSet

# run through all the encoded numbers until an invalid number is found
for i in range(len(encodedNbrs)):
    # assign nbr to the current number being tested for its validity and reset the valid boolean and 
    # reassign the validNbrs set with the changed preamble
    nbr = encodedNbrs[i]
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
        invalidNbr = nbr
        print("The number", invalidNbr, "at index", i+25, "is invalid")
        break

# define a function that adds another number to the sum and returns the new sum
def addTogether(sum, index, nbrList):
    newSum = sum + nbrList[index]
    return newSum

# run through the encodedNbrsList, using each number as the starting number until the right sum is found
for l in range(len(encodedNbrsList)):
    if found:
        break
    # if the end of the list is reached without finding the correct sum, print that the end is reached and break the loop
    if (l == len(encodedNbrsList)-1):
        print("End reached")
        break
    # set the beginning of the addendsList, starting sum, and the list of numbers left to run through
    addendsList = [encodedNbrsList[l], encodedNbrsList[l+1]]
    sum = encodedNbrsList[l] + encodedNbrsList[l+1]
    nbrsAfter = encodedNbrsList[l+2:]
    # run through the remaining numbers until the sum equals or is greater than the invalid number
    for index in range(len(nbrsAfter)):
        if (sum >= invalidNbr):
            # if the sum is equal to the invalid number, set found to true, find the largest and smallest 
            # number in the addends list, and break the loop
            if (sum == invalidNbr):
                found = True
                smallestNbr = min(addendsList)
                largestNbr = max(addendsList)
                print("The correct sum", sum, "has been found", sep=", ")
                break
            break
        # if the sum is less than the invalid number continue by adding another number to the sum and 
        # add the next number to the addendsList
        else:
            sum = addTogether(sum, index, nbrsAfter)
            addendsList.append(nbrsAfter[index])

if found:
    # print the results
    print("The smallest number in this range is", smallestNbr, "and the largest number is", largestNbr)
    print("The encryption weakness is", smallestNbr+largestNbr)
