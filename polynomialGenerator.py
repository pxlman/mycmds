import random
import sympy
import time
from sys import argv
from sympy import Poly, sympify
from sympy.abc import x

def normalPower(expr):
    return expr.replace("**","^")
def degree(expression):
    expression = expression.replace("x^","*x^")
    expression = sympy.sympify(expression)
    try:
        deg = sympy.degree(expression,x)
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
    expression = expression.replace('x^','*x^')
    data = sympy.expand("("+expression+")")
    return data
# Summation of two expressions
def summation(expression1,expression2):
    expression1 = expression1.replace('x^','*x^')
    expression2 = expression2.replace('x^','*x^')
    data = Poly(sympify(expression1) + sympify(expression2),x)
    return data
# Subtraction of two expressions
def sub(expression1,expression2):
    expression1 = expression1.replace('x^','*x^')
    expression2 = expression2.replace('x^','*x^')
    data = Poly(sympify(expression1) - (sympify(expression2)),x)
    return data
# Product of two expressions
def product(expression1,expression2):
    expression1 = expression1.replace('x^','*x^')
    expression2 = expression2.replace('x^','*x^')
    data = Poly((sympify(expression1)) * (sympify(expression2)),x)
    return data
# Derivative of an expression
def derivative(expression):
    expression = expression.replace('x^','*x^')
    data = sympy.diff(expression,'x')
    return data
# Integration of an expression
def integral(expression):
    from sympy.abc import x
    expression = expression.replace('x^','*x^')
    data = sympy.integrate(sympy.sympify(expression),x)
    data = Poly([float("{:.5f}".format(c)) for c in Poly(data, x).all_coeffs()], x).as_expr()
    return data
# Integration of an expression fractioned
def integralf(expression):
    from sympy import Number,Poly,re
    from sympy.abc import x
    expression = expression.replace('x^','*x^')
    data = sympy.integrate(sympy.sympify(expression),x)
    return data
# Definite integration of an expression from 0 to 1
def definite_integration(expression):
    from decimal import Decimal,getcontext
    getcontext().prec = 5
    expression = expression.replace("x^","*x^")
    # data = float("{:.5f}".format(sympy.integrate(expression, ("x", 0, 1))))
    data = Decimal(float(sympy.integrate(expression, ("x", 0, 1))))
    return data
# Definite integration of an expression from 0 to 1 fractioned
def definite_integrationf(expression):
    expression = expression.replace("x^","*x^")
    data = sympy.integrate(expression, ("x", 0, 1))
    return data
