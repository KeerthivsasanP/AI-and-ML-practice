from gameDB import data
from random import randint

total = len(data["objects"])
print(total)
first = randint(0,total-1)
second = first + 1
firstData = data["objects"][first%total]["name"]
firstValue = data["objects"][first%total]["value"]
secondData = data["objects"][second%total]["name"]
secondValue = data["objects"][second%total]["value"]
score = 0
nextlevel = True

while(nextlevel):
    print("Guess which would have higher search?")
    print("1." + firstData +" or "+ "2."+secondData)
    user_input = int(input("Type 1 for first value  2 for second value 3 for DRAW\n"))
    winning_condition = (user_input == 1 and firstValue > secondValue) or (user_input == 2 and secondValue > firstValue) or (user_input == 3 and secondValue == firstValue)
    if (winning_condition):
        first = second
        second += 1
        firstData = secondData
        firstValue = secondValue
        secondData = data["objects"][second % total]["name"]
        secondValue = data["objects"][second % total]["value"]
        score += 1

    elif (not winning_condition):
        print("You lost")
        nextlevel = False
        
print(f"Your score is {score}")
