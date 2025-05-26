print(r'''
 _____       _       _____                      
|  _  |     (_)     |  __ \                     
| | | |_   _ _ ____ | |  \/ __ _ _ __ ___   ___ 
| | | | | | | |_  / | | __ / _ | '_  _ \ / _ \
\ \/' / |_| | |/ /  | |_\ \ (_| | | | | | |  __/
 \_/\_\\__,_|_/___|  \____/\__,_|_| |_| |_|\___|

''')
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

print(
    "NOTE: IN THE QUIZ, PLEASE TYPE THE ACTUAL ANSWERS INSTEAD OF THE OPTION LETTERS, OTHERWISE THE ANSWER WILL NOT BE ACCEPTED.\nFor long answers or answers you cannot type with your keyboard, just copy and paste the answer.")

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_wrong_answer = question["incorrect_answers"]
    new_question = Question(question_text, question_answer, question_wrong_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}.")
