# Arithmetic Operators
print('4 + 3 =', 4 + 3)
print('4 - 3 =', 4 - 3)
print('4 * 3 =', 4 * 3)
print('4 / 3 =', 4 / 3)
print('4 // 3 =', 4 // 3)
print('4 % 3 =', 4 % 3)
print('4 ** 3 =', 4 ** 3)

# Operator Precedence
print((6 + 3) - (6 + 3))

# Assignment Operators
print('count :', count := 1)
count += 1
print('count :', count)
count += 1
print('count :', count)  # Count is 3 now

# Comparison Operators
print('== ', count == 3)
print('!= ', count != 3)
print('> ', count > 3)
print('< ', count < 3)
print('>= ', count >= 3)
print('<= ', count <= 3)

if count >= 3:
    print('Count is at least 3!')
else:
    print('Count is not at least 3!')

# Ternary operator
print('Right On!') if count == 3 else print('Not today!')

# Logical Operators
print(True and False)       # False
print(True or False)        # True
print(not (True or False))  # False

print(1 and 2)  # 2
print(1 or 2)   # 1

print(0 and 1)  # 0
print(0 or 1)   # 1

# Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

# returns True because z is the same object as x
print(x is z)

# returns False because x is not the same object as y, even if they have the same content
print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
print(x is y)

# Membership Operators
# returns True because a sequence with the value "banana" is in the list
print("banana" in x)

# Bitwise Operators
print(3 << 2)  # OUTPUT: 12

"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""
