#RPS.py
#Name: Brennan Wood
#Date: 2/6/25
#Assignment: Lab 3 (RPS)

import random

def main():
  wins = 0
  ties = 0
  losses = 0

  playAgain = "Y"
  while playAgain == "Y":
    # Computer choice
    
    computer = random.choice(["R", "P", "S"])
    
    # Prompt the user for their RPS selection
    
    player = input("Choose your weapon (R, P, S): ")
    
    # Print who chose what
    
    if player == "R":
      print("Player chose Rock,")
    elif player == "P":
      print("Player chose Paper,")
    elif player == "S":
      print("Player chose Scissors,")
    else:
      player = "S"
      print("We chose Scissors for player, please choose R, P, or S :)")
    
    if computer == "R":
      print("Computer chose Rock,")
    elif computer == "P":
      print("Computer chose Paper,")
    elif computer == "S":
      print("Computer chose Scissors,")

      # Determine outcome and state what happened to the user

    # RP
    if computer == "R" and player == "P":
      print("Player wins!")
      wins = wins + 1

    # RS
    if computer == "R" and player == "S":
      print("Computer wins!")
      losses = losses + 1

    # PR
    if computer == "P" and player == "R":
      print("Computer wins!")
      losses = losses + 1

    # PS
    if computer == "P" and player == "S":
      print("Player wins!")
      wins = wins + 1

    # SR
    if computer == "S" and player == "R":
      print("Player wins!")
      wins = wins + 1

    # SP
    if computer == "S" and player == "P":
      print("Computer wins!")
      losses = losses + 1
    
    # TIES
    if computer == "R" and player == "R" or computer == "P" and player == "P" or computer == "S" and player == "S":
        print("It's a tie!")
        ties = ties + 1
    
    # Ask the user if they would like to play again.
    playAgain = input("Would you like to play again? (Y/N): ")

  #In the end, print the stats

  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
  print("\033[91mRock Paper Scissors\033[0m")
