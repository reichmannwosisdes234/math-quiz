
import random

def get_random_math_problem():
    operands = [10, 20, 30, 40, 50]
    operators = ['+', '-', '*', '/']
    problem = ''
    for i in range(2):
        operand1 = random.choice(operands)
        operator = random.choice(operators)
        operand2 = random.choice(operands)
        if operator == '+':
            solution = operand1 + operand2
        elif operator == '-':
            solution = operand1 - operand2
        elif operator == '*':
            solution = operand1 * operand2
        else:
            solution = operand1 / operand2
        problem += str(operand1) + ' ' + operator + ' ' + str(operand2) + ' = '
    return problem + str(solution)