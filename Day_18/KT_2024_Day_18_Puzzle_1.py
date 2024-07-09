# initialize variables
expressions = []
totalSum = 0

# open the file and add each line to a list while removing the spaces
f = open('math_homework_input.txt')
for line in f.readlines():
    if (line.find("\n") != -1):
        line = line[:len(line)-1]
    expressions.append(line.replace(" ", ""))

# create a function to calculate the sum based on the new math rules (no parentheses in expression)
def calcInOrder(exp):
    sum = 0
    symbol = ""
    indexPlus = exp.find("+")
    indexMult = exp.find("*")
    # find the first number and type of operation
    if (indexPlus == -1) and (indexMult == -1):
        return int(exp)
    if (indexPlus < indexMult) and (indexPlus != -1) or (indexMult == -1):
        symbol = "+"
        nbr1 = int(exp[:indexPlus])
        temp = exp[indexPlus+1:]
    else:
        symbol = "*"
        nbr1 = int(exp[:indexMult])
        temp = exp[indexMult+1:]
    indexPlus = temp.find("+")
    indexMult = temp.find("*")
    # find the second number
    if (indexPlus == -1) and (indexMult == -1):
        nbr2 = int(temp)
        next = ""
    elif (indexPlus < indexMult) and (indexPlus != -1) or (indexMult == -1):
        nbr2 = int(temp[:indexPlus])
        next = temp[indexPlus:]
    else:
        nbr2 = int(temp[:indexMult])
        next = temp[indexMult:]

    if (symbol == "+"):
        sum += nbr1 + nbr2
    else:
        sum += nbr1 * nbr2
    sum = calcInOrder(str(sum) + next)
    return sum

# define a function that goes through and solves the problem based on the order of parentheses
def findParentheses(exp):
    newExp = exp
    if (exp.find('(') != -1):
        replacement = findParentheses(exp[exp.find('(')+1:])
        newExp = newExp[:exp.find('(')] + replacement
    if (newExp.find(')') == -1):
        changed = str(calcInOrder(newExp))
    else:
        changed = str(calcInOrder(newExp[:newExp.find(')')])) + newExp[newExp.find(')')+1:]
    return changed

# calculate and then print the total sum of the answers to every problem
for problem in expressions:
    answer = calcInOrder(findParentheses(problem))
    totalSum += answer

print(totalSum)