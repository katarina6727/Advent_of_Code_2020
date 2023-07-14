# initialize variables
yesAnswers = set()
sum = 0

# open the file with all of the customs forms information and assign it to f
f = open('customs_input.txt')

for line in f.readlines():
    # add each character in the line of form answers to the set until that group's
    # form answers are all done
    for a in line:
        if (a != "\n"):
            yesAnswers.add(a)
    # add the number of questions answered yes to the sum and then reset the yes 
    # answers set
    if (line == "\n"):
        sum = sum + len(yesAnswers)
        yesAnswers = set()
    
# if the program forgot to add the last form to the sum, add it now
if (len(yesAnswers) != 0):
    sum = sum + len(yesAnswers)

f.close()

# print the ending sum
print("The sum of questions answered yes by each group is", sum)
