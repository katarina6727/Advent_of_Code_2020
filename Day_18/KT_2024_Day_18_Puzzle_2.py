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
    # initialize variables
    sum = 0
    symbol = ""
    end = False
    next1 = ""
    next2 = ""
    indexPlus = exp.find("+")
    indexMult = exp.find("*")
    nbr1 = ""
    nbr2 = ""
    # find the symbol, first, and second number
    if (indexPlus == -1) and (indexMult == -1):
        return int(exp)
    if (indexPlus != -1):
        symbol = "+"
        before = exp[:indexPlus]
        after = exp[indexPlus+1:]
        # find the first number to add
        for b in before[::-1]:
            if end:
                next1 = b + next1
            elif (b == "*"):
                end = True
                next1 = b + next1
            else:
                nbr1 = b + nbr1
        nbr1 = int(nbr1)
        end = False
        # find the second number to add
        for a in after:
            if end:
                next2 += a
            elif (a == "+") or (a == "*"):
                end = True
                next2 += a
            else:
                nbr2 += a
        nbr2 = int(nbr2)
    else:
        symbol = "*"
        before = exp[:indexMult]
        after = exp[indexMult+1:]
        # find the first number to multiply
        for b in before[::-1]:
            if end:
                next1 = b + next1
            elif (b == "*"):
                end = True
                next1 = b + next1
            else:
                nbr1 = b + nbr1
        nbr1 = int(nbr1)
        end = False
        # find the second number to multiply
        for a in after:
            if end:
                next2 += a
            elif (a == "*"):
                end = True
                next2 += a
            else:
                nbr2 += a
        nbr2 = int(nbr2)
    # add or multiply the two numbers and do recursion things
    if (symbol == "+"):
        sum += nbr1 + nbr2
    else:
        sum += nbr1 * nbr2
    sum = calcInOrder(next1 + str(sum) + next2)
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