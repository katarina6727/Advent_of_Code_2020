# declare location and tree counter variables for each of the 5 slopes and a single counter variable
location1 = 0
location2 = 0
location3 = 0
location4 = 0
location5 = 0
treesPath1 = 0
treesPath2 = 0
treesPath3 = 0
treesPath4 = 0
treesPath5 = 0
counter = 0

# open the file with the map and assign it to f
f = open('map_input.txt')

# move down each line of the slope
for line in f.readlines():
    # SLOPE 1 - right 1, down 1
    # check if the location is on a tree, add to the tree counter if so. Then move the location 1 to the right
    # and if the location moves past the limits of the string return the location to the beginning of the string
    if (line[location1] == "#"):
        treesPath1 += 1
    location1 += 1
    if (location1 > 30):
        location1 = location1 - 31
    
    # SLOPE 2 - right 3, down 1
    # check if the location is on a tree and add to the tree counter if so
    if (line[location2] == "#"):
        treesPath2 += 1
    # move the location 3 to the right and if the location moves past the given slope set the number back 
    # to the start as if the same slope were just repeating infinitely
    location2 += 3
    if (location2 > 30):
        location2 = location2 - 31

    # SLOPE 3 - right 5, down 1
    # check if the location is on a tree, add to the tree counter if so. Then move the location 5 to the right
    # and if the location moves past the limits of the string return the location to the beginning of the string
    if (line[location3] == "#"):
        treesPath3 += 1
    location3 += 5
    if (location3 > 30):
        location3 = location3 - 31

    # SLOPE 4 - right 7, down 1
    # check if the location is on a tree, add to the tree counter if so. Then move the location 7 to the right
    # and if the location moves past the limits of the string return the location to the beginning of the string
    if (line[location4] == "#"):
        treesPath4 += 1
    location4 += 7
    if (location4 > 30):
        location4 = location4 - 31

    # SLOPE 5 - right 1, down 2
    # check counter so slope moves down 2 and then check if the location is on a tree and add to tree counter if
    # so. Then move the location 1 to the right and move the location back to the beginning of the string if it
    # goes past the limits of the string
    if (counter % 2 == 0):
        if (line[location5] == "#"):
            treesPath5 += 1
        location5 += 1
        if (location5 > 30):
            location5 = location5 - 31
    counter += 1

f.close()

# print the product of all the trees encountered on all 5 slopes
print("The product of all the trees hit on the different paths is", treesPath1*treesPath2*treesPath3*treesPath4*treesPath5)
