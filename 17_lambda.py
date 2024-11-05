# Lambda functions
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

from functools import reduce
def squared(num): return num * num  # squared = lambda num : num * num


print(squared(3))


def sum_total(a, b): return a + b  # sum = lambda a, b: a + b


print(sum_total(37, 7))


####################

def function_builder(x):
    return lambda num: num + x


add_ten = function_builder(10)
add_twenty = function_builder(20)

print(add_ten(7))
print(add_twenty(7))

# Higher-order functions
# is a function that does at least one of the following:
# - Takes one or more functions as arguments
# - Returns a function or value as its result

# map()
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

# filter()
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

# reduce()

total = reduce(lambda acc, curr: acc + curr,
               numbers, 100)  # 100 is starting value (optional)

print(total)

print(sum(numbers, 100))  # built-in sum function

#

names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimer Schmidt']


# We need a starting value because we are using strings
char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)
