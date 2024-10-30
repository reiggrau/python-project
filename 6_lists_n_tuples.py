# Lists (Arrays in JS)
# List is one of 4 built-in data types in Python used to store collections of data.
# The other 3 are Tuple, Dictionary and Set, all with different qualities and usage.

# List items are ordered, changeable, and allow duplicate values.

users = ['Guillem', 'Dave', 'John', 'Sara']

data = list(['Guillem', 34, True])

emptylist = []

print(type(users))  # <class 'list'>

# Value at index
# List items are indexed, the first item has index [0], the second item has index [1] etc.
print(users[0])         # Guillem
print(users[-2])        # John (2nd from end)

# in (includes?)
print('Dave' in users)  # True

# Get index of value
print(users.index('Sara'))  # 3

# Get a list slice (end not included)
print(users[0:2])       # ['Guillem', 'Dave']
print(users[1:])        # ['Dave', 'John', 'Sara']
print(users[-3:-1])     # ['Dave', 'John']

# Get list length
print(len(users))    # 4

# Add item to a list
users.append('Elsa')
users += ['Jason']  # Don't forget the brackets
users.extend(['Robert', 'Jimmy'])

users.insert(0, 'Bob')  # insert at position 0
users[2:2] = ['Eddie', 'Alex']  # insert at position 2

# ['Bob', 'Guillem', 'Eddie', 'Alex', 'Dave', 'John', 'Sara', 'Elsa', 'Jason', 'Robert', 'Jimmy']
print(users)

# Remove items
print(users.pop())  # Removes last
del users[0]  # Removes at index

# del data
data.clear()
print(data)

# Sort
users.sort()  # This is case-sensitive
print(users)

users.sort(key=str.lower)  # This sort is case-insensitive

nums = [4, 42, 78, 1, 5]
nums.sort(reverse=True)  # Sort in reverse order
print(nums)

# Reverse
nums.reverse()
print(nums)

# Avoid list mutation
print(sorted(nums, reverse=True))   # This preserves the original list
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
print(mycopy)

# Tuples
# A tuple is a collection which is ordered, unchangeable, and allows duplicate values.

mytuple = ('Guillem', 34, True)
anothertuple = tuple((1, 2, 2, 3, 4))

print(mytuple)
print(type(mytuple))

# Create list from tuple
newlist = list(mytuple)

newlist.append('Developer')
newtuple = tuple(newlist)
print(newtuple)

# Unpacking a tuple
(name, age, *position) = newtuple   # * creates a list
print(name, age, position)  # Guillem 34 [True, 'Developer']

# Tuple count
print(anothertuple.count(2))    # 2 (counts how many times an element)
