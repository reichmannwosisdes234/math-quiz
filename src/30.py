def calculate_total(num1, num2):
    total = num1 + num2
    return total

def display_results(user_answers, correct_answer):
    print("Your answers:")
    for i in range(len(user_answers)):
        if user_answers[i] == correct_answer:
            print(f"{i+1}. {user_answers[i]}")
    print("\nYou got:", len(user_answers), "questions right.")
