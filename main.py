import json
from quiz.question import Question
from quiz.quiz import Quiz

# Load questions from the JSON file
def load_questions():
    with open('questions.json', 'r') as file:
        data = json.load(file)
        questions = [Question(q['text'], q['options'], q['correct_answer']) for q in data]
    return questions

def run_quiz():
    print("🧠 Welcome to the Math Quiz App!\n")
    
    questions = load_questions()
    quiz = Quiz(questions)

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
