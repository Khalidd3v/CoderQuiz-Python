
# Importing different python functions and methods from files.
from .change_password import change_password
from .login import login
from .signup import signup

# Importing built-in functions from python.
import os

USER_DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), 
                                   "User_data/user_data.json")

# This function is starting the authentication system for the user.
def main():
    while True:
        print("\n1. Sign Up\n2. Log In\n3. Change Password\n4. Exit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            signup()
        elif choice == '2':
            login()
        elif choice == '3':
            change_password()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
