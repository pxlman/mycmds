import requests
import json
import random
import re
import sympy
import time
import math

def normalPower(expr):
    return expr.replace("**","^")
def degree(expression):
    expression = expression.replace("x^","*x^")
    expression = sympy.sympify(expression)
    try:
        deg = sympy.degree(expression,sympy.sympify('x'))
    except:
        deg = 0
    return str(deg)
def toExpr(arr):
    # Expression 1
    expr1 = []
    i1 = 0
    for c in arr[1].split(' '):
        if str(i1) == '0':
            expr1.append(c)
        else:
            expr1.append(c + "x^" + str(i1))
        i1 += 1
    expr1 =" +".join(expr1)
    expr1 = expr1.replace("+-", "-")
    # Expression 2
    expr2 = []
    i2 = 0
    for c in arr[3].split(' '):
        if str(i2) == '0':
            expr2.append(c)
        else:
            expr2.append(c + "x^" + str(i2))
        i2 += 1
    expr2 = " +".join(expr2)
    expr2 = expr2.replace("+-", "-")
    return {'deg1':degree(expr1), 'expression1':expr1,'deg2':degree(expr2), 'expression2':expr2}
def simplify(expression):
   #url = "https://newton.now.sh/api/v2/simplify/" + expression
   #data = requests.get(url,timeout=(20,20)).json().get('result')
    expression = expression.replace('x^','*x^')
    data = sympy.expand("("+expression+")")
    return normalPower(str(data))
# Summation of two expressions
def summation(expression1,expression2):
   #url = "https://newton.now.sh/api/v2/simplify/(" + expression1 + ") + (" + expression2 + ')'
   #data = requests.get(url,timeout=(20,20)).json().get('result')
    expression1 = expression1.replace('x^','*x^')
    expression2 = expression2.replace('x^','*x^')
    data = sympy.expand("("+expression1+")+("+expression2+")")
    return normalPower(str(data))
# Subtraction of two expressions
def sub(expression1,expression2):
   #url = "https://newton.now.sh/api/v2/simplify/(" + expression1 + ") - (" + expression2 + ')'
   #data = requests.get(url,timeout=(20,20)).json().get('result')
    expression1 = expression1.replace('x^','*x^')
    expression2 = expression2.replace('x^','*x^')
    data = sympy.expand("("+expression1+")-("+expression2+")")
    return normalPower(str(data))
# Product of two expressions
def product(expression1,expression2):
    #url = "https://newton.now.sh/api/v2/simplify/(" + expression1 + " ) * ( " + expression2 + ' )'
    #data = requests.get(url,timeout=(20,20)).json().get('result')
    expression1 = expression1.replace('x^','*x^')
    expression2 = expression2.replace('x^','*x^')
    data = sympy.expand("("+expression1+")*("+expression2+")")
    return normalPower(str(data))
# Derivative of an expression
def derivative(expression):
    #url = "https://newton.now.sh/api/v2/derive/" + expression
    #data = requests.get(url,timeout=(20,20)).json().get('result')
    expression = expression.replace('x^','*x^')
    data = sympy.diff(expression,'x')
    return normalPower(str(data))
# Integration of an expression
def integral(expression):
   #url = "https://newton.now.sh/api/v2/integrate/" + expression
   #data = requests.get(url,timeout=(20,20)).json().get('result')
    expression = expression.replace('x^','*x^')
    data = sympy.integrate(sympy.sympify(expression),sympy.sympify('x'))
    return normalPower(str(data))
# Definite integration of an expression from 0 to 1
def definite_integration(expression):
    expression = expression.replace("x^","*x^")
    data = sympy.integrate(expression, ("x", 0, 1))
    return normalPower(str(data))
# Evaluate an expression at x = 2
def at2(expression):
    expression = expression.replace("x^","*x^")
    expression = sympy.sympify(expression)
    data = expression.subs(sympy.sympify('x'),2)
    #url = "https://newton.now.sh/api/v2/simplify/" + expression
    #data = requests.get(url,timeout=(20,20)).json().get('result')
    return normalPower(str(data))

def root(expression):
    from sympy.abc import x
    expression = expression.replace("x^","*x^")
    expression = sympy.sympify(expression)
    if degree(str(expression)) == '0':
        return []
    try:
        data = sympy.nroots(expression)
        data = [real for real in data if real.is_real]
    except:
        return []
    return data
def generateTestCases(n):
    testCases = []
    for i in range(n):
        pol1 = []
        random.seed(time.time())            
        for j in range(random.randint(1, 12)):
            pol1.append(random.randint(1, 30) - 15)
        pol2 = []
        random.seed(time.time())            
        for j in range(random.randint(1, 12)):
            pol2.append(random.randint(1, 30) - 15)
        testCases.append([degree("+".join([str(i) for i in pol1 ])), " ".join([str(c) for c in pol1]),degree("+".join([str(i) for i in pol2 ])), " ".join([str(c) for c in pol2])])
    return testCases
i = 0
for case in generateTestCases(250):
    expr = toExpr(case)
    print("Test Case (" + str(i+1) + "): ")
    i += 1
    print(str(expr['deg1']))
    print(case[1])
    print(str(expr['deg2']))
    print(case[3])
    print("")
    print("Expected output: ")
    expr1 = expr['expression1']
    expr2 = expr['expression2']
    print("Polynomial 1: " + simplify(expr1))
    print("Polynomial 2: " + simplify(expr2))
    print("Sum: " + summation(expr1,expr2))
    print("Subtraction: " + sub(expr1,expr2))
    print("Product: " + product(expr1,expr2))
    print("Degree of Polynomial: " + str(expr['deg1']))
    print("Evaluation of polynomial at x=2: " + at2(expr1))
    print("Derivative: " + derivative(expr1))
    print("Integral: " + integral(expr1))
    print("Definite integration from x=0 to x=1: " + str(definite_integration(expr1)))
    print("Real roots of Polynomial 1: " + str(root(expr1)))
