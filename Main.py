"""
This is my main file for my project.
___author___ = Cristal Ramos
"""


# REMEMBER TO CITE EVERYTHING!
def main():
    """

    :return:
    """
    print("Welcome to 'Python Basics' tutorial!")
    print(
        "Read the main menu carefully to select which tutorial you'd like to "
        "see.")
    print("Main Menu")
    user_continue = True
    while user_continue:
        print(
            "Enter the number corresponding to the tutorial you want to see:")
        print("1. How to use Literal Strings ")
        print("2. How to use Input and Variables")
        print("3. How to use 7 Arithmetic Operations")
        print("4. How to use Formatting")
        print("5. How to use Boolean Expressions")
        print("6. How to use If/Else Statements")
        print("7. How to use Nested If/Else Statements")
        print("8. How to use While Loops")
        print("9. How to use For Loops")
        print("10. How to use Nested Loops")
        print("11. How to use Predefined functions")
        print("12. Exit")
        number = int(input())
        if number == 1:
            print("You have chosen the following tutorial 'How to use "
                  "Literal Strings'")
        # Fix indentation problem here
        elif number == 2:
            print("You have chosen the following tutorial 'How to use Input "
                  "and Variables'")
        elif number == 3:
            print("You have chosen the following tutorial 'How to use 7 "
                  "Arithmetic Operations'")
        elif number == 4:
            print("You have chosen the following tutorial 'How to use "
                  "Formatting'")
        elif number == 5:
            print("You have chosen the following tutorial 'How to use "
                  "Boolean Expressions'")
        elif number == 6:
            print("You have chosen the following tutorial 'How to use "
                  "If/Else Statements'")
        elif number == 7:
            print("You have chosen the following tutorial 'How to use "
                  "Nestled If/Else statements'")
        elif number == 8:
            print("You have chosen the following tutorial 'How to use While "
                  "Loops'")
        elif number == 9:
            print("You have chosen the following tutorial 'How to use For "
                  "Loops'")
        elif number == 10:
            print("You have chosen the following tutorial 'How to use "
                  "Nestled Loops'")
        elif number == 11:
            print("You have chosen the following tutorial 'How to use "
                  "Predefined functions'")
        elif number == 12:
            print("Thank you for using my tutorial Program. I hope you "
                  "enjoyed it.")
        else:
            user_continue = False
            print("Error: Invalid Selection")
            print("Please enter a choice from the main menu.")


main()


# This is my New Trivia Game, Mat Dane gave me the Inspiration For A Template

class Question:
    """
    
    """
    def __init__(self, number, answer):
        """
        
        :param number: 
        :param answer: 
        """
        self.prompt = number
        self.answer = answer


question_number = [
    "What color are apples?\n(a) Red/Green\n(b)Orange",
    "What color are bananas?\n(a) Red/Green\n(b)Yellow",
]

questions = [
    Question(question_number[0], "a"),
    Question(question_number[1], "b"),
]


def run_quiz(questions):
    """
    
    :param questions: 
    :return: 
    """
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got", score, "out of", len(questions))


run_quiz(questions)
