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

opponent_choice=int(input("What do you choose?\ntype 0 for rock, 1 for paper, 2 for scissors"))
if opponent_choice==0:
    print(rock)
elif opponent_choice==1:
    print(paper)
elif opponent_choice==2:
    print(scissors)
else:
    print("invalid no. You lose.") 
    import sys
    sys.exit()

choices=[rock,paper,scissors]
import random
number=random.randint(0,2)
computer_choice=choices[number]
print(computer_choice)
if computer_choice == rock and opponent_choice == 1:
    print("You win")
elif computer_choice == paper and opponent_choice == 2:
    print("You win")
elif computer_choice == scissors and opponent_choice == 0:
    print("You win")
elif computer_choice ==rock and opponent_choice== 0:
    print("It's a draw")
elif computer_choice == scissors and opponent_choice == 2:
    print("It's a draw")
elif computer_choice == paper and opponent_choice==1:
    print("It's a draw")
else:
    print("You lose")
