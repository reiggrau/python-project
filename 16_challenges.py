import rps
import guess


def arcade(name='Player'):
    def play_arcade():
        # 1. Select game
        playerchoice = input(
            f"\n{name}, select a game: \n 1 for Rock, Paper, Scissors 🪨 🧻✂️ \n 2 for Guess The Number 🔢❓ \n\n Or 'x' for exit.\n")

        if playerchoice == 'x' or playerchoice == 'X':
            print(f'Goodbye {name}! 👋😊')
            return

        # 1b. Input check
        if playerchoice not in ['1', '2']:
            print(f"{name}, you must enter 1 or 2.")
            return play_arcade()

        # 2. Start selected game
        if playerchoice == '1':
            rock_paper_scissors = rps.rps(name)  # This creates closure
            rock_paper_scissors()
        if playerchoice == '2':
            guess_game = guess.guess(name)
            guess_game()
        else:
            return

    return play_arcade


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

    start_arcade = arcade(args.name)
    start_arcade()
