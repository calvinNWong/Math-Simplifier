operators = []
operatorsPosition = []

originalEquation = "y=5(x-5.1)^2+9"
solveFor = "y"

#Find operators in the equation
def findOperators(equation):
  repeats = 0
  for char in equation:
    if char == '+' or char == '-':
      operators.append(char)
      operatorsPosition.append(repeats)
      print("found addition")
    elif char == '*' or char == '/':
      operators.append(char)
      operatorsPosition.append(repeats)
      print("found multiplication")
    elif char == '^':
      operators.append(char)
      operatorsPosition.append(repeats)
      print("found exponents")
    elif char == "(" or char == ")":
      operators.append(char)
      operatorsPosition.append(repeats)
      print("found parenthesis")
    repeats += 1

#Find numbers in the equation
def findNumbers(equation):
  for char in equation:
    if char.isnumeric:
      print("found number " + char)


def checkAroundOperators(equation):
  repeats = 0
  for char in operators:
    #if operator is +
    if char == "+":
      #if operator is next to 2 numeric numbers
      if equation[operatorsPosition[repeats] -
                  1].isnumeric == True and equation[operatorsPosition[repeats] + 1].isnumeric == True:
        print("Adding two numbers")
      #else if the operator is next to a variable
      elif equation[operatorsPosition[repeats] - 1].isnumeric == False or equation[operatorsPosition[repeats] + 1].isnumeric == False:
        #if the two variables are the same
        if equation[operatorsPosition[repeats] - 1] == equation[operatorsPosition[repeats] + 1]:
          print("Simplified two variables to 2(variable)")
        elif equation[operatorsPosition[repeats] - 1] == solveFor or equation[operatorsPosition[repeats] + 1] == solveFor:
          print("Do nothing")
        elif equation[operatorsPosition[repeats] - 1] != solveFor and equation[operatorsPosition[repeats] + 1] != solveFor:
          print("Do nothing")
        elif equation[operatorsPosition[repeats] - 1] == solveFor and equation[operatorsPosition[repeats] + 1] == solveFor:
          print("Subtracting both sides by (not solveFor)")
    #else if operator is -
    elif char == "-":
      if equation[operatorsPosition[repeats] -
                  1].isnumeric == True and equation[operatorsPosition[repeats]
                                                    + 1].isnumeric == True:
        print("Subtracting two numbers")
      elif equation[operatorsPosition[repeats] -
                    1].isnumeric == False or equation[
                        operatorsPosition[repeats] + 1].isnumeric == False:
        if equation[operatorsPosition[repeats] -
                    1] != solveFor or equation[operatorsPosition[repeats] +
                                               1] != solveFor:
          print("Nothing to do")

    repeats += 1


findOperators(originalEquation)
findNumbers(originalEquation)
checkAroundOperators(originalEquation)
