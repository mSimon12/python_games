import random as rd

def random_word():
    '''
        Return a randon word
    '''
    # Get list of available words
    words_file = open("hangman_words.txt", 'r')
    words = words_file.read()
    words = words.split("\n")
    words_file.close()

    word = words[rd.randint(0, len(words))]
    word = word.upper()
    return word

def print_word(word, control):
    '''
        Print the secret word letters already discovered by the gamer
    '''
    print("SECRET WORD:  ", end='')
    for l in word:
        if(control[l]):
            print(f' {l}', end='')
        else:
            print(" _", end='')
    print()

def print_hangman(fails):
    '''
        Function to print the current status of the HangedMan.
        GAME OVER with 7 fails
    '''

    print("  _____  ")
    print("  |   |  ")
    if(fails == 0):
        print("  |")
        print("  |")
        print("  |")
        print("  |")
    elif(fails == 1):
        print("  |   O  ")
        print("  |")
        print("  |")
        print("  |")
    elif(fails == 2):
        print("  |   O  ")
        print("  |  /")
        print("  |")
        print("  |")
    elif(fails == 3):
        print("  |   O  ")
        print("  |  / \ ")
        print("  |")
        print("  |")
    elif(fails == 4):
        print("  |   O  ")
        print("  |  /|\ ")
        print("  |   |  ")
        print("  |")
    elif(fails == 5):
        print("  |   O  ")
        print("  |  /|\ ")
        print("  |   |  ")
        print("  |  / ")
    elif(fails == 6):
        print("  |   O  ")
        print("  |  /|\ ")
        print("  |   |  ")
        print("  |  / \ ")
    elif(fails > 6):
        print("  |  _X_     G    O")
        print("  |  /|\      A    V")
        print("  |   |        M    E")
        print("  |  / \        E    R!")

    print("  |      ")
    print("__|_     ")

def print_loser_msg():
    print("SORRY, YOU WERE HANGED!")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def print_winner_msg():
    print("CONGRATULATION, YOU FOUND THE SECRET WORD!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def play():
    print("\n\n*********************************")
    print("Welcome to the HangMan game!")
    print("*********************************")

    secret_word = random_word()
    
    # Variable to monitor discovered letters
    found_letters = {}                                              ## A dict with the status of each letter from the secret word
    for l in secret_word:
        found_letters[l] = False

    fails = 0
    hanged = lambda x: True if x > 6 else False                     ## True if 7 fails
    won = lambda f_l: True if all(list(f_l.values())) else False    ## verify if all letters were found

    while ((not hanged(fails)) and (not won(found_letters))):
        print_hangman(fails)
        print_word(secret_word,found_letters)

        letter = input("\nChoose a letter: ")
        letter = letter.strip().upper()

        if(secret_word.find(letter) >= 0):
            found_letters[letter] = True
        else:
            fails +=1

    if (won(found_letters)):
        print_winner_msg()
    else:
        print_hangman(fails)
        print_loser_msg()

    print(f'SECRET WORD: {secret_word}')


if __name__ == "__main__":
    play()