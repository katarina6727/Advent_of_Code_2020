# initialize variables
masks = {}
mem = []
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

# define a function that uses the mask to change the value
def changeVal(value, mask):
    counter = 0
    # change the decimal value to binary
    binary = format(value, '036b')
    for bit in mask:
        # change each bit in the binary to match the bit in the mask if the mask bit isn't X
        if (bit != 'X'):
            binary = binary[:counter] + bit + binary[counter+1:]
        counter += 1
    return makeDec(binary)
    
# run through every mask's list and go through each of the values in the mask's list
for m, list in masks.items():
    # change the memory slot to be the changed value
    for i in list:
        memory[i[0]] = changeVal(i[1], m)

# get the sum of all the values in the memory and then print it
for value in memory.values():
    sum += value

print("The sum of all the values in the memory is", sum)