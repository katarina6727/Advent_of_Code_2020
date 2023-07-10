# declare the starting number of valid passwords
validPasswords = 0
t = 0

# open the file with all the policies and corresponding passwords and assign it to p
p = open('pass_input.txt')

# go through every password in the input file
for line in p.readlines():
    # # separate the policy and the password and assign them to their respective variables
    # separator = line.find(":")
    # policy = line[0:separator]
    # password = line[separator+2:len(line)-1]
    policy = "12-20 t"
    password = "abcdefghijklmopqrstuv"
    # # separate the policy to get the necessary information into their own variables
    nbrSeparator = policy.find("-")
    letterSeparator = policy.find(" ")
    nbr1 = int(policy[0:nbrSeparator])
    nbr2 = int(policy[nbrSeparator+1:letterSeparator])
    letter = policy[letterSeparator+1:]
    # start the number of letters found in the password at zero
    letterCount = 0
    # check if the letters at the locations given are the letter required in the policy
    if (password[nbr1-1:nbr1] == letter):
        letterCount += 1
    if (password[nbr2-1:nbr2] == letter):
        letterCount += 1
    print(letterCount, letter, password[nbr1-1:nbr1], password[nbr2-1:nbr2])
    # if the password fulfilled its policy, add one to the number of valid passwords
    if (letterCount == 1):
        validPasswords += 1
        print("valid")
    break

p.close()

# print the number of valid passwords
print("There are", validPasswords, "valid passwords in the database")

