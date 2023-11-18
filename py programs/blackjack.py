import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
is_game = True

user_card = []
dealer_card = []

def get_card():
    return random.choice(cards) 
    

def calc_score(card_score):
    
    return sum(card_score)

def isGameOver(userScore,dealerScore):
    if dealerScore == 21 or userScore == 21:
        return True
    elif sum(user_card) > 21:
        return True

def result(userScore,dealerScore):
    if userScore == 0 and  dealerScore == 0:
        print("Draw")
    elif dealerScore == 0 or (dealerScore < 21 and userScore > dealerScore):
        print("Dealer wins")
    elif userScore == 0 or (userScore < 21 and userScore <  dealerScore):
        print("You win")
    elif userScore < 21 and dealerScore < 21:
        if (userScore > dealerScore):
            print("You win")
        elif(userScore < dealerScore):
            print("Dealer wins") 
        else :
            print("Draw")       

for _ in range(2):
    user_card.append(random.choice(cards))
    dealer_card.append(random.choice(cards))

user_choice = True

dealerScore = calc_score(dealer_card)
userScore = calc_score(user_card)

if isGameOver(userScore,dealerScore):
    result()

while user_choice:
    print(f"Your cards {user_card}")
    print(f"User current score = {calc_score(user_card)}")
    print(f"Dealer cards {dealer_card}")
    print(f"Dealer current score = {calc_score(dealer_card)}")
    #print(f"dealer first card {dealer_card[0]}")
    if isGameOver(user_card,dealer_card):
        result(userScore,dealerScore)
        # print(f"Your cards {user_card}")
        # print(f"User current score = {calc_score(user_card)}")
        # print(f"Dealer cards {dealer_card}")
        # print(f"Dealer current score = {calc_score(dealer_card)}")
        break
    else:
        #print("Game not over")
        user_choice=input("Do you want to hit?")
        if user_choice == 'y':
            user_card.append(get_card())
            dealer_card.append(get_card()) 
        else:
            result(userScore,dealerScore)
            user_choice = False
