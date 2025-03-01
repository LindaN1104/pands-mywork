# Lab 4.2 loops 
# Author Linda Nikolajeva

# Programme that prompts the user to guess a number
# Keep prompting the user to guess the number
# until the user gets the right on
# Programme was then modified to generate a random number

import random

numToGuess = random.randint(0, 100)  # Generate a random number between 0 and 100

guess = int(input('Please guess the number: ')) # prompts the user to enter a number
# int(...) converts the user’s input (which is a string) into an integer
# The guessed number is stored in the variable guess

while guess != numToGuess: # starts a while loop, which keeps running
    #as long as the guessed number (guess) is not equal to (!=) numToGuess (which is 30)
    if guess < numToGuess: # promt to say guessed number is too low
        print('Too Low! ')
    else: # I know it cant be equal or too low, so it must be too high
        print('Too High! ')
    guess = int(input('Guess Again! '))

print('Well done! Yes the number was ', numToGuess)


# source to generate the random num
# https://chatgpt.com/c/67c36d0b-dac4-8005-a16e-dbb1d6af2045