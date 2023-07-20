# initialize variables
bootCode = []
codeRun = []
repeat = False
acc = 0
counter = 0

# open the file with the boot up code
f = open('boot_code_input.txt')

# organize each line of code into the bootCode list
for line in f.readlines():
    # separate the number part of the line, including the negative symbol but not the positive symbol
    if (line.find("\n") != -1):
        if (line.find("-") != -1):
            nbr = int(line[4:len(line)-1])
        else:
            nbr = int(line[5:len(line)-1])
    else:
        if (line.find("-") != -1):
            nbr = int(line[4:len(line)])
        else:
            nbr = int(line[5:len(line)])
    # add a list to the bootCode list that includes the operation and the corresponding number
    bootCode.append([line[:3], nbr])

# repeat the code until a line is repeated
while not repeat:
    codeLine = bootCode[counter]
    # check if a line of code has been revisited and set repeat to true if so
    for item in codeRun:
        if (item == counter):
            repeat = True
    codeRun.append(counter)
    # determine and perform the operation in the line of code
    if not repeat:
        if (codeLine[0] == "acc"):
            acc += codeLine[1]
            counter += 1
        elif (codeLine[0] == "jmp"):
            counter += codeLine[1]
        else:
            counter += 1

# print the result
print("The accumulator value before the code repeats is", acc)

