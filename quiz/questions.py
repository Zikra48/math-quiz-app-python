class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options  # List of options like ['A', 'B', 'C', 'D']
        self.correct_answer = correct_answer  # Example: 'B'

    def check_answer(self, user_answer):
        return user_answer.strip().lower() == self.correct_answer.lower()

    def display(self):
        print(f"\n{self.text}")
        for option in self.options:
            print(option)
