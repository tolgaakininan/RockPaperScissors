import random as rand
import os
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
computerWon=0
playerWon=0
game=True
while game==True:
    playerPlay=input("Rock Paper or Scissors ").lower()
    os.system('cls')
    if playerPlay=="rock":
        print(f"Player chose:\n{rock}")
    elif playerPlay=="paper":
        print(f"Player chose:\n{paper}")
    elif playerPlay=="scissors":
        print(f"Player chose:\n{scissors}")
    computerNum=rand.randint(1,3)
    if computerNum==1:
        computerPlay="rock"
        print(f"Computer chose:\n{rock}")
    elif computerNum==2:
        computerPlay="paper"
        print(f"Computer chose:\n{paper}")
    elif computerNum==3:
        computerPlay="scissors"
        print(f"Computer chose:\n{scissors}")
    
    if computerPlay=="rock" and playerPlay=="scissors" or computerPlay=="paper" and playerPlay=="rock" or computerPlay=="scissors" and playerPlay=="paper":
            print("Computer Won!")
            computerWon+=1
    elif playerPlay=="rock" and computerPlay=="scissors" or playerPlay=="paper" and computerPlay=="rock" or playerPlay=="scissors" and computerPlay=="paper":
            print("Player Won!")
            playerWon+=1
    else:
            print("Draw!")
    if playerWon==3:
            print("Player Won The Match!")
            game=False
    elif computerWon==3:
            print("Computer Won The Match!")
            game=False
