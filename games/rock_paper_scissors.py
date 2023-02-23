
import random as rd

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

vs = '''
\ \  / /
 \ \/ /
  \  /  
  /  \ 
 / /\ \ 
/ /  \ \ 
'''

options = ['Rock', 'Paper', 'Scissor', rock, paper, scissors]


def play():
    print("Welcome to Rock, Paper or Scissors!")
    op = int(input(f"Choose your play.\n{options[0]}(0), {options[1]}(1) or {options[2]}(2): "))

    if (op < 0 or op > 2):
        print("Unavailable option!")
    else:
        print(f"You played {options[op]}")
        print(options[op+3])

        print(vs)

        cpu_op = rd.randint(0,2)
        print(options[cpu_op+3])
        print(f"CPU played {options[cpu_op]}")

        print(f"\n{options[op]} x {options[cpu_op]}")

        if ((op == 0) and (cpu_op == 2)):
            print("You won!")
        elif ((cpu_op == 0) and (op == 2)):
            print("CPU won!")
        elif (op > cpu_op):
            print("You won!")
        elif (cpu_op > op):
            print("CPU won!")
        elif (cpu_op == op):
            print("It is a draw!")

if __name__ == "__main__":
    play()