# Lab 3.2 Fun with Numbers
# Author Linda Nikolajeva

# Programme that takes in a float and outputs an int rounded down
# Steps involved
# 1. import math module (it is built in)
# 2. Get user input
# 3. Round down
# 4. Output the result
# ChatGPT Reference https://chatgpt.com/c/67baf6c3-39b0-8005-a0eb-6f35c295ba82

import math

# Get user input
numberTofloor = float(input("Enter a float number: "))

# to round down
flooredNumber = math.floor(numberTofloor)

print('{} rounded down {}'.format(numberTofloor, flooredNumber))