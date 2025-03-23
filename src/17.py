import sympy as sp

def calculate_expression(expression):
    result = sp.sympify(expression)
    print(result)

expression = "3*x**2 + 4*x - 5"
calculate_expression(expression)
