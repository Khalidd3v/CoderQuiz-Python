
# Importing methods and functions from pyton files.
from .load_user import load_user_data, save_user_data

# This function is using for signup the user account and save the data.
def signup():
    print("\n\n\033[95mSign Up in CoderQuiz App.\033[0m\n\n")
    username = input("\033[1mEnter username: \033[0m")
    password = input("\033[1mEnter password: \033[0m")
    email = input("\033[1mEnter email: \033[0m")

    user_data = load_user_data()

    if not user_data:
        user_data = {username: {'password': password, 'email': email}}
        save_user_data(user_data)
        print("\033[92mSign up successful!\033[0m")
    elif username in user_data:
        print("\033[91mUsername already exists. "
              "Please choose a different username.\033[0m")
    else:
        user_data[username] = {'password': password, 'email': email}
        save_user_data(user_data)
        print("\n\n\033[92mSign up successful!\033[0m\n\n")
