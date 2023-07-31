# initialize variables
navigationDirections = []
verticalPosition = 0
horizontalPosition = 0
degrees = 0
face = 'east'

f = open('navigation_input.txt', "r")

# organize the info so the line number is the key and it contains a list with the direction and its corresponding number separated
for line in f.readlines():
    if (line.find("\n") != -1):
        navigationDirections.append((line[0:1], int(line[1:len(line)-1])))
    else:
        navigationDirections.append((line[0:1], int(line[1:len(line)])))

f.close()

# define a function that takes one of the directions and returns it in a form the code can easily use
def followDirections(directions, facing):
    action = directions[0]
    value = directions[1]
    # if the directions have an action that moves the ship in a predetermined direction, return if it moves 
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
    # if the directions have an action that turns the ship left or right, return a positive value if it turns 
    # left and negative if it turns right
    elif (action == 'L') or (action == 'R'):
        if (action == 'L'):
            return value, 't'
        else:
            return -value, 't'
    # the directions are having the ship move forward, so return if the ship moved horizontally or vertically 
    # and how much that way it moved
    else:
        if (facing == 'north'):
            return value, 'v'
        elif (facing == 'south'):
            return -value, 'v'
        elif (facing == 'west'):
            return -value, 'h'
        else:
            return value, 'h'

# run all of the instructions
for instruction in navigationDirections:
    # call the function to get the value and what will be modified
    value, mod = followDirections(instruction, face)
    # modify the vertical and horizontal positions accordingly
    if (mod == 'v'):
        verticalPosition += value
    elif (mod == 'h'):
        horizontalPosition += value
    else:
        # keep the degrees within the 360 degrees from 0
        degrees += value
        if (degrees >= 360):
            degrees -= 360
        if (degrees <= -360):
            degrees += 360
        # set the face to correspond with the degrees
        if (degrees == 0):
            face = 'east'
        elif (degrees == 90) or (degrees == -270):
            face = 'north'
        elif (degrees == 180) or (degrees == -180):
            face = 'west'
        else:
            face = 'south'

# print the result
print("The Manhattan distance between te ship and the starting position is", abs(verticalPosition)+abs(horizontalPosition))
