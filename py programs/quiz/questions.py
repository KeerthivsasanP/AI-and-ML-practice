from quizdb import data

class Question:
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer
        
    def check_answer(self,user_answer):
        return self.answer.lower() == user_answer.lower()

quiz = []
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
    if Question.check_answer(quiz[qno],user_ans):
        total_score += 1
    print(f"Correct answer is {quiz[qno].answer}\nYour current score {total_score}")

print(f"Your score = {total_score}")
   
