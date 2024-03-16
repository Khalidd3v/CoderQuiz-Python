
# Importing pyton builtin functions
import json

# This is third-party library for colors
from colorama import init, Fore, Style

# This function is printing the results for the user if he want to check so.
def print_results(results_file):
    init()

    with open(results_file, 'r') as file:
        results = json.load(file)

    for index, result in enumerate(results["results"]):
        question = result["question"]
        user_answer = result["user_answer"]
        correct_answer = result["correct_answer"]
        is_correct = result["is_correct"]
        print(f"{Style.BRIGHT}Question {index + 1}:{Style.RESET_ALL} {question}")
        print(f"Your Answer: {Fore.RED if not is_correct else Fore.GREEN}{user_answer}{Style.RESET_ALL}")
        print(f"Correct Answer: {Fore.GREEN}{correct_answer}{Style.RESET_ALL}" if is_correct else f"Correct Answer: {Fore.RED}{correct_answer}{Style.RESET_ALL}")
        print()


