# https://www.w3schools.com/python/python_ref_exceptions.asp

# Generic exception catch
try:
    print(x)  # NameError: name 'x' is not defined
except:
    print('There is an error!')


# Specific exception catch
class JustNotCoolError(Exception):
    pass


x = -1
y = 0

try:
    if not type(x) is int:
        raise TypeError("Only integers are allowed!")

    if x > 10:
        raise Exception("I'm a custom exception!")

    if x < 0:
        raise JustNotCoolError("This is not cool man!")

    print(x / y)

except NameError:
    print('NameError means something is probably undefined')
except ZeroDivisionError:
    print('You cannot divide by 0!')
except Exception as error:
    print(error)  # Prints the error
else:
    print('SUCCESS!')  # This runs if there is no error
finally:
    print('THE END')  # This runs in all cases
