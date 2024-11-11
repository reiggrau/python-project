import os

# r = Read
# a = Append
# w = Write
# c = Create

# Read - error if it does not exist

file = open('names.txt', 'r')  # 'rt' for text files, 'rb' for binary

# print(file.read())

# print(file.read(3))  # First 3 letters

# print(file.readline())  # First line
# print(file.readline())  # Second line

for line in file:
    print(line)

file.close()  # Remember to close the file once done

# Error handling
try:
    file = open('names.txt')
    print(file.read())
except:
    print("File not found!")
finally:
    file.close()

# Append - creates the file if it does not exist
file = open('extra_names.txt', 'a')  # append
file.write("\nKraden")
file.close()

file = open('names.txt')  # append
print(file.read())
file.close()

# Write (overwrite)
file = open('extra_names.txt', 'w')
file.write("I overwrote the file.")
file.close()

file = open('extra_names.txt')  # append
print(file.read())
file.close()

# Create
# Method 1 - Opens file, creates one if it does not exist
file = open('new_file.txt', 'w')
file.close()

# Method 2 - Creates file but returns an error if it exists
if not os.path.exists('new_file'):
    f = open('new_file', 'x')
    f.close()

# Delete
# avoid error if it doesn't exist
if os.path.exists('new_file.txt'):
    os.remove('new_file.txt')
else:
    print("File not found!")

# 'with' keyword (copy content of 'names.txt' to 'extra_names.txt')
with open('names.txt') as f:
    content = f.read()

with open('extra_names.txt', 'w') as f:
    f.write(content)
