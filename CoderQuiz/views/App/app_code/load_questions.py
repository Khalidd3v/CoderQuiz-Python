
# This function is loading all the question store in following python dictionaries:
def load_questions(language):
    
    questions = {
        'HTML': {
            "What does HTML stand for?": {
                "correct_answer": "Hyper Text Markup Language",
                "wrong_answers": ["Hyperlinks and Text Markup Language", "Home Tool Markup Language", "Hyper Text Management Language"]
            },
            "What is the correct HTML element for the largest heading?": {
                "correct_answer": "h1",
                "wrong_answers": ["head", "heading", "hlargest"]
            },
            "What is the correct HTML for adding a line break?": {
                "correct_answer": "<br>",
                "wrong_answers": ["<break>", "<lb>", "<linebreak>"]
            },
            "What is the correct HTML tag for creating a hyperlink?": {
                "correct_answer": "<a>",
                "wrong_answers": ["<link>", "<href>", "<hyper>"]
            },
            "What is the correct HTML for inserting an image?": {
                "correct_answer": "<img src='image.jpg' alt='Description'>",
                "wrong_answers": ["<picture src='image.jpg' alt='Description'>", "<image src='image.jpg' alt='Description'>", "<img alt='Description' src='image.jpg'>"]
            },
            "Which HTML tag is used to define an unordered list?": {
                "correct_answer": "<ul>",
                "wrong_answers": ["<ol>", "<li>", "<list>"]
            },
            "Which HTML attribute is used to define inline styles?": {
                "correct_answer": "style",
                "wrong_answers": ["class", "id", "format"]
            },
            "What is the correct HTML for making a checkbox?": {
                "correct_answer": "<input type='checkbox'>",
                "wrong_answers": ["<checkbox>", "<check>", "<input type='check'>"]
            },
            "What is the correct HTML for creating a table?": {
                "correct_answer": "<table>",
                "wrong_answers": ["<tab>", "<grid>", "<datagrid>"]
            },
            "What is the correct HTML for creating a form?": {
                "correct_answer": "<form>",
                "wrong_answers": ["<input>", "<submit>", "<formdata>"]
            }
        },

        'CSS': {
            "What does CSS stand for?": {
                "correct_answer": "Cascading Style Sheets",
                "wrong_answers": ["Creative Style Sheets", "Computer Style Sheets", "Coded Style Sheets"]
            },
            "Which CSS property is used to change the text color of an element?": {
                "correct_answer": "color",
                "wrong_answers": ["text-color", "font-color", "background-color"]
            },
            "Which CSS property is used to change the background color of an element?": {
                "correct_answer": "background-color",
                "wrong_answers": ["background", "color", "text-color"]
            },
            "Which CSS property is used to set the height and width of an element?": {
                "correct_answer": "height and width",
                "wrong_answers": ["size", "dimensions", "scale"]
            },
            "Which CSS property is used to control the space between elements?": {
                "correct_answer": "margin",
                "wrong_answers": ["padding", "spacing", "border"]
            },
            "Which CSS property is used to make text bold?": {
                "correct_answer": "font-weight",
                "wrong_answers": ["bold", "font-style", "text-weight"]
            },
            "Which CSS property is used to remove the underline from links?": {
                "correct_answer": "text-decoration",
                "wrong_answers": ["underline", "link-decoration", "line-decoration"]
            },
            "Which CSS property is used to align text to the center of its container?": {
                "correct_answer": "text-align",
                "wrong_answers": ["align", "text-center", "center-align"]
            },
            "Which CSS property is used to set the font size of text?": {
                "correct_answer": "font-size",
                "wrong_answers": ["text-size", "font-style", "size"]
            },
            "Which CSS property is used to create rounded corners on an element?": {
                "correct_answer": "border-radius",
                "wrong_answers": ["rounded-corners", "corner-radius", "border-style"]
            }
        },
        'Python': {
            "What is Python?": {
                "correct_answer": "Python is a high-level programming language known for its simplicity and readability.",
                "wrong_answers": ["Python is a type of snake.", "Python is a video game.", "Python is a type of pasta."]
            },
            "What is the syntax to define a function in Python?": {
                "correct_answer": "def function_name(parameters):",
                "wrong_answers": ["function function_name(parameters):", "define function_name(parameters):", "func function_name(parameters):"]
            },
            "Which keyword is used for defining a loop in Python?": {
                "correct_answer": "for",
                "wrong_answers": ["loop", "repeat", "while"]
            },
            "How do you comment out multiple lines of code in Python?": {
                "correct_answer": "Use triple quotes (''' or ''') to enclose the block of comments.",
                "wrong_answers": ["Use // at the beginning of each line.", "Use /* */ to enclose the block of comments.", "Use # to comment out each line."]
            },
            "What is the output of 'print(2 + 3 * 4)' in Python?": {
                "correct_answer": "The output is 14.",
                "wrong_answers": ["The output is 20.", "The output is 18.", "The output is 15."]
            },
            "What is the purpose of 'if' statement in Python?": {
                "correct_answer": "'if' statement is used to execute a block of code only if a specified condition is true.",
                "wrong_answers": ["'if' statement is used to execute a block of code repeatedly.", "'if' statement is used to define a function.", "'if' statement is used to import modules."]
            },
            "What does the 'len()' function do in Python?": {
                "correct_answer": "The 'len()' function returns the number of items in an object.",
                "wrong_answers": ["The 'len()' function removes an item from an object.", "The 'len()' function adds items to an object.", "The 'len()' function updates an object."]
            },
            "How do you create a list in Python?": {
                "correct_answer": "You can create a list by enclosing elements in square brackets ([]).",
                "wrong_answers": ["You can create a list by using curly braces ({}) .", "You can create a list using parentheses (()).", "You can create a list using angle brackets (<>)."]
            },
            "What is the purpose of the 'append()' method in Python lists?": {
                "correct_answer": "The 'append()' method is used to add an element to the end of a list.",
                "wrong_answers": ["The 'append()' method is used to remove an element from a list.", "The 'append()' method is used to update an element in a list.", "The 'append()' method is used to search for an element in a list."]
            },
            "How do you access the last element of a list in Python?": {
                "correct_answer": "You can access the last element of a list using index -1.",
                "wrong_answers": ["You can access the last element of a list using index 0.", "You can access the last element of a list using index 1.", "You can access the last element of a list using index -2."]
            }
        },
        'JavaScript': {
            "What is JavaScript?": {
                "correct_answer": "JavaScript is a high-level, interpreted programming language used to create interactive effects within web browsers.",
                "wrong_answers": ["JavaScript is a type of coffee.", "JavaScript is a type of car.", "JavaScript is a type of fruit."]
            },
            "What is the syntax for declaring a variable in JavaScript?": {
                "correct_answer": "var variableName;",
                "wrong_answers": ["variable variableName;", "let variableName;", "int variableName;"]
            },
            "Which keyword is used to declare a function in JavaScript?": {
                "correct_answer": "function",
                "wrong_answers": ["def", "func", "method"]
            },
            "What is the purpose of the 'addEventListener()' method in JavaScript?": {
                "correct_answer": "The 'addEventListener()' method is used to attach an event handler to an element.",
                "wrong_answers": ["The 'addEventListener()' method is used to remove an event handler from an element.", "The 'addEventListener()' method is used to create an element.", "The 'addEventListener()' method is used to update an element."]
            },
            "How do you comment out a single line of code in JavaScript?": {
                "correct_answer": "// This is a comment",
                "wrong_answers": ["# This is a comment", "/* This is a comment */", "-- This is a comment"]
            },
            "How do you declare a constant variable in JavaScript?": {
                "correct_answer": "const variableName = value;",
                "wrong_answers": ["let variableName = value;", "var variableName = value;", "constant variableName = value;"]
            },
            "What does the 'innerHTML' property do in JavaScript?": {
                "correct_answer": "The 'innerHTML' property sets or returns the HTML content (inner HTML) of an element.",
                "wrong_answers": ["The 'innerHTML' property sets or returns the outer HTML of an element.", "The 'innerHTML' property sets or returns the text content of an element.", "The 'innerHTML' property sets or returns the CSS content of an element."]
            },
            "How do you select an element by its id in JavaScript?": {
                "correct_answer": "document.getElementById('elementId')",
                "wrong_answers": ["document.getElementByName('elementId')", "document.getElementByTag('elementId')", "document.getElementByClass('elementId')"]
            },
            "What is the purpose of the 'querySelector()' method in JavaScript?": {
                "correct_answer": "The 'querySelector()' method is used to select the first element that matches a specified CSS selector.",
                "wrong_answers": ["The 'querySelector()' method is used to select all elements that match a specified CSS selector.", "The 'querySelector()' method is used to update an element.", "The 'querySelector()' method is used to remove an element."]
            },
            "How do you create an array in JavaScript?": {
                "correct_answer": "You can create an array by enclosing elements in square brackets ([]).",
                "wrong_answers": ["You can create an array using curly braces ({}) .", "You can create an array using parentheses (()).", "You can create an array using angle brackets (<>)."]
            }
        },

        'C++': {
            "What is C++?": {
                "correct_answer": "C++ is a high-level programming language developed as an extension of the C programming language.",
                "wrong_answers": ["C++ is a type of car.", "C++ is a type of coffee.", "C++ is a type of fruit."]
            },
            "What is the syntax for declaring a variable in C++?": {
                "correct_answer": "data_type variable_name;",
                "wrong_answers": ["variable variable_name;", "let variable_name;", "int variable_name;"]
            },
            "Which symbol is used to denote a single-line comment in C++?": {
                "correct_answer": "//",
                "wrong_answers": ["#", "/* */", "--"]
            },
            "What is the purpose of 'cout' in C++?": {
                "correct_answer": "'cout' is used to display output to the standard output device (usually the console).",
                "wrong_answers": ["'cout' is used to accept input from the standard input device (usually the keyboard).", "'cout' is used to declare a constant variable.", "'cout' is used to define a function."]
            },
            "How do you declare a constant variable in C++?": {
                "correct_answer": "const data_type constant_name = value;",
                "wrong_answers": ["let data_type constant_name = value;", "const constant_name = value;", "constant data_type constant_name = value;"]
            },
            "What is the purpose of the 'cin' object in C++?": {
                "correct_answer": "'cin' is used to accept input from the standard input device (usually the keyboard).",
                "wrong_answers": ["'cin' is used to display output to the standard output device (usually the console).", "'cin' is used to declare a constant variable.", "'cin' is used to define a function."]
            },
            "What is the syntax for a 'for' loop in C++?": {
                "correct_answer": "for (initialization; condition; increment/decrement) { // code to be executed }",
                "wrong_answers": ["for (condition; initialization; increment/decrement) { // code to be executed }", "for (condition; increment/decrement; initialization) { // code to be executed }", "for (increment/decrement; condition; initialization) { // code to be executed }"]
            },
            "How do you declare and define a function in C++?": {
                "correct_answer": "return_type function_name(parameters) { // function body }",
                "wrong_answers": ["return function_name(parameters) { // function body }", "function function_name(parameters) { // function body }", "define function_name(parameters) { // function body }"]
            },
            "What is the purpose of the 'new' keyword in C++?": {
                "correct_answer": "The 'new' keyword is used to dynamically allocate memory for a variable or an object.",
                "wrong_answers": ["The 'new' keyword is used to declare a constant variable.", "The 'new' keyword is used to define a function.", "The 'new' keyword is used to accept input from the standard input device (usually the keyboard)."]
            },
            "What is the purpose of 'nullptr' in C++?": {
                "correct_answer": "'nullptr' is a pointer literal representing a null pointer. It is used to indicate that a pointer does not point to any memory location.",
                "wrong_answers": ["'nullptr' is used to display output to the standard output device (usually the console).", "'nullptr' is used to declare a constant variable.", "'nullptr' is used to define a function."]
            }
        },

    }

    return questions.get(language)

