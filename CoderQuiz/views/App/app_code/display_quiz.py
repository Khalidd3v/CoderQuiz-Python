#import random module to shuffle the questions the user will get in terminal.
import random

#This function will actually show all the questions one by one to the user
#to choose the right answer among 4 options with every question.
def display_quiz(questions):
    if not questions:
        print("\033[91mQuiz questions not found.\033[0m")
        return

    responses = {}
    score = 0

    print("\n\n\033[95mStarting quiz...\033[0m\n\n")

    #picking question one by one using for loop.
    for question, answers_dict in questions.items():
        print(question + ":")
        options = [answers_dict["correct_answer"]] + answers_dict["wrong_answers"]
        random.shuffle(options)

        for idx, option in enumerate(options):
            print(f"{idx + 1}. {option}")

        while True:
            user_answer_index = int(input("Your answer (enter the number): ")) - 1
            if user_answer_index >= 0 and user_answer_index < len(options):
                break
            else:
                print("Error: Please enter a number between 1 and", len(options))
                
        user_answer = options[user_answer_index]
        correct_answer = answers_dict["correct_answer"]
        responses[question] = {
            "user_answer": user_answer,
            "correct_answer": correct_answer
        }

        #checking if the answer is correct or not
        if user_answer.lower() == correct_answer.lower():
            score += 1

    print(f"\n\n\033[94mQuiz completed. Your score: {score}/{len(questions)}\033[0m\n\n")
    return responses, score
