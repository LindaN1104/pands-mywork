# Lab 4.2 loops 
# Author Linda Nikolajeva

# Programme that keeps reading numbers
# Until the user enters a 
# append each number entered into a list
# then print out each of the numbers entered
# and the average of them

numbers = [] # This line initializes an empty list called numbers.
# This list will be used to store the numbers entered by the user.

num = int(input('Enter number (0 to quit): '))
# This line asks the user to input a number and converts the input to an integer using int()
# The input() function waits for the user to type a number and hit Enter.
# The prompt tells the user they can enter 0 to quit.

while num != 0:
    # This is the start of a while loop
    #  The loop will continue running as long as the value of num is not 0
    # When the user enters 0, the loop will stop
    numbers.append(num)
    # Inside the loop, this line adds the value of num to the numbers list using the append() method

    num = int(input('Enter another (0 to quit): '))

for value in numbers:
    print (value)

average = float(sum(numbers)) / len(numbers)
print (f'The average is {average}')



# help used to understand each line of code
# https://chatgpt.com/c/67c373fa-65b8-8005-8e7b-17e723535a70