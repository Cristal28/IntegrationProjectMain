"""
This is my main file for my project.
___author___ = Cristal Ramos
"""

# REMEMBER TO CITE EVERYTHING!
# def main():
#    """
#    :return:
#  """
#    print("Welcome to 'Python Basics' tutorial!")
#    print(
#        "Read the main menu carefully to select which tutorial you'd like to "
#        "see.")
#    print("Main Menu")
#    user_continue = True
#    while user_continue:
#        print(
#            "Enter the number corresponding to the tutorial you want to see:")
#        print("1. How to use Literal Strings ")
#        print("2. How to use Input and Variables")
#        print("3. How to use 7 Arithmetic Operations")
#        print("4. How to use Formatting")
#        print("5. How to use Boolean Expressions")
#        print("6. How to use If/Else Statements")
#        print("7. How to use Nested If/Else Statements")
#        print("8. How to use While Loops")
#        print("9. How to use For Loops")
#        print("10. How to use Nested Loops")
#        print("11. How to use Predefined functions")
#        print("12. Exit")
#        number = int(input())
#        if number == 1:
#            print("You have chosen the following tutorial 'How to use "
#                  "Literal Strings'")
# Fix indentation problem here
#        elif number == 2:
#            print("You have chosen the following tutorial 'How to use Input "
#                  "and Variables'")
#        elif number == 3:
#            print("You have chosen the following tutorial 'How to use 7 "
#                  "Arithmetic Operations'")
#        elif number == 4:
#            print("You have chosen the following tutorial 'How to use "
#                  "Formatting'")
#        elif number == 5:
#            print("You have chosen the following tutorial 'How to use "
#                  "Boolean Expressions'")
#        elif number == 6:
#            print("You have chosen the following tutorial 'How to use "
#                  "If/Else Statements'")
#        elif number == 7:
#            print("You have chosen the following tutorial 'How to use "
#                  "Nestled If/Else statements'")
#        elif number == 8:
#            print("You have chosen the following tutorial 'How to use While "
#                  "Loops'")
#        elif number == 9:
#            print("You have chosen the following tutorial 'How to use For "
#                  "Loops'")
#        elif number == 10:
#            print("You have chosen the following tutorial 'How to use "
#                  "Nestled Loops'")
#        elif number == 11:
#            print("You have chosen the following tutorial 'How to use "
#                  "Predefined functions'")
#        elif number == 12:
#            print("Thank you for using my tutorial Program. I hope you "
#                  "enjoyed it.")
#        else:
#            user_continue = False
#            print("Error: Invalid Selection")
#            print("Please enter a choice from the main menu.")


# main()

# This is my New Trivia Game, Mat Dane gave me the Inspiration For A Template


print("Welcome to my Trivia Quiz!")
print("This is a quiz on the Marvel Universe which includes the comic books "
      "and the movies.")
print("DIRECTIONS: Please enter your selection and hit enter. You receive a "
      "point for every "
      "question "
      "you get "
      "right.")


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
    "Who was the First Avenger according to the movies? \n(a) Thor \n(b) "
    "IronMan \n(c) Captain "
    "America \n(d) Hulk" '\n',
    "What alien race does Ronan the Accuser belong to? \n(a) "
    "Kree \n(b) Celestials \n(c) Phalanx \n(d) Skrulls" '\n',
    "How many Infinity Stones are there in the MCU? \n(a) 10 \n(b) 5 \n(c) 6 "
    "\n(d) 3" '\n',
]

questions = [
    Question(question_number[0], "c"),
    Question(question_number[1], "a"),
    Question(question_number[2], "c"),

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
    print("Your score is", score, "out of", len(questions))


print("Thank you for taking my quiz. I Hope you had fun! :)")

run_quiz(questions)
