import sympy as sp
from sympy import symbols

def calculate_derivative(expression):
    """
    Calculate the derivative of an expression with respect to x.
    
    Parameters:
    expression (str): The mathematical expression whose derivative needs to be calculated.
    
    Returns:
    str: The result of the derivative calculation in LaTeX format.
    """
    return sp.diff(sp.sympify(expression), symbols('x'))

# Example usage
expression = "x**2 + 3*x - 4"
derivative = calculate_derivative(expression)
print(derivative)

