# Lab 3.1 Variables and State
# Author Linda Nikolajeva
# A program that reads in two numbers and subtracts the first one from the second one. 

# input reads in a string so we need to convert it into an int
# so we can perform mathematical operations

x = int(input('Enter the first number you clown: '))
y = int(input('Enter the second number you toole: '))

answer = x - y

print('{} minus {} is {}, you waste of oxygen!'.format(x, y, answer))

# food for thought, ideally you would want something in the code to come up if the wrong type
# of character is entered e.g. 5.6