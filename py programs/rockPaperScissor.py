import random

rpc = ['Rock','Paper','Scissor']
print("0-Rock 1-Paper 2-Scissor")
user_choice = int(input("Enter your choice(0,1,2)"))
if (user_choice < 0 or user_choice > 2):
    print("invalid input")
else:
    computer_choice = random.randint(0,2)
    result = [["Draw","You lose","You win"],["You win","Draw","You lose"],["You lose","You win","Draw"]]
    fruit = ['apple','banana']

    print(f"you chose \n  {rpc[user_choice]}")
    print(f"computer chose \n {rpc[computer_choice]}")
    print(result[user_choice][computer_choice])
