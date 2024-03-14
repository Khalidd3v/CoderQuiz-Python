from .choose_language import choose_language
from .load_questions import load_questions
from .display_quiz import display_quiz

def start_quiz(username):
    language = choose_language()
    if not language:
        return

    questions = load_questions(language)
    if not questions:
        return

    responses, score = display_quiz(questions)
    from .save_result import save_result  # Import save_result here to avoid circular import
    save_result(username, language, questions, responses, score)

if __name__ == "__main__":
    start_quiz()
