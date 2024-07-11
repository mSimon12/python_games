
from games import guessing, hangman, rock_paper_scissors, treasure_island, blackjack, higher_lower

print("*********************************")
print("Welcome Simon's games!")
print("*********************************")

# Game options
games_list = [
    "Guessing", 
    "HangMan", 
    "Rock_Paper_Scissors", 
    "Treasure_Island", 
    "BlackJack",
    "Higher_Lower"
    ]

print("Choose your game!")
for count, game in enumerate(games_list, start=1):
    print(f'({count}) {game}')

option = int(input("Game:"))

if((option <= len(games_list)) and (option > 0)):
    for count, game in enumerate(games_list, start=1):
        if (count == option):
            globals()[game.lower()].play()
else:
    print(f"Invalid option. Choose between 1 and {len(games_list)}")

