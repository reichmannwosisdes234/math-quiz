
import random

def get_random_code():
    numbers = list(range(10))
    operators = ["+", "-", "*", "/"]
    equation = []
    for i in range(3):
        operator = random.choice(operators)
        number = random.choice(numbers)
        equation.append(operator)
        equation.append(number)
    return "".join(str(e) for e in equation)