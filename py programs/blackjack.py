import random

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
