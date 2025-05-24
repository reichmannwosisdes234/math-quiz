import sympy as sp

def add(a, b):
    return sp.add(sp.sympify(a), sp.sympify(b))

def subtract(a, b):
    return sp.subtract(sp.sympify(a), sp.sympify(b))

def multiply(a, b):
    return sp.simplify(sp.mul(a, b))

def divide(a, b):
    if b != 0:
        return sp.simplify(sp.divide(a, b))
    else:
        return "Cannot divide by zero."

# Example usage
print(add(2, 3))  # Output: 5
print(subtract(4, 1))  # Output: -3
print(multiply(5, 6))  # Output: 30
print(divide(8, 2))  # Output: 4.0
