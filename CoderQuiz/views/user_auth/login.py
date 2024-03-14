import json
from user_auth.load_user import load_user_data
from App.app_code.quiz_app_handler import start_quiz

# Function for user login
def login():
    print("\n\n\033[95mLog In with correct username and password!\033[0m\n\n")  # Header in magenta color
    username = input("\033[1mEnter your username: \033[0m")  # Bold prompt for username input
    password = input("\033[1mEnter your password: \033[0m")  # Bold prompt for password input

    user_data = load_user_data()

    if username in user_data and user_data[username]['password'] == password:
        print("\n\n\033[92mLogin successful!\033[0m\n\n\n")  # Green color for successful login
        start_quiz(username)

    else:
        print("\033[91mInvalid username or password.\033[0m")  # Red color for invalid credentials
