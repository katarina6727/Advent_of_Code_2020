# initialize variables
passportData = ""
dataList = []
validPassports = 0
validFieldsCount = 0

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
        # go through each piece of data provided in the passport
        for i in dataList:
            # separate the data field and the corresponding data
            dataField = i[:3]
            data = i[4:]
            # find which field the data corresponds to and check if it is valid based on that field's constraints
            if (dataField == "byr"):
                # change the data to the int data type and count it as valid if the data is between 1920 and 2002
                data = int(data)
                if (data >= 1920) and (data <= 2002):
                    validFieldsCount += 1
            elif (dataField == "iyr"):
                # change the data to the int data type and count it as valid if the data is between 2010 and 2020
                data = int(data)
                if (data >= 2010) and (data <= 2020):
                    validFieldsCount += 1
            elif (dataField == "eyr"):
                # change the data to the int data type and count it as valid if the data is between 2020 and 2030
                data = int(data)
                if (data >= 2020) and (data <= 2030):
                    validFieldsCount += 1
            elif (dataField == "hgt"):
                # see if the data is in centimeters or inches and determine if it is valid based on the
                # constraints that go with that measurement type
                if (data.find("cm") != -1):
                    data = int(data[:data.find("cm")])
                    if (data >= 150) and (data <= 193):
                        validFieldsCount += 1
                elif (data.find("in") != -1):
                    data = int(data[:data.find("in")])
                    if (data >= 59) and (data <= 76):
                        validFieldsCount += 1
            elif (dataField == "hcl"):
                validCharacters = 0
                # check if the data starts with a # and remove it from the data string before continuing 
                # to check other parts of the data
                if (data[0] == "#"):
                    data = data[1:]
                    # check if there are exactly 6 characters in the data before continuing
                    if (len(data) == 6):
                        for j in data:
                            # determine if the character is a number or letter and then check if it fits
                            # into the constraints for its type. If it does, count it as a valid character
                            if (j.isdigit()):
                                j = int(j)
                                if (j >= 0) and (j <= 9):
                                    validCharacters += 1
                            elif (j.isalpha()):
                                if (j >= 'a') and (j <= 'f'):
                                    validCharacters += 1
                        # if all the characters are valid, count the field as valid
                        if (validCharacters == 6):
                            validFieldsCount += 1
            elif (dataField == "ecl"):
                # check if the data matches one of valid values and count it as a valid field if so
                if (data == "amb"):
                    validFieldsCount += 1
                elif (data == "blu"):
                    validFieldsCount += 1
                elif (data == "brn"):
                    validFieldsCount += 1
                elif (data == "gry"):
                    validFieldsCount += 1
                elif (data == "grn"):
                    validFieldsCount += 1
                elif (data == "hzl"):
                    validFieldsCount += 1
                elif (data == "oth"):
                    validFieldsCount += 1
            elif (dataField == "pid"):
                # check if the passport id is a number and is the correct number of digits and add it
                # to the count of valid fields if so
                if (len(data) == 9) and (data.isdigit()):
                    validFieldsCount += 1
        
        # if all 7 of the required fields (ignoring country ID) are present and valid, add it to the number of valid passports
        if (validFieldsCount == 7):
            validPassports += 1

        # reset the current passport's data, data list, and count of valid fields for the next passport
        passportData = ""
        dataList = []
        validFieldsCount = 0
        
f.close()

# print the total number of valid passports
print("There are", validPassports, "valid passports")
