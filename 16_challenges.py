import sys
from rps import rps
from guess import guess


def play_arcade(name='Player'):
    welcomeback = False

    while True:
        if welcomeback == True:
            print(f"\nWelcome back to the Arcade menu.")

        # 1. Select game
        playerchoice = input(
            "\nPlease select a game: \n 1 for Rock, Paper, Scissors 🪨 🧻✂️ \n 2 for Guess The Number 🔢❓ \n\n Or 'x' for exit.\n")

        # 1b. Input check
        if playerchoice.lower() not in ['1', '2', 'x']:
            print(f"{name}, you must enter 1, 2 or x.")
            return play_arcade()

        # 2. Start selected game
        welcomeback = True

        if playerchoice == '1':
            rock_paper_scissors = rps(name)  # This creates closure
            rock_paper_scissors()
        if playerchoice == '2':
            guess_game = guess(name)
            guess_game()
        else:
            sys.exit(f'Goodbye {name}! 👋😊')


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

    print(f"Welcome to the Arcade menu, {args.name}!")
    play_arcade(args.name)
