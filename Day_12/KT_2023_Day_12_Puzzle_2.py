# initialize variables
navigationDirections = []
quadrant = 0
wayptVertical = 1
wayptHorizontal = 10
verticalPosition = 0
horizontalPosition = 0
degrees = 0
quadProperties = [(1,1), (-1,1), (-1,-1), (1,-1)]

f = open('navigation_input.txt', "r")

# organize the info so the line number is the key and it contains a list with the direction and its corresponding number separated
for line in f.readlines():
    if (line.find("\n") != -1):
        navigationDirections.append((line[0:1], int(line[1:len(line)-1])))
    else:
        navigationDirections.append((line[0:1], int(line[1:len(line)])))

f.close()

# define a function that returns true if a number entered is negative and false if the number is positive (include 0 as positive)
def checkNegative(nbr):
    if (nbr < 0):
        return True
    else:
        return False

# define a function that takes one of the directions and returns it in a form the code can easily use
def followDirections(directions, waypoint):
    action = directions[0]
    value = directions[1]
    # if the directions have an action that moves the waypoint in a predetermined direction, return if it moves 
    # vertically or horizontally and a positive or negative value depending on the direction
    if (action == 'N') or (action == 'S') or (action == 'W') or (action == 'E'):
        if (action == 'N'):
            return value, 'v'
        elif (action == 'S'):
            return -value, 'v'
        elif (action == 'W'):
            return -value, 'h'
        else:
            return value, 'h'
    # if the directions have an action that rotates the waypoint left or right, return a positive value if it 
    # rotates left and negative if it turns right
    elif (action == 'L') or (action == 'R'):
        if (action == 'L'):
            return value, 't'
        else:
            return -value, 't'
    # have the ship keep moving to the waypoint for however many times the value is
    else:
        x, y = waypoint[0] * value, waypoint[1] * value
        return (x, y), 'f'
    
# define a function that rotates the waypoint
def rotateWaypoint(change, ogQuadrant, wayx, wayy):
    # if the change is 180 degrees, find the new quadrant and the waypoint's x and y values and return them right away
    if (abs(change) == 180):
        quad = ogQuadrant + 2
        if (quad > 4):
            quad -= 4
        newWaypt = [-wayx, -wayy]
        return newWaypt[0], newWaypt[1], quad
    # if the change is 90 or 270 degrees, find the new quadrant and switch the x and y values for the new waypoint
    elif (change == 90) or (change == -270):
        quad = ogQuadrant + 1
        newWaypt = [wayy, wayx]
    elif (change == 270) or (change == -90):
        quad = ogQuadrant + 3
        newWaypt = [wayy, wayx]
    if (quad > 4):
        quad -= 4
    # give the new waypoint the negatives and positives that match its quadrant and then return the waypoint's
    # x and y values and the quadrant
    quadProp = quadProperties[quad-1]
    negOrPosx, negOrPosy = checkNegative(quadProp[0]), checkNegative(quadProp[1])
    if (negOrPosx != checkNegative(newWaypt[0])):
        newWaypt[0] = -newWaypt[0]
    if (negOrPosy != checkNegative(newWaypt[1])):
        newWaypt[1] = -newWaypt[1]
    return newWaypt[0], newWaypt[1], quad

# run all of the instructions
for instruction in navigationDirections:
    # call the function to get the value and what will be modified
    value, mod = followDirections(instruction, (wayptHorizontal, wayptVertical))
    # modify the vertical and horizontal positions of the waypoint accordingly
    if (mod == 'v'):
        wayptVertical += value
    elif (mod == 'h'):
        wayptHorizontal += value
    elif (mod == 't'):
        degrees = value
        # determine the quadrant the point is located in
        if (wayptHorizontal >= 0):
            if (wayptVertical >= 0):
                quadrant = 1
            else:
                quadrant = 4
        else:
            if (wayptVertical >= 0):
                quadrant = 2
            else:
                quadrant = 3
        # change the quadrant and waypoint x and y values to match with the rotated waypoint
        wayptHorizontal, wayptVertical, quadrant = rotateWaypoint(degrees, quadrant, wayptHorizontal, wayptVertical)
    # change the location of the ship by adding what was returned by the follow directions function
    else:
        horizontalPosition += value[0]
        verticalPosition += value[1]

# print the result
print("The Manhattan distance between the ship and the starting position is", abs(verticalPosition)+abs(horizontalPosition))
