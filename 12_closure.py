# Python closure is a nested function that allows us to access variables of the outer function
# even after the outer function is closed.
def parent_function(person, coins):  # These variables also remain
    # coins = 3  # This variable remains after the function ends

    def play_game():
        nonlocal coins  # we need to use 'nonlocal' because we change the variable's value
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")

        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")

        else:
            print("\n" + person + " is out of coins.")

    return play_game


tommy = parent_function("Tommy", 3)  # Here is where the number of coins is set
jenny = parent_function("Jenny", 5)

tommy()  # 2
tommy()  # 1

jenny()  # 4

tommy()  # 0
