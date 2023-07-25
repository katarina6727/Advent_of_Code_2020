# initialize variables
adaptersList = []
oneJoltDifs = 0
threeJoltDifs = 0
adapter = 0
counter = 0

# open the file and put all of the adapters input into a list before closing the file
f = open('adapters_input.txt')

for line in f.readlines():
    if (line.find("\n") != -1):
        data = int(line[:len(line)-1])
    else:
        data = int(line)
    adaptersList.append(data)

f.close()

# add my device's adapter to the adapter list
adaptersList.append(max(adaptersList)+3)

# define a function to find the next available adapter
def findNextAdapter(currentAdapter):
    oneAway = -1
    twoAway = -1
    threeAway = -1
    # check each adapter and set it to its corresponding variable if it is in the correct range
    for a in adaptersList:
        if (a-1 == currentAdapter):
            oneAway = a
        elif (a-2 == currentAdapter):
            twoAway = a
        elif (a-3 == currentAdapter):
            threeAway = a
    # return the adapter closest to the current adapter and how far away it was
    if (oneAway != -1):
        return oneAway, 1
    elif (twoAway != -1):
        return twoAway, 2
    elif (threeAway != -1):
        return threeAway, 3

# repeat the loop until the last adapter has been reached
while (adapter != max(adaptersList)):
    counter += 1
    # set adapter and jolts to the findNextAdapter function's returned values
    adapter, jolts = findNextAdapter(adapter)
    # if the jolts are one or three away from the last adapter, add one to the corresponding counter
    if (jolts == 1):
        oneJoltDifs += 1
    elif (jolts == 3):
        threeJoltDifs += 1

# print the result
print("The product of one jolt differences multiplied by three jolt differences is", oneJoltDifs*threeJoltDifs)
