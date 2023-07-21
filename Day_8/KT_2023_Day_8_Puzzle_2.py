# initialize variables
bootCode = []

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

f.close()

def runAndMod(bootup):
    # go through every line of bootup code and call the runUntilRepeat function if a jmp or nop is found
    for index in range(len(bootup)):
        changedCode = bootup[index]
        if (changedCode[0] != "acc"):
            print("found jmp or nop at address:", index)
            result = runUntilRepeat(bootup, index, changedCode)
            # if the result says the loop was completed correctly, stop the loop and print the correct accumulator
            if (result[0] == "completed"):
                print("found corrupted line, correct accumulator is", result[1])
                break
            # if the result shows the bootup code repeated, show that the wrong line was changed and repeat the loop
            else:
                print("changed wrong line.")


def runUntilRepeat(bootup, index, newCode):
    # initializie variables
    modifiedCode = list(bootup)
    codeRun = []
    counter = 0
    acc = 0
    # modify a single line to switch its jmp to nop or nop to jmp
    if (newCode[0] == "jmp"):
        modifiedCode[index] = ["nop", newCode[1]]
    else:
        modifiedCode[index] = ["jmp", newCode[1]]
    # repeat the code until the counter reaches the last line of the bootup code
    while (counter != len(modifiedCode)):
        codeLine = modifiedCode[counter]
        # check if a line of code has been revisited and return that the code has repeated if so
        for item in codeRun:
            if (item == counter):
                return ["repeated"]
        codeRun.append(counter)
        # determine and perform the operation in the line of code
        if (codeLine[0] == "acc"):
            acc += codeLine[1]
            counter += 1
        elif (codeLine[0] == "jmp"):
            counter += codeLine[1]
        else:
            counter += 1
    # return that the bootup code worked correctly and the accumulator
    return ["completed", acc]

runAndMod(bootCode)
