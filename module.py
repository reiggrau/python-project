from random import choice

capital = 'Topeka'

bird = "Western Meadowlark"

flower = 'Sunflower'

song = "More on the Range"


def randomfunfact():
    funfacts = [
        "Kansas is considered flat, but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess that it is Kansas City.",
        "A considerable portion of Kansas City is actually in Missouri.",
        "Most Kansans are annoyed by Wizard of Oz references from people outside of Kansas."
    ]

    index = choice('0123')

    print(funfacts[int(index)])


if __name__ == '__main__':  # This will trigger only if we run this file directly
    randomfunfact()  # If this was outside the 'if' block it would run at module import
