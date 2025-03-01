# Lab Topic 04-Flow control if elif and else
# Author Linda Nikolajeva

# Programme that asks the user to input a number
# And tell the user if number is even or odd

number = int(input('Enter an integer: '))

if (number % 2) == 0:
    print (f'{number} number is an even number')

else:
    print (f'{number} is an odd number')