import random

def get_random_math_problem():
    operators = ["+", "-", "*", "/"]
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    operator = random.choice(operators)
    problem = f"{num1} {operator} {num2}"
    solution = eval(problem)
    return problem, solution
