# initialize varibles
counter = -1
busTimes = []
startValue = 100000000000009
end = False

f = open('bus_input.txt', 'r')

# add all the bus times to a list and include the bus ID and the bus's order in the bus list
for line in f.readlines():
    if (line.find("\n") != -1):
        pass
    else:
        givenBuses = line.split(",")
        for item in givenBuses:
            counter += 1
            if (item != 'x'):
                busTimes.append([int(item), counter])
                counter = 0

f.close()

# define a function that checks if the given value in the list is in the right offset
def checkPos(bus, offset, previous, found):
    endReached = False
    value = previous
    # repeat until a value is returned
    while True:
        # return true if all the values are at the right offset and return false as soon as one value is found at the wrong offset
        if endReached:
            return True
        if not found:
            return False
        # check the previous value and those ahead of it until one that works with the bus's timing comes up
        while True:
            if (value % bus != 0):
                value += 1
            else:
                break
        # return that this value doesn't end up with the correct offsets if it ends up having a greater value than the required offset
        if (value > previous+offset):
            return False
        # if the value is less than the required offset, start over the loop to find the next value in the bus's timings
        elif (value < previous+offset):
            value += 1
        else:
            for item in range(len(busTimes)):
                # find the current bus in the bus times list and check if it's the last bus in the list. If it is, return true 
                # as the value with the correct offsets has been found
                if (busTimes[item][0] == bus):
                    if (item+1 == len(busTimes)):
                        return True
                    else:
                        # run the function for all of the busses in the list. If the correct value is found set endReached to 
                        # true so the function can stop running 
                        found = checkPos(busTimes[item+1][0], busTimes[item+1][1], value, found)
                        if found:
                            endReached = True
                        break

# check all the possibilites until the correct one is found
while not end:
    startValue += busTimes[0][0]
    end = checkPos(busTimes[1][0], busTimes[1][1], startValue, True)

# print the result
print("The earliest timestamp where all the buses depart at their listed offset is", startValue)
