
# Importing python built-in methods and modules
import os
import json
from datetime import datetime
import sys

# Impoting functions and methods from python files.
from .show_result import print_results
from .quiz_app_handler import start_quiz

RED = '\033[91m'
GREEN = '\033[92m'
ENDC = '\033[0m'

# This function is saving the result of the user quiz into Json file.
def save_result(username, language, questions, responses, score):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    result = {
        'username': username,
        'language': language,
        'results': []
    }

    for question, result_dict in responses.items():
        user_answer = result_dict['user_answer']
        correct_answer = result_dict['correct_answer']
        result_item = {
            'question': question,
            'user_answer': user_answer,
            'correct_answer': correct_answer,
            'is_correct': user_answer.lower() == correct_answer.lower() if isinstance(user_answer, str) else False
        }
        result['results'].append(result_item)

    results_dir = os.path.join("views", "results")

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    filename = os.path.join(results_dir, f"{username}_{timestamp}.json")

    try:
        with open(filename, 'w') as file:
            json.dump(result, file, indent=4)
        print(GREEN + f"Result saved to {filename}" + ENDC)
        re_try = input("\n\nDo you want to check your result? reply with ( Y / N ) : \n\n").lower()
        if re_try:
            if re_try == "y":
                print_results(filename)
                take_test = input("\n\nDo you want to re-try ? reply with Y / N : \n\n").lower()
                if take_test == "y":
                    start_quiz(username)
            if re_try == "n":
                print("\033[92mExiting...\033[0m")
                sys.exit()
    except Exception as e:
        print(RED + f"Failed to save result: {e}" + ENDC)
