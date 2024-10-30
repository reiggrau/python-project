import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True

# print(RPS(1))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)

# Rock, Paper, Scissors game
playerscore = 0
computerscore = 0

while playagain:
    # 1. Computer choice
    computerchoice = random.choice('123')   # String type!

    computer = int(computerchoice)

    # 2. Ask player input
    playerchoice = input(
        "\nChose one: \n 1 for Rock \n 2 for Paper \n 3 for Scissors:\n\n")    # String type!

    player = int(playerchoice)

    # 3. Input check
    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2 or 3.")  # This will exit the program

    # 4. Reveal choices
    print("")
    print("You chose " + str(RPS(player)).replace('RPS.', '') + "!")
    print("The computer chose " + str(RPS(computer)).replace('RPS.', '') + "!")
    print("")

    # 5. Calculate match results
    if player == 1 and computer == 3:
        print("You win! 🤩")
        playerscore += 1
    elif player == 2 and computer == 1:
        print("You win! 🤩")
        playerscore += 1
    elif player == 3 and computer == 2:
        print("You win! 🤩")
        playerscore += 1
    elif player == computer:
        print("It's a draw! 😬")
    else:
        print("You lose! 😵")
        computerscore += 1

    # 6. Rematch?
    playagain = input("\nPlay again?\n Y for Yes\n N for No\n")

    if playagain.lower() == 'y':
        # 7. Scores
        print('Scores'.center(10, "="))
        print('Player ' + str(playerscore))
        print('Computer ' + str(computerscore))
        continue
    else:
        break
