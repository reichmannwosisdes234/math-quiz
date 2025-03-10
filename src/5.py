import random
def generate_random_code():
    num = random.randint(1, 10)
    operators = ["+", "-", "*", "/"]
    operator = random.choice(operators)
    result = eval(str(num) + operator + str(random.randint(1, 10)))
    return result
