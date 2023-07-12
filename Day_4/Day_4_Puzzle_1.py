# initialize variables
passportData = ""
dataList = []
validPassports = 0
valid = True

# open the file with all of the passport information and assign it to f
f = open('passport_input.txt')


for line in f.readlines():
    # keep adding the same passport data to the passportData variable until there is a line break indicating the following data would
    # be for a different passport
    if (line != "\n"):
        passportData = passportData + line
    if (line == "\n"):
        # if there are any separate lines in the passport data, replace them with a space
        if (passportData.index("\n") != -1):
            passportData = passportData.replace("\n", " ")
        # separate each piece of data in a list by finding the spaces between pieces of data
        while (passportData.find(" ") != -1):
            index = passportData.find(" ")
            dataList.append(passportData[:index])
            passportData = passportData[index+1:]
        # add to the valid passport count if a passport has all 8 required fields
        length = len(dataList)
        if (length > 7):
            validPassports += 1
        # if the passport only has 7 of the 8 required fields determine if the missing field is the country ID. If it is, add to the
        # valid passport count
        elif (length == 7):
            for i in range(7):
                dataPiece = dataList[i]
                if (dataPiece.find("cid") != -1):
                    valid = False
            if valid:
                validPassports += 1

        # reset the current passport's data, data list, and valid variable for the next passport
        valid = True
        passportData = ""
        dataList = []
        
f.close()

# print the total number of valid passports
print("There are", validPassports, "valid passports")
