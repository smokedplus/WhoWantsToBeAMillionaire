import random


class Question():
    def __init__(self, question, correct_answer, fake_answer1, fake_answer2, fake_answer3):
        self.question = question
        self.correct_answer = correct_answer
        self.fake_answer1 = fake_answer1
        self.fake_answer2 = fake_answer2
        self.fake_answer3 = fake_answer3


set_of_questions = []


def create_questions():
    while True:
        user_choice2 = input(
            "Would you like to view the current questions, make a question, or go back to the start screen? Input View, Make, or Back.\n")
        if user_choice2 == "View":
            for question in set_of_questions:
                print("Q: " + question.question + " A: " + question.correct_answer+ "\n")
            continue
        elif user_choice2 == "Make":
            question = input("What question would like to add?\n")
            correct_answer = input("What is the answer to " + question + "\n")
            fake_answer1 = input("Input the 1st fake answer.\n")
            fake_answer2 = input("Input the 2nd fake answer.\n")
            fake_answer3 = input("Input the 3rd fake answer.\n")
            temp_question = Question(question, correct_answer, fake_answer1, fake_answer2, fake_answer3)
            set_of_questions.append(temp_question)
            continue
        elif user_choice2 == "Back":
            break

def start_screen():
    user_choice = input("Do you want to play the game or create a set of questions? Input Play or Create.")
    if user_choice == "Play":
        questions_number = input("How many questions would you like?")
        for i in range(0, questions_number):
            continue
    elif user_choice == "Create":
        create_questions()


start_screen()






