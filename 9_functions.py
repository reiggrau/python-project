def hello_world():
    print("Hello world!")


hello_world()


def sum(num1, num2):
    return num1 + num2


total = sum(1, 2)

print(total)

# Check correct input type


def safesum(num1=0, num2=0):  # Default values
    if (type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2


print(safesum('1', 2))  # None
print(safesum())  # 0 (defaults are used, otherwise ERROR)

# Unknown number of arguments


def multiple_items(*args):  # with *
    print(args)
    print(type(args))


multiple_items('Guillem', 34, True)

# Use key/word arguments


def mult_named_items(**kwargs):  # with **
    print(kwargs)
    print(type(kwargs))


mult_named_items(name='Guillem', age=34, is_developer=True)
