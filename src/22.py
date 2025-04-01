import numpy as np

def check_accuracy(question_answers):
    correct = 0
    total_questions = len(question_answers)
    
    for i in range(total_questions):
        guess_answer = input(f"Question {i+1}: {question_answers[i]}")
        
        if "correct answer" in question_answers and guess_answer.lower() == question_answers["correct answer"].lower():
            correct += 1
        
    accuracy = (correct / total_questions) * 100
    print("Accuracy: ", accuracy)
    
# Example usage
question_answers = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "Who invented Python?", "answer": "Guido van Rossum"},
    # Add more questions here...
]
check_accuracy(question_answers)
