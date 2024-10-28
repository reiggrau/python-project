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
