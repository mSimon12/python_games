
import random as rd

def play():
    print("\n\n*********************************")
    print("Welcome to the Guessing game!")
    print("*********************************")

    # Level selection
    print("Select the game difficulty")
    level= int(input("(1) Easy, (2) Medium, (3) Hard: "))
    print(f"You selected level {level}")

    if ((level > 3) or (level < 1)):
        print("Invallid option!!! Level must be from 1 to 3.")
        exit()

    if (level == 1):
        trials = 15
    elif (level == 2):
        trials = 10
    else:
        trials = 5    

    # Score
    score = 500

    # Secret number
    secret_num = rd.randint(1,100)

    # Game execution
    for i in range(1,trials+1):
        print("\nTrial {} of {}".format(i, trials))
        x = int(input("Guess the secret number (0-100):"))

        if ((x >= 100) or (x <= 0)):
            print("ERROR - the number must be between 0 and 100!")
            continue

        if (x == secret_num):
            print("Congratulations, you chose the right number")
            break
        else:
            if (i == trials):
                print("Game Over!")
                print("The secrete number is:", secret_num)
            elif (x > secret_num):
                print("Sorry, wrong number. Your guess was BIGGER than the secret number.")
            else:
                print("Sorry, wrong number. Your guess was SMALLER than the secret number.")
            
            score -= abs(x - secret_num)

    print(f"Your final score is {score}.")
    print("\nTHE END\n")

if __name__ == "__main__":
    play()