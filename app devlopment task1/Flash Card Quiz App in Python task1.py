# Flash Card Quiz App in Python

import random

class FlashCardQuiz:
    def __init__(self):
        self.flashcards = {
            "What is the capital of India?": "Delhi",
            "What is 5 + 7?": "12",
            "Who developed Python?": "Guido van Rossum",
            "What planet is known as the Red Planet?": "Mars",
            "What is the largest ocean?": "Pacific"
        }
        self.score = 0

    def start_quiz(self):
        print("\n===== Flash Card Quiz App =====\n")

        questions = list(self.flashcards.items())
        random.shuffle(questions)

        for question, answer in questions:
            user_answer = input(f"{question}\nYour Answer: ")

            if user_answer.strip().lower() == answer.lower():
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! Correct Answer: {answer}\n")

        print("===== Quiz Finished =====")
        print(f"Your Score: {self.score}/{len(self.flashcards)}")


# Run App
quiz = FlashCardQuiz()
quiz.start_quiz()