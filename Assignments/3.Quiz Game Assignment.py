def python_game_quiz():
    print("Welcome to the Python Quiz Game!")
    questions = (
        "Question 1: What is a variable in Python?",
        "Question 2: Which keyword is used to define a function in Python?",
        "Question 3: How do you declare a variable in Python?",
        "Question 4: Which of the following is a valid variable name in Python?",
        "Question 5: How do you start a comment in Python?",
        "Question 6: How do you swap the values of two variables in Python without using a third variable?",
        "Question 7: Which of the following data types is immutable in Python?",
        "Question 8: What does the type() function return in Python?",
        "Question 9: What is the scope of a global variable in Python?",
        "Question 10: How do you convert a string to an integer in Python?",
        "Question 11: Which of these is not a core data type?",
        "Question 12: What data type is this-> li = [1, 23, ‘hello’, 1]",
        "Question 13: Which of the following function convert a string x to a float in python?",
        "Question 14: Which Python datatype maintains the order of elements inserted?",
        "Question 15: print(9//2)",
        "Question 16: Which function overloads the >> operator?",
        "Question 17: Which special method overloads the bitwise OR (|) operator in Python?",
        "Question 18: What is the purpose of the if statement in Python?",
        "Question 19: Which of the following operators is used for equality comparison in Python?",
        "Question 20: What is the purpose of the elif statement in Python?",
    )
    options = (
        ("A) A reserved word", "B) A data type", "C) A location in memory to store data", "D) A function"),
        ("A) function", "B) def", "C) fun", "D) define"),
        ("A) var x", "B) x = variable", "C) declare x", "D) x = 4"),
        ("A) 1variable", "B) my_variable", "C) global", "D) variable-1"),
        ("A) //", "B) <!--", "C) #", "D) **"),
        ("A) x = y; y = x", "B) x, y = y, x", "C) temp = x; x = y; y = temp", "D) x + y; y = x; x = y"),
        ("A) List", "B) Tuple", "C) Set", "D) Dictionary"),
        ("A) The value of the variable", "B) The type of the variable", "C) The memory address of the variable", "D) The length of the variable"),
        ("A) Limited to the function it is defined in", "B) Limited to the module it is defined in", "C) Limited to the class it is defined in", "D) Limited to the block it is defined in"),
        ("A) int(string)", "B) convert(int, string)", "C) str_to_int(string)", "D) stringToInt(string)"),
        ("A) Lists","B) Dictionary","C) Tuples","D) Class"),
        ("A) List","B) dictionary","C) Tuple","D) Array"),
        ("A) int(x [,base])","B) long(x[,base])","C) float(x)","D) str(x)"),
        ("A) set","B) list","C) dict","D) Both B and C"),
        ("A) 4.5","B) 4.0","C) 4","D) Error"),
        ("A) more()","B) gt()","C) ge()","D) None of the above"),
        ("A) __or__()","B) __and__()","C) __xor__()","D) __rshift__()"),
        ("A) To define a function","B) To declare a variable","C) To execute a block of code conditionally","D) To create a loop"),
        ("A) ==","B) =","C) ===","D) >"),
        ("A) To handle exceptions","B) To create a loop","C) To define a function","D) To check additional conditions after the initial if statement"),
    )
    answers = ("C", "B", "D", "B", "C", "B", "B", "B", "B", "A","D","A","C","D","C","D","A","A","C","D")
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter the option(A,B,C,D): ").upper()
        guesses.append(guess)

        if guess == answers[question_num]:
            print(" ✅ Correct")
        else:
            print(f" ❌ Worng! The correct answer is {answers[question_num]}")
        question_num += 1

    for i in range(len(answers)):
        if guesses[i] == answers[i]:
            score += 1
    print(f" 🎯 Your Final Score: {score}/{len(answers)}")

    if score <= 10:
        print("You can practice more")
    else:
        print(" 🥳 Great job! keep practicing!")
python_game_quiz()
