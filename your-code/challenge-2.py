"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""


def random_string_generator(length=12, char='abcdefghijklmnopqrstuvwxyz0123456789'):
    import random
    s = [random.choice(char) for i in range(length)]
    return ''.join(s)


def batch_string_generator(n, a=8, b=12):
    import random
    import sys
    if a <= b:
        return [random_string_generator(random.choice(range(a, b))) if a < b else a for i in range(n)]
    else:
        sys.exit('Incorrect min and max string lengths. Try again.')


a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')

print(batch_string_generator(int(n), int(a), int(b)))
