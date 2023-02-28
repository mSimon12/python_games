
import random as rd

def get_card():
    '''
        Randomly return a card from the deck
    '''
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    return rd.choice(cards)

def get_score(cards):
    '''
        Return the score according the given cards
    '''
    score = 0
    aces = 0
    for c in cards:
        if c in ['J', 'Q', 'K']:
            score += 10
        elif c == 'A':
            aces += 1
        else:
            score += c

    while aces:
        if (score + aces*11) > 21:
            score +=1
        else:
            score += aces*11
        aces -=1

    return score

def play():
    print("\n\n*********************************")
    print("Welcome to Blackjack!")
    print("*********************************")

    dealer_cards = []
    player_cards = []

    player_cards.append(get_card())
    player_cards.append(get_card())

    dealer_cards.append(get_card())

    while True:
        print(f"\nPlayer cards: {player_cards} = {get_score(player_cards)} points")
        print(f"Dealer cards: {dealer_cards} = {get_score(dealer_cards)} points")

        if get_score(player_cards) > 21:
            print(f"\nPLAYER LOSE!")
            return
        
        op = input("Do you want another card? 'y' or 'n': ")

        if (op != 'y'):
            break

        player_cards.append(get_card())
        

    while(get_score(dealer_cards) < 17):
        dealer_cards.append(get_card())
        print(f"\nPlayer cards: {player_cards} = {get_score(player_cards)} points")
        print(f"Dealer cards: {dealer_cards} = {get_score(dealer_cards)} points")


    if (get_score(player_cards) > get_score(dealer_cards)) or (get_score(dealer_cards) > 21):
        print("\nPLAYER WINS!")
    elif get_score(player_cards) < get_score(dealer_cards):
        print("\nPLAYER LOSE!")
    else:
        print("\nDRAW!")    


if __name__ == "__main__":
    play()