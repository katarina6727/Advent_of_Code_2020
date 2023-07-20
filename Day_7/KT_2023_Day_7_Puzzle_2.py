# initialize variables
bagContentsDict = {}
bagCount = 0
t = 0

# open the file with all of the customs forms information and assign it to f
f = open('bag_input.txt')

# organize original input into a dictionary
for line in f.readlines():
    # reset the inner bags dictionary and then set the original bag and inner bags
    innerBagsDict = {}
    startingBag = line[:line.find("bags")-1]
    innerBags = line[line.find("contain")+8:]
    innerBags = innerBags.replace(" bags", "").replace(" bag", "").replace(".\n", "")
    # add to the inner bags dictionary until all inner bags have been added
    while (len(innerBags) != 0):
        # if there are no other bags, put that in the dictionary and break the loop
        if (innerBags.find("no other") != -1):
            innerBagsDict[innerBags] = 0
            break
        # add the inner bag to the dictionary until there are no more bags to add
        if (innerBags.find(",") != -1):
            innerBagsDict[innerBags[2:innerBags.find(",")]] = int(innerBags[:1])
            innerBags = innerBags[innerBags.find(",")+2:]
        else:
            innerBagsDict[innerBags[2:]] = int(innerBags[:1])
            innerBags = ""
    # set the bag contents dictionary using the original bag and the inner bags dictionary
    bagContentsDict[startingBag] = innerBagsDict

f.close()

# create a function that has the current bag and factor as parameters
def countBags(bag, factor):
    bagCount = 0
    containedBags = bagContentsDict[bag]
    # loop through all the items in the contained bags dictionary, set the bag color to b and number of bags to n
    # and keep looping and counting bags until all contained bags are counted
    for b, n in containedBags.items():
        if (b != 'no other'):
            bags = countBags(b, factor*n)
            bagCount += bags + factor * n
    return bagCount

# print the final result
print(countBags('shiny gold', 1), "bags are required to be in my shiny gold bag")
