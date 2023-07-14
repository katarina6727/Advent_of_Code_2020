# initialize variables
yesAnswersList = []
groupMembers = 0
sum = 0

# define function to calculate and return the number of questions everyone in the group answered yes to
def calcYesAnswers(answersList, membersNbr):
    yesQuestions = 0
    for l in "abcdefghijklmnopqrstuvwxyz":
            yeses = answersList.count(l)
            if (yeses == membersNbr):
                yesQuestions = yesQuestions + 1
    return yesQuestions

# open the file with all of the customs forms information and assign it to f
f = open('customs_input.txt')

for line in f.readlines():
    # add each character in the line of form answers to the list and add to the number of members in the group 
    # until that group's form answers are all added
    groupMembers += 1
    for a in line:
        if (a != "\n"):
            yesAnswersList.append(a)
    # subtract the extra group member added for the empty line, add the number of questions answered yes 
    # to the sum and then reset the yes answers list and number of members in the group
    if (line == "\n"):
        groupMembers -= 1
        sum = sum + calcYesAnswers(yesAnswersList, groupMembers)
        yesAnswersList = []
        groupMembers = 0
    
# if the program forgot to add the last form to the sum, add it now
if (len(yesAnswersList) != 0):
    sum = sum + calcYesAnswers(yesAnswersList, groupMembers)

f.close()

# print the ending sum
print("The sum of questions answered yes by every person in each group is", sum)
