"""Little Rock paper scissors game using some ASCII designs."""

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

import random

#the opponent
RPC = [rock, paper, scissors] #criamos uma lsita para as opções
robot_hand = random.randint(0,2)


#the player
print("Welcome! This script is made for playing rock paper scissors!")
player_input = int(input("Which hand are you playing?(type 0 for rock, 1 for paper, 2 for scissors): "))
print("You played: \n" + RPC[player_input] + "\nRobot played: " + RPC[robot_hand])

#game logic

if player_input >= 3 or player_input < 0:
    print("You typed a wrong option, you lose!")
elif player_input == 0 and robot_hand == 2:
    print("You win!")
elif robot_hand == 0 and player_input == 2:
    print("You lose!")
elif robot_hand > player_input:
    print("You lose!")
elif player_input > robot_hand:
    print("You win!")
#elif player_input == robot_hand:
else:
    print("It's a tie!")