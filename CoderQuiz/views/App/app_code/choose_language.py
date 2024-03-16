
#this function is actually taking the arguements from the user to show him
#questions about the selected lanuage or choosen option.
def choose_language():
    print("\n\n\033[95mChoose a language for the quiz:\033[0m\n\n")
    print("\033[94m1. HTML\n2. CSS\n3. Python\n4. JavaScript\n5. C++\033[0m")
    language_choice = input("\n\n\033[1mEnter the number corresponding to your choice: \033[0m")

    #User can select one of the following options:
    languages = {
        '1': 'HTML',
        '2': 'CSS',
        '3': 'Python',
        '4': 'JavaScript',
        '5': 'C++'
    }

    language = languages.get(language_choice)
    if not language:
        print("\033[91mInvalid choice. Please try again.\033[0m")
    return language
