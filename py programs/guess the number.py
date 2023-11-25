import random

random_numb = random.randint(1,100)
print(random_numb)
user_input = 0

level = input("Choose the level 'hard' or 'easy'")

if level == 'easy':
    chance = 10
else:
    chance = 5

while (user_input != random_numb):
    user_input = int(input("Guess the number"))
    if user_input == random_numb:
        print("You guessed it right")
        break
    elif user_input > random_numb:
        print("Too high")
    else:
        print("Too low")
    chance -= 1
    print(f"You have got {chance} more change")
    
