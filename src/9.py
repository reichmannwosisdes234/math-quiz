import random

def get_random_math_question(difficulty):
    if difficulty == "easy":
        numbers = list(range(1, 10))
        operation = ["+", "-"][random.randint(0, 1)]
        question = f"What is {numbers[0]} {operation} {numbers[1]}?"
        answer = numbers[0] + numbers[1]
    elif difficulty == "medium":
        numbers = list(range(1, 21))
        operation = ["+", "-", "*", "/"][random.randint(0, 3)]
        question = f"What is {numbers[0]} {operation} {numbers[1]}?"
        answer = numbers[0] + numbers[1] if operation == "+" else numbers[0] - numbers[1] if operation == "-" else numbers[0] * numbers[1] if operation == "*" else numbers[0] / numbers[1]
    elif difficulty == "hard":
        numbers = list(range(1, 101))
        operation = ["+", "-", "*", "/"][random.randint(0, 3)]
        question = f"What is {numbers[0]} {operation} {numbers[1]}?"
        answer = numbers[0] + numbers[1] if operation == "+" else numbers[0] - numbers[1] if operation == "-" else numbers[0] * numbers[1] if operation == "*" else numbers[0] / numbers[1]
    return question, answer
