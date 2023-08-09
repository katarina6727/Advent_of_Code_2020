# initialize variables that will either contain values from the input or be used to put the right 
# input values into the right variables
fields = dict()
mine = False
more = True
myTicket = []
nearby = False
tickets = []

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

# initialize variables that will be used to find the ticket scanning error rate
invalidNbrs = []
errorRate = 0

# define a function that checks if the number is within the field's range
def checkValidity(inNbr, field):
    ranges = fields[field]
    for r in ranges:
        if (int(r[:r.find('-')]) <= inNbr <= int(r[r.find('-')+1:])):
            return True
    return False

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
    for p in t:
        for i in invalidNbrs:
            if (p == i):
                errorRate += p

# print the results
print("The ticket scanning error rate is", errorRate)
