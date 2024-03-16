
# Importing some function and methods from python files.
from user_auth.load_user import load_user_data
from App.app_code.quiz_app_handler import start_quiz

# This function is using for login the user and show error on wrong credentials.
def login():
    print("\n\n\033[95mLog In with correct username and password!\033[0m\n\n")
    username = input("\033[1mEnter your username: \033[0m")
    password = input("\033[1mEnter your password: \033[0m")

    user_data = load_user_data()

    if username in user_data and user_data[username]['password'] == password:
        print("\n\n\033[92mLogin successful!\033[0m\n\n\n")
        start_quiz(username)
    else:
        print("\033[91mInvalid username or password.\033[0m")
