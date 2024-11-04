def hello(name, lang):
    greetings = {
        'English': 'Hello',
        'Spanish': 'Hola',
        'German': 'Hallo',
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    # The arguments
    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=['English', 'Spanish', 'German'], help="The language of the greeting."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )

    args = parser.parse_args()

    msg = f"Hello {args.name}!"

    hello(args.name, args.lang)

    # Running the code as it is will give you an error, as the argument -n/--name is required
    # Type 'py 15_argparse -h' in the console to see the help data
    # To provide the 'name', type 'py 15_argparse.py -n "yourname"'
