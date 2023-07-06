# declare given expense list
expenseList = []
# loading a pointer to the file into the variable called f
f = open('input.txt')
# load the list with each line of the file one line at a time
for line in f.readlines():
    expenseList.append(int(line))

f.close()

# declare a boolean to show when the pair of numbers adding to 2020 have been found
nbrsFound = False

# set nbr1 to each value in the list
for i in range(len(expenseList)):
    # check if the pair of numbers adding to 2020 has been found, continue the loop if not, stop it if yes
    if nbrsFound:
        break
    nbr1 = expenseList[i]
    # set nbr2 to each value in the list
    for j in range(len(expenseList)):
        # check if the pair of numbers adding to 2020 has been found, continue the loop if not, stop it if yes
        if nbrsFound:
            break
        nbr2 = expenseList[j]
        # set nbr3 to each value in the list
        for k in range(len(expenseList)):
            nbr3 = expenseList[k]
        # check if the current values of nbr1, nbr2, and nbr3 sum to 2020 and if they do print the numbers,
        # their product, and change nbrsFound to show the numbers have been found
            if nbr1 + nbr2 + nbr3 == 2020:
                nbrsFound = True
                result = nbr1 * nbr2 * nbr3
                print(nbr1, ", ", nbr2, ", and ", nbr3, " have a sum of 2020 and a product of ", result, sep="")
