
import random as rd
from .higher_lower_data import data, logo, vs
import os

def get_oponent(winner = ''):
    '''
        Return an oponent that is different from the current one
    '''
    while True:
        candidate = rd.choice(data)
        if candidate['name'] != winner:
            return candidate

def get_winner(candidates):
    '''
        Compare the number of followers of both candidates and return the list index from the winner
    '''
    if len(candidates) != 2 or type(candidates) != list:
        return -1
    
    if candidates[0]['follower_count'] >= candidates[1]['follower_count']:
        return 0
    else:
        return 1


def play():

    last_winner = get_oponent()
    score = 0

    print(logo)
    while True:
        new_oponent = get_oponent(last_winner['name'])

        print(f"Option A: {last_winner['name']}, a {last_winner['description']} from {last_winner['country']}.")
        print(vs)
        print(f"Option B: {new_oponent['name']}, a {new_oponent['description']} from {new_oponent['country']}.")

        # Show to the user and get user option
        option = input("Who has more followers? Type 'A' or 'B': ")

        candidates = [last_winner, new_oponent]
        winner_idx = get_winner(candidates)
        if (option.lower() == 'a' and winner_idx == 0) or (option.lower() == 'b' and winner_idx == 1):
            score +=1
        else:
            print(f"\nWrong option!\nYour final score is {score}!")
            return
        
        os.system('cls||clear')
        print(logo)
        print(f"You are right! Current score: {score}")
        last_winner = candidates[winner_idx]

if __name__ == "__main__":
    play()