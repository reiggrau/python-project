# python-project

This project follows the tutorial from Dave Gray
Source: https://youtu.be/H2EJuAcrZYU?si=ShG6FtnMOQ6el6Bb

# Lesson 1 - First steps

## Setup

In order to start your first python project, follow the following steps:

1. Install python from https://python.org

2. Install a code editor (I chose VS Code)

3. Open VS Code, and install 'python' from the 'extensions' menu

4. In VS Code, press 'Ctrl+Shift+P' and search 'Python: Select Interpreter' and select 'Python 3.XX...' (whatever the version is installed)

5. Open a new terminal. If you are in windows, type 'py -3 --version'. In Mac or Lunux type 'python3 --version' instead. Python version should appear in the terminal.

## REPL (Read-Evaluate-Print-Loop)

Developers use REPL Python to communicate with the Python Interpreter. In contrast to running a Python file, you can input commands in the REPL and see the results displayed immediately.

To try it, type 'py' in the terminal to start REPL. Some text followed by '>>>' should appear.

To try it out, type '2+2', and a '4' should appear as a response. You can also type 'greeting = "Hello World!"' and then type 'print(greeting)', and a 'Hello World!' should appear as a response.

You can close REPL by typing 'quit()'.

## Create a .py file and run it

Create a new file and name it hello.py (make sure to save as a python .py file type). Then add the following lines:

```python
greeting = 'Hello World!'
print(greeting)
```

We'll see three ways of running the code:

1. In the temrinal, navigate to the location of 'hello.py' and type 'py hello.py'. The 'Hello World!' should appear in the same terminal.
2. (in VS Code) Press the 'play' symbol in the top-right corner.
3. (in VS Code) Right-click the 'hello.py' file in the explorer menu and select 'Run Python File In Terminal'.

# Lesson 2 -

## Naming variables

Variable names can be made up with letters and numbers, like 'name0001', or undescore characters, like '\_name'. We cannot start a variable name with numbers though, like '0001name'.

## Expressions vs Statements

Expressions are a combination of programming logic that evaluates to a result. Adding two numbers together is an expression because it results in the sum of the two numbers.

```python
2 + 2 # OUTPUT: 4
```

Statements are a more general term for all sorts of pieces that make up your code. In programming, statements are the building blocks that constitute a program.

An example of a statement is the variable assignment:

```python
x = 2
```

In any complex program that you'll write, you'll use both expressions and statements together. A basic example of a statement that comes in combination with an expression is:

```python
x = 2 + 3
```

One example of where the distinction between statements and expressions is important is when passing arguments to functions. You can pass an expression as an argument to a function, but you can't pass a statement as an argument.

As a rule of thumb, you can remember that expressions evaluate to a result and statements don't.

## print()

The print() function prints the specified message to the screen, or other standard output device.

The message can be a string, or any other object, the object will be converted into a string before written to the screen.

```python
greeting = 'Hello World!'
print(greeting) # OUTPUT: 'Hello World!'
```

## Comments

Single-line comments begin with the “#” character. Anything that is written in a single line after ‘#’ is considered as a comment and thus ignored when the code runs.

There are two ways of using single-line comments in Python. You can use it before the code or next to the code.

## Multi-line comments

Python does not support multi-line comments. However, there are multiple ways to overcome this issue.

The first way is by using # at the beginning of each line of the comment.

```python
# This is a
# multi-line
# comment
```

The next way is by using string literals but not assigning them to any variables. If you do not assign a string literal to a variable, the Python interpreter ignores it.

You can either use a single (‘’) quotation or double (“”) quotation.

```python
"""
This is a
multi-line
comment
"""
```

## Indentations

Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code, and will give you an error if you skip the indentation, os use it where it is not meant to be used:

```python
if 5 > 2:
  print("Five is greater than two!") # Correct way of using indentation
```

```python
name = 'Guillem'
    surname = 'Reig' # 'Unexpected indentation' error warning
```

The number of spaces is up to you as a programmer, but it has to be at least one.

## Formatter

