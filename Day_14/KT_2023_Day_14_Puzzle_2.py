# initialize variables
masks = {}
mem = []
floatingMems = []
memAddress = 0
memory = {}
sum = 0

# open the file and make each mask the key to the list of values the mask modifies
f = open('initiate_program_input.txt')

for line in f.readlines():
    # when a new mask is reached, add the last mask and its corresponding list before assigning the new mask to the mask variable
    if (line.find('mask') != -1):
        if (mem != []):
            masks[mask] = mem
            mem = []
        mask = line[7:len(line)-1]
    # add the values under the mask to the mem list
    else:
        if (line.find("\n") != -1):
            mem.append((int(line[4:line.find(']')]), int(line[line.find('=')+2:len(line)-1])))
        else:
            mem.append((int(line[4:line.find(']')]), int(line[line.find('=')+2:len(line)])))

# add the last mask and its corresponding list if it wasn't added already
if (mem != []):
    masks[mask] = mem

f.close()

# define a function that converts a binary number to a decimal
def makeDec(bin):
    exponent = 0
    nbr = 0
    # reverse bin so it goes lowest to highest from left to right
    bin = bin[::-1]
    # add each converted bit to the number and then return the final decimal number
    for b in bin:
        nbr += (int(b)*(2**exponent))
        exponent += 1
    return nbr

# define a function that puts all of the memory addresses created by the floating bits into a set
def makeMemSet(address, og):
    index = address.find('X')
    # go through the entire address replacing each floating bit until every possibility has been found and added to the set
    if (index != -1):
        address = address[:index] + '0' + address[index+1:]
        makeMemSet(address, False)
        address = address[:index] + '1' + address[index+1:]
        makeMemSet(address, False)
    else:
        floatingMems.append(address)

# define a function that uses the mask to change the value
def changeAdd(address, mask):
    bitCounter = 0
    addCounter = 0
    # change the decimal value to binary
    binary = format(address, '036b')
    for bit in mask:
        # change each bit in the binary to match the bit in the mask if the mask bit isn't X
        if (bit != '0'):
            binary = binary[:bitCounter] + bit + binary[bitCounter+1:]
        bitCounter += 1
    makeMemSet(binary, True)
    # convert each binary number into a decimal one and then return the list of all of the converted decimal numbers
    for item in floatingMems:
        floatingMems[addCounter] = makeDec(item)
        addCounter += 1
    return floatingMems

# run through every mask's list and go through each of the values in the mask's list
for m, list in masks.items():
    # get the list of memory addresses that will be set to the value and then add each to the memory dictionary
    for i in list:
        memAddress = changeAdd(i[0], m)
        for add in memAddress:
            memory[add] = i[1]
        floatingMems = []

# get the sum of all the values in the memory and then print it
for value in memory.values():
    sum += value

print("The sum of all the values in the memory is", sum)
