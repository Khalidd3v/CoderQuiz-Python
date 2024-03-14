import json
from colorama import init, Fore, Style

def print_results(results_file):
    # Initialize colorama
    init()

    # Load JSON data from the file
    with open(results_file, 'r') as file:
        results = json.load(file)

    # Iterate over each result and print with colors and designs
    for index, result in enumerate(results["results"]):
        question = result[f"question"]
        user_answer = result["user_answer"]
        correct_answer = result["correct_answer"]
        is_correct = result["is_correct"]

        print(f"{Style.BRIGHT}Question {index}:{Style.RESET_ALL} {question}")
        print(f"Your Answer: {Fore.RED if not is_correct else Fore.GREEN}{user_answer}{Style.RESET_ALL}")
        print(f"Correct Answer: {Fore.GREEN}{correct_answer}{Style.RESET_ALL}" if is_correct else f"Correct Answer: {Fore.RED}{correct_answer}{Style.RESET_ALL}")
        print()

