# declare variables
location = 0
trees = 0

# open the file with the map and assign it to f
f = open('map_input.txt')

# move down each line of the slope
for line in f.readlines():
    # check if the location is on a tree and add to the tree counter if so
    if (line[location] == "#"):
        trees += 1
    # move the location 3 to the right and if the location moves past the given slope set the number back 
    # to the start as if the same slope were just repeating infinitely
    location += 3
    if (location > 30):
        location = location - 31

f.close()

# print the number of trees encountered
print("You encountered", trees, "trees on your path")
