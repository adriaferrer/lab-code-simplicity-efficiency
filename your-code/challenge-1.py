"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""
from word2number import w2n

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')

number_options = 'zeroonetwothreefourfiveZeroOneTwoThreeFourFiveZEROONETWOTHREEFOURFIVE'
ops_options = 'plusminus'

a = 'None'
b = 'None'
c = 'None'

while a not in number_options:
    a = str(input('Please choose your first number (zero to five): '))
while b not in ops_options:
    b = str(input('What do you want to do? plus or minus: '))
while c not in number_options:
    c = str(input('Please choose your second number (zero to five): '))

# convert words into numbers
a_num = w2n.word_to_num(a)
c_num = w2n.word_to_num(c)

if b == 'plus':
    result = a_num + c_num
elif b == 'minus':
    result = a_num - c_num
else:
    result = 'Error: invalid input'

print(f'Result: {result}\nThanks for using this calculator, goodbye :)')
