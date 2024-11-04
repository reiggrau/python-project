import sys
import random
from enum import Enum


def rps(name='Player'):
    # Rock, Paper, Scissors game
    playerscore = 0
    computerscore = 0
    gamecount = 0

    def play_rps():
        nonlocal name
        nonlocal playerscore
        nonlocal computerscore
        nonlocal gamecount

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        # 2. Computer choice
        computerchoice = random.choice('123')   # String type!
        computer = int(computerchoice)

        # 3a. Ask player input
        playerchoice = input(
            f"\n{name}, chose one: \n 1 for Rock 🪨 \n 2 for Paper 🧻 \n 3 for Scissors ✂️\n\n")

        # 3b. Input check
        if playerchoice not in ['1', '2', '3']:
            # This will exit the program
            sys.exit(f"{name}, you must enter 1, 2 or 3.")
            return play_rps()
        player = int(playerchoice)

        # 4. Reveal choices
        print("")
        print(f"{name} chose " + str(RPS(player)).replace('RPS.', '') + "!")
        print("The computer chose " +
              str(RPS(computer)).replace('RPS.', '') + "!")
        print("")

        # 5. Calculate match results
        def decide_winner(player, computer):
            nonlocal name
            nonlocal playerscore
            nonlocal computerscore
            nonlocal gamecount

            gamecount += 1

            if player == 1 and computer == 3:
                print(f"{name} wins! 🤩")
                playerscore += 1
            elif player == 2 and computer == 1:
                print(f"{name} wins! 🤩")
                playerscore += 1
            elif player == 3 and computer == 2:
                print(f"{name} wins! 🤩")
                playerscore += 1
            elif player == computer:
                print("It's a draw! 😬")
            else:
                print("You lose! 😵")
                computerscore += 1

        decide_winner(player, computer)

        # 6. Print scores
        print(f' Game {gamecount} '.center(10, "="))
        print(f'{name} ' + str(playerscore))
        print('Computer ' + str(computerscore))

        # 7. Rematch?
        playagain = input("\nPlay again?\n Y for Yes\n N for No\n")

        if playagain.lower() == 'y':
            return play_rps()
        else:
            print('Thank you for playing!')
            if __name__ == '__main__':
                sys.exit('Goodbye {name}! 👋😊')
            else:
                return

    return play_rps


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the player."
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)  # This creates closure
    rock_paper_scissors()
