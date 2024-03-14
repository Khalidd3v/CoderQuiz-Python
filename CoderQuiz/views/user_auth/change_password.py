import json
from .load_user import load_user_data, save_user_data

# Function to change user password
def change_password():
    print("\033[95mChange Password\033[0m")  # Header in magenta color
    username = input("\033[1mEnter username: \033[0m")  # Bold prompt for username input
    old_password = input("\033[1mEnter current password: \033[0m")  # Bold prompt for current password input

    user_data = load_user_data()

    if username in user_data and user_data[username]['password'] == old_password:
        new_password = input("\033[1mEnter new password: \033[0m")  # Bold prompt for new password input
        user_data[username]['password'] = new_password
        save_user_data(user_data)
        print("\033[92mPassword changed successfully!\033[0m")  # Green color for successful password change
    else:
        print("\033[91mInvalid username or password.\033[0m")  # Red color for invalid username or password
