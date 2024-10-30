# Global scope
name = 'Global'


def greeting():
    print(name)  # 'Global'


greeting()


def another():
    name = 'Local'
    print(name)  # 'Local'


another()
print(name)  # name remains 'Global'

# Changing global variables from inside a function
num = 1


def numfun():
    global num
    num = 2

    num2 = 3

    def extra():
        nonlocal num2
        print(num2)

    extra()


numfun()

print(num)  # 2
