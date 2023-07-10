# declare the starting number of valid passwords
validPasswords = 0

# open the file with all the policies and corresponding passwords and assign it to p
p = open('pass_input.txt')

# go through every password in the input file
for line in p.readlines():
    # separate the policy and the password and assign them to their respective variables
    separator = line.find(":")
    policy = line[0:separator]
    password = line[separator+2:len(line)-1]
    # separate the policy to get the necessary information into their own variables
    nbrSeparator = policy.find("-")
    letterSeparator = policy.find(" ")
    nbr1 = int(policy[0:nbrSeparator])
    nbr2 = int(policy[nbrSeparator+1:letterSeparator])
    letter = policy[letterSeparator+1:]
    # start the number of letters found in the password at zero
    letterCount = 0
    # check each letter in the password and if it matches the letter required in the policy, 
    # add one to the letterCount
    for i in password:
        if i == letter:
            letterCount += 1
    # if the password fulfilled its policy, add one to the number of valid passwords
    if (letterCount >= nbr1) and (letterCount <= nbr2):
        validPasswords += 1

p.close()

# print the number of valid passwords
print("There are", validPasswords, "valid passwords in the database")
