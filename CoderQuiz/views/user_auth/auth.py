from .change_password import *
from .load_user import *
from .login import *
from .signup import *
import json
import os

USER_DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), "User_data/user_data.json")

# Main function to demonstrate user authentication functionality
def main():
    print("\033[95mWelcome to CoderQuiz!\033[0m")  # Header in magenta color
    while True:
        print("\n\033[94m1. Sign Up\n2. Log In\n3. Change Password\n4. Exit\033[0m")  # Menu options in blue color
        choice = input("\n\033[1mEnter your choice: \033[0m\n")  # Bold prompt for user input

        if choice == '1':
            signup()
        elif choice == '2':
            login()
        elif choice == '3':
            change_password()
        elif choice == '4':
            print("\033[92mExiting...\033[0m")  # Green color for "Exiting..."
            break
        else:
            print("\033[91mInvalid choice. Please try again.\033[0m")  # Red color for error message

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
