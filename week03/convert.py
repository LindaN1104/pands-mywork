# Lab 3.2 Fun with Numbers
# Author Linda Nikolajeva

# Programme that that takes in a float amount of dollars and returns that absolute amount in cent

# Steps incolved
# 1 Takes a float input representing dollars and cents (e.g., -9.44 or 9.44).
# 2 Converts it to cents by multiplying by 100.
# 3 Returns the absolute value as an integer.
# ChatGPT used/ adapted from ...https://chatgpt.com/c/67baf940-d518-8005-a2a8-461d33eb4814
# food for thought, what happens if another type amount/ character is entered?

import math

floatnum = float(input("Enter a money amount: "))

cents = abs(round(floatnum * 100))
# # Convert to cents and take absolute value return cents

print('{} in cents is {}'.format(floatnum, cents))