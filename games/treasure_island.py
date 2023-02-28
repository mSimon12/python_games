logo = '''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    '''

def play():
    print(logo)
    print("Welcome to Treasure Island")
    print("Your mission is to find the treasure.")

    option = input("You are at a cross road. Where do you want to go?\nType 'left' or 'right': ")

    if (option.lower() == "left"):
        option = input("You came to a lake. There is a island in the middle of the lake. \nType 'wait' to wait for a boat or 'swim' to swim across: ")
        
        if (option.lower() == "wait"):
            option = input("You arrived at the Island unharmed. There is a house with three doors. One red, one yellow and one blue.\nWhich colour do you choose: ")
            
            if (option.lower() == "yellow"):
                print("\nCongratulations!!! You found the treasure.")
            elif (option.lower() == "red"):
                print("\nAn assassin is inside and he killed you. GAME OVER!!!")
            elif (option.lower() == "blue"):
                print("\nThere is a philosopher and you got so tedious and died. GAME OVER!!!")
            else:
                print("\nUnavailable option. GAME OVER!!!")
        elif (option.lower() == "swim"):
            print("\nAn alligator killed you. GAME OVER!!!")
        else: 
            print("\nUnavailable option. GAME OVER!!!")
    elif (option.lower() == "right"):
        print("\nYou faced a Monster and he killed you. GAME OVER!!!")
    else: 
        print("\nUnavailable option. GAME OVER!!!")

if __name__ == "__main__":
    play()