# While loop
value = 0
while value <= 10:
    value += 1
    if value == 1:
        continue  # 'continue' jumps to the next loop
        # WARNING: Do not put 'continue' before updating the iteration counter
    if value == 5:
        break  # 'break' exits the loop
    print(value)
else:
    print('Loop complete!')  # Will run at loop end if no 'break' has ocurred

# 'For' loops
# List loop
list = ['Dave', 'Sara', 'John']
for name in list:
    print(name)

# String loop
for letter in 'Reig':  # You can loop through strings
    print(letter)

# Tuple loop
tuple = (1, 2, 3)

for x in tuple:
    print(x)

# Set loop
set = {7, 8, 9}

for n in set:
    print(n)  # 8, 9, 7 => Sets are unordered!

# Dictionary loop
dict = {'player1': 'Guillem', 'player2': 'Dave', 'player3': 'Sara'}

for key, value in dict.items():  # use .items()
    print(key, value)

# Range loop
for x in range(4):
    print(x)  # 0, 1, 2, 3 (starts at 0)

for x in range(0, 25, 5):  # Start at 0, until 25 (excluded), in increments of 5
    print(x)  # 0, 5, 10, 15, 20
else:
    print('Loop over!')

# Nested loops
names = ['Dave', 'Sara', 'John']
actions = ['codes', 'eats', 'sleeps']

for name in names:
    for action in actions:
        print(name + ' ' + action + '.')

# Example
value = True
count = 0

while value:
    count += 1
    print(count)
    if (count == 5):
        break
    else:
        value = 0
        continue
