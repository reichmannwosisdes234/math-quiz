import random

def get_random_math_problem():
    operands = [10, 20, 30]
    operator = random.choice(["+", "-", "*", "/"])
    answer = eval(" ".join([str(operands[i]), operator, str(operands[i+1])]))
    return f"{operands[0]} {operator} {operands[1]}"
