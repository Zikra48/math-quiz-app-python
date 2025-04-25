from quiz.questions import Question
from quiz.quiz import Quiz

# Sample questions (you can later load from JSON or a file)
question_bank = [
    Question(
        text="What is the derivative of x²?",
        options=["A. x", "B. 2x", "C. x²", "D. 1"],
        correct_answer="B"
    ),
    Question(
        text="What is the integral of 2x?",
        options=["A. x²", "B. 2x²", "C. x", "D. 1"],
        correct_answer="A"
    ),
    Question(
        text="What is the value of π (approximately)?",
        options=["A. 2.14", "B. 3.14", "C. 3.41", "D. 2.71"],
        correct_answer="B"
    ),
    Question(
        text="What is the square root of 144?",
        options=["A. 11", "B. 13", "C. 12", "D. 14"],
        correct_answer="C"
    )
]

def run_quiz():
    print("🧠 Welcome to the Math Quiz App!\n")
    quiz = Quiz(question_bank)

    while quiz.has_more_questions():
        question = quiz.get_next_question()
        question.display()
        answer = input("Your answer (A/B/C/D): ")
        
        if question.check_answer(answer):
            print("✅ Correct!")
            quiz.increment_score()
        else:
            print(f"❌ Incorrect. The correct answer was {question.correct_answer.upper()}.")

    quiz.display_score()
    print("\nThanks for playing! 🎉")

if __name__ == "__main__":
    run_quiz()
