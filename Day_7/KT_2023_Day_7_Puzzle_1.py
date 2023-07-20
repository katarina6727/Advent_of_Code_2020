# initialize variables
bagList = []
uncheckedInsideBagsSet = set()
multipleBags = False
shinyFound = False
shinyGoldBags = 0

# open the file with all of the customs forms information and assign it to f
f = open('bag_input.txt')

# add each line to bagList
for line in f.readlines():
    bagList.append(line)

f.close()

for i in bagList:
    # find the index for the original color
    index = i.find("bags")-1
    # check that there are bags inside the current bag and if so, find the index of the bag or
    # bags. If it's more than one bag, change the multipleBags variable to true
    if (i.find("no other") == -1):
        i = i[index+16:]
        while (index != -1):
            index = i.find("bag")
            # if there are more bags to add to the list, add them and then set i, based on if it is 1 or 
            # more bags, to not include the bag just added to the list.
            if (index != -1):
                if (i[index+3] == "s"):
                    multipleBags = True
                newBag = i[:index-1]
                # check if the new bag is shiny gold, and if so stop iterating the loop and add 1 to the shiny gold counter
                if (newBag == "shiny gold"):
                    shinyGoldBags += 1
                    shinyFound = True
                    uncheckedInsideBagsSet = set()
                    break
                uncheckedInsideBagsSet.add(newBag)
                if multipleBags:
                    i = i[index+8:]
                else:
                    i = i[index+7:]
            # reset multipleBags variable
            multipleBags = False
    # if the shiny gold bag has not yet been found, iterate through all the inner bags until it is found or there are no more bags
    if not shinyFound:
        while (len(uncheckedInsideBagsSet) != 0):
            # if the shiny has been found reset the unchecked bags set and break the loop
            if shinyFound:
                uncheckedInsideBagsSet = set()
                break
            # set one of the unchecked bags in the set to current bag to be checked
            for c in uncheckedInsideBagsSet:
                currentBag = c
                break
            # go through the bag list and find the current bag and what it contains
            for j in bagList:
                index = j.find(currentBag)
                if (index == 0):
                    # check that there are bags inside the current bag and if so, find the index of the
                    # bag or bags. If it's more than one bag, set the multipleBags varible to true
                    if (j.find("no other") == -1):
                        index = j.find("bags")
                        j = j[index+15:]
                        while (index != -1):
                            index = j.find("bag")
                            # if there are more bags to add to the list, add them and then set i, based on 
                            # if it is 1 or more bags, to not include the bag just added to the list.
                            if (index != -1):
                                if (j[index+3] == "s"):
                                    multipleBags = True
                                newBag = j[:index-1]
                                # what
                                if (newBag == "shiny gold"):
                                    shinyGoldBags += 1
                                    shinyFound = True
                                    break
                                uncheckedInsideBagsSet.add(newBag)
                                if multipleBags:
                                    j = j[index+8:]
                                else:
                                    j = j[index+7:]
                            # reset the multipleBags variable
                            multipleBags = False
            # remove the bag that was just checked
            uncheckedInsideBagsSet.remove(currentBag)
    # reset shinyFound to false
    shinyFound = False

print(shinyGoldBags, "bags can eventually contain at least 1 shiny gold bag")
