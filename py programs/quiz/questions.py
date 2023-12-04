from quizdb import data

class Question:
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer

quiz = []
question_number=0
total_score = 0

for question in data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    quiz.append(new_question)
    
total_question = len(quiz)
print("Welcome to the quiz")

for qno in range(0,total_question):
    user_ans = input(f"Q{qno+1} . {quiz[qno].text} (True/False)")
    if user_ans == quiz[qno].answer:
        total_score += 1

print(f"Your score = {total_score}")
   
