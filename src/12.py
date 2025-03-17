import random

def get_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def get_random_operator():
    operators = ["+", "-", "*", "/"]
    return random.choice(operators)

def generate_question():
    num1 = get_random_number(1, 10)
    num2 = get_random_number(1, 10)
    operator = get_random_operator()
    question = f"What is {num1} {operator} {num2}"
    return question

def check_answer(user_answer):
    try:
        user_answer = int(user_answer)
    except ValueError:
        print("Please enter a number")
        return False
    correct_answer = eval(f"{num1} {operator} {num2}")
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print("Incorrect, the answer is", correct_answer)
        return False

question = generate_question()
print(question)
user_answer = input("Your answer: ")
check_answer(user_answer)
