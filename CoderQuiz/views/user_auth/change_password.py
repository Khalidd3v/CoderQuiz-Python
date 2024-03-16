# importing some methods from laod_user files
from .load_user import load_user_data, save_user_data


# Function to change user password
def change_password():
    print("\033[95mChange Password\033[0m")
    username = input("\033[1mEnter username: \033[0m")
    old_password = input("\033[1mEnter current password: \033[0m")

    user_data = load_user_data()

    if (username in user_data and
            user_data[username]['password'] == old_password):
        new_password = input("\033[1mEnter new password: \033[0m")
        user_data[username]['password'] = new_password
        save_user_data(user_data)
        print("\033[92mPassword changed successfully!\033[0m")
    else:
        print("\033[91mInvalid username or password.\033[0m")
