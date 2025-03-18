import random

def get_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def generate_question():
    number1 = get_random_number(1, 10)
    number2 = get_random_number(1, 10)
    operation = random.choice(["+", "-", "*", "/"])
    answer = eval(f"{number1} {operation} {number2}")
    return f"What is {number1} {operation} {number2}?"
