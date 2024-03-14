import random

def display_quiz(questions):
    if not questions:
        print("\033[91mQuiz questions not found.\033[0m")  # Red color for error message
        return

    responses = {}
    score = 0

    print("\n\n\033[95mStarting quiz...\033[0m\n\n")  # Header in magenta color
    for question, answers_dict in questions.items():
        print(question + ":")
        options = [answers_dict["correct_answer"]] + answers_dict["wrong_answers"]
        random.shuffle(options)  # Shuffle options to randomize their order
        for idx, option in enumerate(options):
            print(f"{idx + 1}. {option}")
        user_answer_index = int(input("Your answer (enter the number): ")) - 1
        user_answer = options[user_answer_index]
        correct_answer = answers_dict["correct_answer"]
        responses[question] = {
            "user_answer": user_answer,
            "correct_answer": correct_answer
        }
        if user_answer.lower() == correct_answer.lower():
            score += 1

    print(f"\n\n\033[94mQuiz completed. Your score: {score}/{len(questions)}\033[0m\n\n")  # Score in blue color
    return responses, score
