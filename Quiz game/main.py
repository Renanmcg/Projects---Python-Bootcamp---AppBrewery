from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    item = Question(item["text"], item["answer"])
    question_bank.append(item)

# for question in question_data:
    # question_text = question["text"]
    # question_answer = question["answer"]
    # new_question = Question(question_text, question_answer)
    # question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You completes your quiz!")
print(f"Your score is: {quiz.score}/{len(question_bank)}")