import random

class Quiz:
    def __init__(self, questions):
        self.questions = random.sample(questions, len(questions))  # Shuffle questions
        self.current_index = 0
        self.score = 0

    def has_more_questions(self):
        return self.current_index < len(self.questions)

    def get_next_question(self):
        question = self.questions[self.current_index]
        self.current_index += 1
        return question

    def increment_score(self):
        self.score += 1

    def display_score(self):
        print(f"\nYour final score: {self.score} / {len(self.questions)}")
