
from games import guessing, hangman, rock_paper_scissors, treasure_island, blackjack, higher_lower

print("*********************************")
print("Welcome to Pystation!")
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

def main():
    print("Choose your game!")
    for count, game in enumerate(games_list, start=1):
        print(f'({count}) {game}')
    option = int(input("Game:"))

    if (option <= len(games_list)) and (option > 0):
        game = games_list[option-1]
        globals()[game.lower()].play()
    else:
        print(f"Invalid option. Choose between 1 and {len(games_list)}")

if __name__ == "__main__":
    main()