import random

name_list=["Alex","Charlie","Phil","Arun","Mike","Keerthivasan"]
students_score = {name:random.randint(1,100) for name in name_list}
print(students_score)

passed_student = {student:score for (student,score) in students_score.items() if score >= 60}
print(passed_student)
