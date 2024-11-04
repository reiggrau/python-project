import sys
import random


def guess(name='Player'):
    playerscore = 0
    computerscore = 0
    gamecount = 0

    def play_guess():
        nonlocal playerscore
        nonlocal computerscore
        nonlocal gamecount

        # 1. Computer selects number
        computerchoice = random.choice('123')

        # 2. Player guess
        playerchoice = input(
            f"\n{name}, guess what number I'm thinking of... 1, 2 or 3.")

        # 2b. Input check
        if playerchoice not in ['1', '2', '3']:
            print(f"{name}, you must enter 1, 2 or 3.")
            return play_guess()

        # 3. Reveal choices
        print(f"\n{name}, you chose " + playerchoice + ".")
        print("I chose " + computerchoice + ".")

        # 4. Calculate match
        player = int(playerchoice)
        computer = int(computerchoice)

        def decide_winner(player, computer):
            nonlocal name
            nonlocal playerscore
            nonlocal computerscore
            nonlocal gamecount

            if (player == computer):
                print(f"\n{name}, you win!")
                playerscore += 1
            else:
                print(f"\n{name}, you lose!")
                computerscore += 1

            gamecount += 1

        decide_winner(player, computer)

        # 5. Display winning percentage
        winrate = playerscore / gamecount

        print(f"\nYour winning percentage: {winrate:.2%}")

        # 6. Play again?
        playagain = input("\nPlay again?\n Y for Yes\n N for No\n")

        if playagain.lower() == 'y':
            return play_guess()
        else:
            print('Thank you for playing!')
            if __name__ == '__main__':
                sys.exit('Goodbye {name}! 👋😊')
            else:
                return

    return play_guess


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

    guess_game = guess(args.name)
    guess_game()
