import sys
sys.path.append('/Users/khalid/Documents/Projects/CoderQuiz/CoderQuiz/views')

from user_auth.auth import main as user_auth_main

def main():
    print("\n\n\033[95mWelcome to CoderQuiz!\033[0m")  # Header in magenta color
    # print("\033[94m1. Sign Up\n2. Log In\n3. Change Password\n4. Exit\033[0m")  # Menu options in blue color
    print("Type Y or Yes to start the Quiz App.\n\n")
    choice = input("\033[1mEnter Yes or No: \033[0m").lower()  # Bold prompt for user input
    print(choice)
    if choice == "y" or choice == "yes":
        # Call user authentication main function
        user_auth_main()
        
    elif choice == 'n' or choice == "no":
        print("\033[92mExiting...\033[0m")  # Green color for "Exiting..."
        sys.exit()
    else:
        print("\n\n\033[91mInvalid choice. Please try again.\033[0m\n\n")  # Red color for error message
if __name__ == "__main__":
    main()
