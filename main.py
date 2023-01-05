import csv
import sympy
from sympy import Symbol, sympify
import re

# define symbols
N = Symbol("N")
A = Symbol("A")

# create a list to store the equations
equations = []
symbols = set()

# open the input file and read the contents into a list of rows
with open('outputConst.csv', 'r') as f:
    rows = list(csv.reader(f))

# iterate over the rows
for row in rows:
    # check if there are 1 or fewer units in the row
    if len(row[1].split('*')) <= 1:
        continue
    # split the equation string into the constant numerical value and the expression
    # parts = row[1].split("=")

    constant_value = float(row[0])

    expression = row[1]
    #expression = row[0] + " - " + row[1]
    # find the caret symbol followed by a negative exponent

    pattern = r"\^(-\d+)"
    # replace the caret symbol and negative exponent with parentheses around the exponentiation operator and the exponent
    expression = re.sub(pattern, r"**(\1)", expression)
    # create a sympy expression from the expression string

    print(expression)
    if (row[1] == "N*A^-2"):
        continue
        print("here")
        expression == ("N*(A**(-2))")
        expr = (sympy.Symbol("N")*sympy.Symbol("A")**(-2))
    else:
     expr = sympy.sympify(expression)

    # get the symbols in the expression
    new_symbols = expr.atoms(sympy.Symbol)
    # add the new symbols to the set of symbols
    symbols.update(new_symbols)

    # create a new equation in the form "constant_value = expr"
    equation = "1" + str(constant_value) + " - " + str(expression) # formerly expr

    # add the equation to the list
    equations.append(equation)

# print the list of equations
print(equations)


# solve the equations for the variables
solutions = sympy.solve(equations, symbols)

# print the solutions
print(solutions)
