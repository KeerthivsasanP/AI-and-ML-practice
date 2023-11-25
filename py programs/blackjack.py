import random
<<<<<<< HEAD

play = True

while play:
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

    user_card = []
    dealer_card = []
    isGameOver = False

    def pick_card():
        return random.choice(cards)

    for _ in range(2):
        user_card.append(pick_card())
        dealer_card.append(pick_card())



    def calc_score(card): 
        if sum(card)==21 and len(card)==2:
            return 0
        if 11 in card and sum(card) > 21:
            card.remove(11)
            card.append(1)

        return sum(card)

    def compare_score(user_score,dealer_score):
        if user_score == 0 and dealer_score == 0:
            return ("Draw")
        elif user_score == 0:
            return ("You win")
        elif dealer_score == 0:
            return ("Dealer wins")
        elif user_score > 21:
            return ("Busted. You lost")
        elif dealer_score > 21:
            return ("Dealer busted. You win")
        elif user_score > dealer_score:
            return ("You win")
        else:
            return ("Dealer wins")

    while not isGameOver:
        user_score = calc_score(user_card)
        dealer_score = calc_score(dealer_card)

        print(f"user cards = {user_card} and score = {user_score}")
        print(f"Dealer first card is {dealer_card[0]}")

        if user_score == 0 or dealer_score == 0:
            isGameOver = True
        else:
            hit = input("Do you want a card? (y/n)")
            if hit == 'y':
                user_card.append(pick_card())
                user_score = calc_score(user_card)
                if user_score > 21:
                    break
            else:
                isGameOver = True

    while dealer_score !=0 and dealer_score < 17:
        dealer_card.append(pick_card())
        dealer_score = calc_score(dealer_card)

    print(f"Your final card: {user_card} , you score = {user_score}")
    print(f"Dealer final card: {dealer_card} , dealer score = {dealer_score}")

    print(compare_score(user_score,dealer_score))


    play = input("Do you want to play black jack?")
    if play != 'y':
        play = False
=======
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
>>>>>>> 80598e4354e6f32a0fc2efdcf99f7bd931419f9c
