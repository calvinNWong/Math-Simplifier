operators = []
operatorsPosition = []
solveFor = "y"


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


def checkAroundOperators(equation):
  repeats = 0
  for char in operators:
    #if operator is +
    if char == "+":
      if 
      if equation[operatorsPosition[repeats] - 1].isnumeric == False and equation[operatorsPosition[repeats] - 1] != solveFor or equation[operatorsPosition[repeats] + 1].isnumeric == False and equation[operatorsPosition[repeats] + 1] != solveFor:
        print("Nothing to do")
      elif equation[operatorsPosition[repeats] - 1].isnumeric and equation[operatorsPosition[repeats] + 1].isnumeric:
        print("adding two numbers")
      elif equation[operatorsPosition[repeats] - 1] == equation[operatorsPosition[repeats] + 1]:
        print("Replace with 2", equation[operatorsPosition[repeats] - 1])
    #else if operator is -
    elif char == "-":
      if equation[operatorsPosition[repeats] - 1].isnumeric == False and equation[operatorsPosition[repeats] - 1] != solveFor or equation[operatorsPosition[repeats] + 1].isnumeric == False and equation[operatorsPosition[repeats] + 1] != solveFor:
        print("Nothing to do")
      elif 

    repeats += 1

findOperators("y=m(x-k)^z+h")
