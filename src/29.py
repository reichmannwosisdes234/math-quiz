import sympy as sp
from sympy import symbols, solve

x = symbols('x')
equation = x**2 + 3*x - 5

solutions = solve(equation, x)
print(solutions)
