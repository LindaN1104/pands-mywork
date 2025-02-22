# Lab 3.1 Variables and State
# Author Linda Nikolajeva

#  program that reads in two numbers 
# and divides the first one by the second 
# and give the integer result 
# and the remainder

x = int(input('Enter the first number you clown: '))
y = int(input('Enter the number you want to divide by you toole: '))

answer = int(x//y)
#// gives the integer division

remainder = x%y
# % gives the remainder

print('{} divided by {}, is {}, with remainder of {}, you waste of oxygen!'.format(x, y, answer, remainder))