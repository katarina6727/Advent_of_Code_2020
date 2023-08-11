# initialize variables that will either contain values from the input or be used to put the right 
# input values into the right variables
fields = dict()
mine = False
more = True
myTicket = []
nearby = False
tickets = []
validTickets = []

# open the file and separate the data
f = open('ticket_input.txt')

for line in f.readlines():
    index = line.find(": ")
    # separate all of the ranges for each field into a dictionary
    if (index != -1):
        fieldName = line[:index]
        line = line[index+2:]
        fields[fieldName] = [line[:line.find("or")-1], line[line.find("or")+3:len(line)-1]]
    # set myTicket to the ticket given in the file input
    if mine:
        while more:
            if (line.find(",") != -1):
                myTicket.append(int(line[:line.find(",")]))
                line = line[line.find(",")+1:]
            else:
                myTicket.append(int(line[:-1]))
                more = False
        mine = False
    # signal that the next line will be my ticket
    if (line.find("your ticket") != -1):
        mine = True
    # put all of the tickets into the ticket list
    if nearby:
        more = True
        curTicket = []
        while more:
            # add the numbers from each field into a list and then add that list to the tickets list
            if (line.find(",") != -1):
                curTicket.append(int(line[:line.find(",")]))
                line = line[line.find(",")+1:]
            elif (line.find("\n") != -1):
                curTicket.append(int(line[:-1]))
                more = False
            else:
                curTicket.append(int(line))
                more = False
        tickets.append(curTicket)
        # signal that the rest of the lines will be the nearby tickets
    if (line.find("nearby tickets") != -1):
        nearby = True

# set valid tickets to be all of the current tickets but do this weird tuple conversion and then list conversion thing so the tickets variable doesn't decide to connect to the validTickets for some reason
validTickets = tuple(tickets)
validTickets = list(validTickets)

# define a function that checks if the number is within the field's range
def checkValidity(inNbr, field):
    ranges = fields[field]
    for r in ranges:
        if (int(r[:r.find('-')]) <= inNbr <= int(r[r.find('-')+1:])):
            return True
    return False

# define a function that finds all the tickets with invalid numbers and removes them from the list
def removeInvalids():
    invalidNbrs = []
    # go through every possible number and add it to the invalid numbers list if it's invalid for every field
    for nbr in range(999):
        nbr += 1
        valid = False
        for k in fields.keys():
            valid = checkValidity(nbr, k)
            if valid:
                break
        if not valid:
            invalidNbrs.append(nbr)
    
    # go through all the tickets and check if any of their numbers are on the invalid list
    for t in tickets:
        remove = False
        for p in t:
            for i in invalidNbrs:
                if (p == i):
                    validTickets.remove(t)
                    remove = True
                    break
            if remove:
                break

removeInvalids()

# initialize variables needed for finding the order of the fields and answer
fieldOrder = dict()
for key in fields.keys():
    fieldOrder[key] = set()
product = 1
finalOrder = dict()

# determine which fields would be valid for which columns
for col in range(20):
    for field in fields.keys():
        for ticket in validTickets:
            works = checkValidity(ticket[col], field)
            if not works:
                break
        # add this column to the list of fields that could possibly work for that column
        if works:
            posList = fieldOrder[field]
            posList.add(col)
            fieldOrder[field] = posList

# order the fields by the length of their possible lists 
for field in sorted(fieldOrder, key=lambda l: len(fieldOrder[l])):
    for p in fieldOrder[field]:
        # if the possible column isn't already taken, assign it to that field
        if p not in finalOrder.values():
            finalOrder[field] = p
            # if the field is departure, multiply its value in my ticket to the current product
            if (field.find('departure') != -1):
                product *= myTicket[p]
            break

# print the product
print("The product of departure fields on my ticket is", product)
