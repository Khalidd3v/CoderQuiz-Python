import json
import os

# Absolute path to the user data JSON file
USER_DATA_FILE_PATH = "/Users/khalid/Documents/Projects/CoderQuiz/CoderQuiz/User_data/user_data.json"

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
    with open(USER_DATA_FILE_PATH, 'w') as file:
        json.dump(user_data, file, indent=4)
