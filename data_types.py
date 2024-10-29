# String data type

# Literal assignment
import math
first = "Guillem"
last = "Reig"

print(type(first))  # OUTPUT: <class 'str'>
print(type(first) == str)  # OUTPUT: True
print(isinstance(first, str))  # OUTPUT: True

# Constructor Function
pizza = str("Pepperoni")

print(type(pizza))  # OUTPUT: <class 'str'>
print(type(pizza) == str)  # OUTPUT: True
print(isinstance(pizza, str))  # OUTPUT: True

# Concatenation
fullname = first + " " + last
fullname += " Grau"
print(fullname)

# Casting a number to a string
year = str(1989)
print(year)
print(type(year))

statement = "I was born in " + year + "."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you?

I was just checking in.
                    All good?

'''

print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods
print(first.lower())
print(first.upper())
print(first)  # Does not mutate the string

print(multiline.title())  # Capitalizes the first letter of each word
print(multiline.replace("good", "ok"))  # Replaces a word for another

print(len(multiline))
multiline += "                               "
multiline = "                       " + multiline
print(len(multiline))

print(len(multiline.strip()))   # Removes whitespaces
print(len(multiline.lstrip()))  # Removes left whitespaces
print(len(multiline.rstrip()))  # Removes right whitespaces

# Build a Menu
title = "menu".upper()
# Adds '=' to each side until a length of 20
print(title.center(20, "="))  # OUTPUT: ========MENU========
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheescake".ljust(16, ".") + "$4".rjust(4))

# String index values
print(first[1])     # u
print(first[-1])    # m (last letter)
print(first[1:])    # uillem
print(first[1:-1])  # uille (last not included)

# Some methods return boolean data
print(first.startswith("G"))    # Case sensitive!
print(first.endswith("m"))

# Boolean data type
myvalue = True
x = bool(False)

print(type(myvalue))
print(type(x))

# Numeric data types
# Integer
price = 100
best_price = int(80)
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers
print(abs(gpa))         # 3.28
print(round(gpa))       # 3
print(round(gpa, 1))    # 3.3

# Math
print(math.pi)          # 3.141592653589793
print(math.sqrt(64))    # 8
print(math.ceil(gpa))   # 4
print(math.floor(gpa))  # 3

# Casting a string to a number
print(zipcode := "08000")
print(zip_value := int(zipcode))
print(type(zip_value))

# Error if you try to cast incorrect data
print(int(first))
