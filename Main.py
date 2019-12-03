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
    "When was Marvel Entertainment LLC Founded ? \n(a) 1980 \n(b) "
    "2008 \n(c) 1998  \n(d) 1988" '\n',
    # c
    "What alien race does Ronan the Accuser belong to? \n(a) "
    "Kree \n(b) Celestials \n(c) Phalanx \n(d) Skrulls" '\n',
    # a
    "How many Infinity Stones are there in the MCU? \n(a) 10 \n(b) 5 \n(c) 6 "
    "\n(d) 3" '\n',
    # c
    "What team does Johnny Storm belong to? \n(a) The X-Men \n(b) The "
    "Fantastic 4 \n(c) The Avengers \n(d) None of the Above" '\n',
    # b
    "Who came first? \n(a) Detective Comics \n(b) Marvel" '\n',
    # a
    "What is Loki's last Name? \n(a) Surtur-son \n(b) Odin-son \n(c) "
    "Laufey-son \n(d) Urik-son" '\n',
    # c
    "Who is Thor's sister in the MCU? \n(a) Freya \n(b) Nanna \n(c) Thrud \n("
    "d) Hela" '\n',
    # d
    "Who can pick up Thor's hammer? \n(a) Loki \n(b) Iron Man \n(c) Pepper \n("
    "d) Captain America" '\n',
    # d
    "Who developed the super soldier serum in Captain America? \n(a) Dr. "
    "Schmidt \n(b) Dr. Wiesel \n(c) Dr. Zola \n(d) Dr. Erskine" '\n',
    # d
    "What is Abominations's real name? \n(a) Brock Rumlow \n(b) Emil "
    "Blonsky \n(c) Georges Batroc \n(d) Thunderbolt' Ross" '\n',
    # b
    "What was Sam Wilson before he became Falcon \n(a) A Navy Seal \n(b) A "
    "Para-rescue \n(c) A Pilot \n(d) A Professional Daredevil" '\n',
    # b
    "What is Star-Lord's Mother's Name? \n(a) Meredith Quill \n(b) Joan "
    "Quill \n(c) Jane Quill \n(d) Anna Quill" '\n',
    # a
    "What's Hawkeye's real name? \n(a) Barton Carter \n(b) Clint Coulson \n("
    "c) Clint Barton \n(d) Bart Clinton" '\n',
    # d
]

questions = [
    Question(question_number[0], "c"),
    Question(question_number[1], "a"),
    Question(question_number[2], "c"),
    Question(question_number[3], "b"),
    Question(question_number[4], "a"),
    Question(question_number[5], "c"),
    Question(question_number[6], "d"),
    Question(question_number[7], "d"),
    Question(question_number[8], "d"),
    Question(question_number[9], "b"),
    Question(question_number[10], "b"),
    Question(question_number[11], "a"),
    Question(question_number[12], "d")
]


def run_quiz(new_questions):
    """

    :param new_questions:
    :return:
    """
    score = 0
    for question in new_questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Your score is", score, "out of", len(new_questions))


def :
    pass


try:
    if len(score) == 12:
        print("You are a Marvel Genius!")
    elif len(score) < 6 > 12:
        print('You did great, but you may want to refresh your mind! \n '
              'Try Again!')
    else:
        print("Try again.")


print("Thank you for taking my quiz.I Hope you had fun!")

run_quiz(questions)
