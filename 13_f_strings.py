person = 'Dave'
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

print("\n%s has %s coins left." % (person, coins))  # Old method

print("\n{} has {} coins left.".format(person, coins))  # format() method

print("\n{1} has {0} coins left.".format(person, coins))  # Change order

print("\n{person} has {coins} coins left.".format(
    person='Guillem', coins='6'))  # Specific values

player = {'person': 'Rob', 'coins': 4}

print("\n{person} has {coins} coins left.".format(
    **player))  # Dictionary values (** required)

###############

# f-String method (recommended)
message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person.lower()} has {2 * 5} coins left."
print(message)

message = f"\n{player['person']} has {player['coins']} coins left."
print(message)

###############
# You can pass formatting options

num = 10
# We specify to always display 2 decimals, 0s included
print(f"\n2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 6):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 7):
    print(f"{num} divided by 6 is {num / 6:.2%}")

# Python String format() Method
# https://www.w3schools.com/python/ref_string_format.asp
