import json
from .load_user import load_user_data, save_user_data

# Function for user signup
def signup():
    print("\n\n\033[95mSign Up in CoderQuiz App.\033[0m\n\n")  # Header in magenta color
    username = input("\033[1mEnter username: \033[0m")  # Bold prompt for username input
    password = input("\033[1mEnter password: \033[0m")  # Bold prompt for password input
    email = input("\033[1mEnter email: \033[0m")  # Bold prompt for email input

    user_data = load_user_data()

    if not user_data:
        # If user_data dictionary is empty, initialize it with the first user's data
        user_data = {username: {'password': password, 'email': email}}
        save_user_data(user_data)
        print("\033[92mSign up successful!\033[0m")  # Green color for successful signup
    elif username in user_data:
        print("\033[91mUsername already exists. Please choose a different username.\033[0m")  # Red color for username exists
    else:
        user_data[username] = {'password': password, 'email': email}
        save_user_data(user_data)
        print("\n\n\033[92mSign up successful!\033[0m\n\n")  # Green color for successful signup

