# initialize varibles
earliest = 0
busTimes = []
posBus = []
bestTime = 0
bestBus = 0

f = open('bus_input.txt', 'r')

# assign a variable the earliest time you can get on a bus and add all the bus times to a list
for line in f.readlines():
    if (line.find("\n") != -1):
        earliest = int(line[:len(line)-1])
    else:
        givenBuses = line.split(",")
        for item in givenBuses:
            if (item != 'x'):
                busTimes.append([int(item), 0])

f.close()

# go through each bus, find what time would be the earliest they would arrive when you could get on them, and
# add them time with the busID to a list
for time in busTimes:
    while True:
        current = time[1]
        if (current >= earliest):
            posBus.append((current, time[0]))
            break
        else:
            time[1] += time[0]

# go through each of the buses best possible times and assign a variable the best time and another variable 
# the corresponding bus ID for that best time
for pos in posBus:
    if (bestTime == 0):
        bestTime = pos[0]
        bestBus = pos[1]
    elif (bestTime > pos[0]):
        bestTime = pos[0]
        bestBus = pos[1]

# multiply the best bus's ID by the number of minutes that you will have to wait and print the result
print("The best bus to take is", bestBus, "as you will only have to wait", bestTime-earliest, "minutes for it. If you multiply the best bus's ID and the waiting time you get", bestBus * (bestTime - earliest))