You can avoid the previous error by enabling a formatting provider for python. The one I use is 'autopep8', downloadable from the extensions menu.

# Lesson 3 - Operators

Operators are used to perform operations on variables and values.

```python
sum = 10 + 5
print(sum) # OUTPUT: 15
```

## Arithmetic Operators

Arithmetic operators are used with numeric values to perform common mathematical operations:

```
+	  Addition	        x + y
-	  Subtraction	      x - y
*	  Multiplication	  x * y
/	  Division	        x / y     # 4 / 3 => 1.333 (decimal, use 'round(x) to convert to integer)
%	  Modulus	          x % y     # 4 % 3 => 1
**	Exponentiation	  x ** y    # 4 ** 3 => 64
//	Floor division	  x // y    # 4 // 3 => 1
```

The addition operator can be used to concatenate strings:

```python
'Guillem ' + 'Reig' # OUTPUT: 'Guillem Reig'
```

### Operator Precedence

Operator precedence describes the order in which operations are performed.

Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

```python
print((6 + 3) - (6 + 3)) # OUTPUT: 0
```

Multiplication \* has higher precedence than addition +, and therefor multiplications are evaluated before additions:

```python
print(100 + 5 * 3) # OUTPUT: 115
```

The precedence order is described in the table below, starting with the highest precedence at the top:

```
()	          Parentheses
**	          Exponentiation
+x  -x  ~x	  Unary plus, unary minus, and bitwise NOT
*  /  //  %	  Multiplication, division, floor division, and modulus
+  -	        Addition and subtraction
<<  >>	      Bitwise left and right shifts
&	            Bitwise AND
^	            Bitwise XOR
|	            Bitwise OR
==  !=  >  >=  <  <=  is  is not  in  not in 	    Comparisons, identity, and membership operators
not	          Logical NOT
and	          AND
or	          OR
```

If two operators have the same precedence, the expression is evaluated from left to right. Beware though, as different order might give a different result.

```python
print(4 / 3 * 9 // 3 % 2) # OUTPUT: 0.0
print(4 // 3 * 9 / 3 % 2) # OUTPUT: 1.0
print(4 % 3 * 9 // 3 / 2) # OUTPUT: 1.5

```

## Assignment Operators

Assignment operators are used to assign values to variables:

```
=	      x = y	      x = y
+=	    x += y	    x = x + y
-=	    x -= y	    x = x - y
*=	    x *= y	    x = x * y
/=	    x /= y	    x = x / y
%=	    x %= y	    x = x % y
//=	    x //= y	    x = x // y
**=	    x **= y	    x = x ** y
```

## Comparison Operators

Comparison operators are used to compare two values. They return either 'true' or 'false':

```
==	  Equal	                    x == y
!=	  Not equal	                x != y
>	    Greater than	            x > y
<	    Less than	                x < y
>=	  Greater than or equal to	x >= y
<=	  Less than or equal to	    x <= y
```

## Logical Operators

Logical operators are used to combine conditional statements:

```
and 	  Returns True if both statements are true	                  x < 5 and  x < 10
or	    Returns True if one of the statements is true	              x < 5 or x < 4
not	    Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)
```

## Identity Operators

Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

```
is 	      Returns True if both variables are the same object	      x is y
is not	  Returns True if both variables are not the same object	  x is not y
```

## Membership Operators

Membership operators are used to test if a sequence is presented in an object:

```
in 	      Returns True if a sequence with the specified value is present in the object	      x in y
not in	  Returns True if a sequence with the specified value is not present in the object	  x not in y
```

## Bitwise Operators

Bitwise operators are used to compare (binary) numbers:

```
& 	  AND	                        Sets each bit to 1 if both bits are 1	            x & y
|	    OR	                        Sets each bit to 1 if one of two bits is 1	      x | y
^	    XOR	                        Sets each bit to 1 if only one of two bits is 1	  x ^ y
~	    NOT	                        Inverts all the bits	                            ~x
<<	  Zero fill left shift	      Shift left by pushing zeros in from the right and let the leftmost bits fall off	    x << 2
>>	  Signed right shift	        Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	    x >> 2
```