# Evaluate an expression at x = 2
def at2(expression):
    expression = expression.replace("x^","*x^")
    expression = sympy.sympify(expression)
    data = expression.subs(sympy.sympify('x'),2)
    return data

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
def compose(expression):
    expression = expression.replace("x^","*x^")
    expression = sympy.sympify(expression)
    data = Poly(expression,x).compose(Poly(expression,x)).as_expr()
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
#forUs = input("If it's for us just enter hehe: ")
forUs = argv[1]
ncases = int(argv[2])
foramr = argv[3]
for case in generateTestCases(ncases):
    expr = toExpr(case)
    print("//Test Case (" + str(i+1) + "): ")
    i += 1
    expr1 = expr['expression1']
    expr2 = expr['expression2']
    if forUs != "hehe":
        print(str(expr['deg1']))
        print(case[1])
        print(str(expr['deg2']))
        print(case[3])
        print("")
        print("Expected output: ")
        print("Polynomial 1: " + str(simplify(expr1)).replace("**","^"))
        print("Polynomial 2: " + str(simplify(expr2)).replace("**","^"))
        print("Sum: " + str(summation(expr1,expr2).as_expr()).replace("**","^"))
        print("Subtraction: " + str(sub(expr1,expr2).as_expr()).replace("**","^"))
        print("Product: " + str(product(expr1,expr2).as_expr()).replace("**","^"))
        print("Degree of Polynomial: " + str(expr['deg1']))
        print("Evaluation of polynomial at x=2: " + str(at2(expr1)))
        print("Derivative: " + str(derivative(expr1).as_expr()).replace("**","^"))
        if foramr == "amr":
            print("Integral: " + str(integral(expr1).as_expr()).replace("**","^"))
            print("Definite integration from x=0 to x=1: " + str(definite_integration(expr1)))
        else:
            print("Integral: " + str(integralf(expr1).as_expr()).replace("**","^"))
            print("Definite integration from x=0 to x=1: " + str(definite_integrationf(expr1)))
        print("Real roots of Polynomial 1: " + str(root(expr1)))
        print("Compose of Polynomial 1: " + str(compose(expr1)).replace("**","^"))
    else:
        print("""
   TEST_F(PolynomialTest, Addition"""+str(i)+""") {
        Polynomial p1{{"""+",".join(case[1].split(' '))+"""}};
        Polynomial p2{{"""+",".join(case[3].split(' '))+"""}};
        Polynomial sum = p1 + p2;
        EXPECT_EQ(sum, Polynomial({"""+",".join([ str(c) for c in summation(expr1,expr2).all_coeffs()[::-1]])+"""}));  // Expected result of p1 + p2
    } 
    """)
        print("""
   TEST_F(PolynomialTest, Subtraction"""+str(i)+""") {
        Polynomial p1{{"""+",".join(case[1].split(' '))+"""}};
        Polynomial p2{{"""+",".join(case[3].split(' '))+"""}};
        Polynomial sum = p1 - p2;
        EXPECT_EQ(sum, Polynomial({"""+",".join([ str(c) for c in sub(expr1,expr2).all_coeffs()[::-1]])+"""}));  // Expected result of p1 + p2
    } 
    """)
        print("""
   TEST_F(PolynomialTest, Multiplication"""+str(i)+""") {
        Polynomial p1{{"""+",".join(case[1].split(' '))+"""}};
        Polynomial p2{{"""+",".join(case[3].split(' '))+"""}};
        Polynomial sum = p1 * p2;
        EXPECT_EQ(sum, Polynomial({"""+",".join([ str(c) for c in product(expr1,expr2).all_coeffs()[::-1]])+"""}));  // Expected result of p1 + p2
    } 
    """)
        print("""
    TEST_F(PolynomialTest, Evaluation"""+str(i)+""") {
        Polynomial p1{{"""+",".join(case[1].split(' '))+"""}};
        EXPECT_EQ(p1.evaluate(2),"""+str(at2(expr1))+""");
    }
    """)
        print("""
    TEST_F(PolynomialTest, Degree"""+str(i)+""") {
        Polynomial p1{{"""+",".join(case[1].split(' '))+"""}};
        EXPECT_EQ(p1.degree(),"""+str(degree(expr1))+""");
    }
    """)
        print("""
    // Test derivative
    TEST_F(PolynomialTest, Derivative"""+str(i)+""") {
        Polynomial p1{{"""+",".join(case[1].split(' '))+"""}};
        EXPECT_EQ(p1.derivative(), Polynomial({"""+",".join([ str(c) for c in Poly(derivative(expr1),x).all_coeffs()[::-1]])+"""}));
    }
    """)
        print("""
    // Test integral
    TEST_F(PolynomialTest, Integral"""+str(i)+""") {
        Polynomial p1{{"""+",".join(case[1].split(' '))+"""}};
        EXPECT_EQ(p1.integral(), Polynomial({"""+",".join([ str(c) for c in Poly(integral(expr1),x).all_coeffs()[::-1]])+"""}));
    }
    """)
        print("""
    // Test definite integral
    TEST_F(PolynomialTest, dintegral"""+str(i)+""") {
        Polynomial p1{{"""+",".join(case[1].split(' '))+"""}};
        double expected{"""+str(float(definite_integration(expr1)))+"""  };
        EXPECT_EQ(p1.integral(0,1), expected);
    }
    """)
        roots = root(expr1)
        print("""
    // Test root finding (assuming root is 0 for x=1)
    TEST_F(PolynomialTest, Root"""+str(i)+""") {
        Polynomial p1{{"""+",".join(case[1].split(' '))+"""}};
        double values[] = {"""+",".join([str(r) for r in root(expr1)])+"""};
        double target = p1.getRoot();
        EXPECT_TRUE(isNearInArray(target, values, """+str(len(root(expr1)))+""", 0.001));
    }
    """)
        print("""
    // Test Compose function
    TEST_F(PolynomialTest, Compose"""+str(i)+""") {
        Polynomial p1{{"""+",".join(case[1].split(' '))+"""}};
        Polynomial cc = p1.compose(p1);
        EXPECT_EQ(cc, Polynomial({"""+",".join([ str(c) for c in Poly(compose(expr1),x).all_coeffs()[::-1]])+"""}));
    }
    """)
