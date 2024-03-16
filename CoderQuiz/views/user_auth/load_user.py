
# Importing built-in python functions and modules.
import json
import os

# Get the absolute path of the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Relative path to the user data JSON file from the current directory
relative_path = "User_data/user_data.json"

# Absolute path to the user data JSON file using the relative path
USER_DATA_FILE_PATH = os.path.join(current_directory, relative_path)


# Function to load user data from JSON file
def load_user_data():
    if not os.path.exists(USER_DATA_FILE_PATH):
        # If file doesn't exist, initialize user data as an empty dictionary
        return {}

    try:
        with open(USER_DATA_FILE_PATH, 'r') as file:
            user_data = json.load(file)
    except json.JSONDecodeError:
        # If JSON decoding fails, initialize user data as an empty dictionary
        user_data = {}

    return user_data


# Function to save user data to JSON file
def save_user_data(user_data):
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(USER_DATA_FILE_PATH), exist_ok=True)
    with open(USER_DATA_FILE_PATH, 'w') as file:
        json.dump(user_data, file, indent=4)
