# Lab 3.2 Fun with Numbers
# Author Linda Nikolajeva
# prpgramme that taksetakes in a float and outputs an int (rounded up or down)
# Per A.Beaty be careful of round, it rounds to the nearest even number
# eg 4.5 rounds to 4
# but 5.5 rounds to 6
# so do not use it accuracy is essential

numberToRound = float(input("Enter a float number: "))
roundedNumber = round(numberToRound)
print ( '{} rounded is {}'.format(numberToRound,roundedNumber))