# Lab Topic 04-Flow control if elif and else
# Author Linda Nikolajeva

# Programme that reads in a student's percentage mark
# And prints out 
# The corresponding grade
# The programme should check if the percentage is valid
    # Under 40% => Fail 
    # Between 40% and 49%  => Pass 
    # Between 50% and 59%  => Merit 2 
    # Between 60% and 69%  => Merit 1 
    # Over 70%    => Distinction

percentage = float(input('Enter the percentage '))
# print (percentage)

# be careful with and's and or's
if percentage < 0 or percentage > 100:
    print ('Please enter a number between 0 and 100')
elif percentage < 40: # we know it is greater than 0
    print ('Fail')

elif percentage < 50: # between 40 and 49
    print ('Pass')

elif percentage < 60: # between 50 and 59
    print ('Merit 2')

elif percentage < 70: # between 60 and 69
    print ('Merit 1')

else: # the only option left is between 70 and 100
    print ('Distinction')

# Extra...
# In practice the percentages are rounded ie 69.5 gets rounded to 70 so is equal to a Distinction
# How would you modify the program in 1 to deal with this? Per Adnrew there are 2 ways

# This program does not actually round percentages
# to ensure that the percentage is not being unintentionally rounded when entered
# Source: ChatGPT - https://chatgpt.com/c/67c3558c-e9cc-8005-ad86-619150031081

percentage = float(input('Enter the percentage: ')) # use float to avoid unintentionally rounding

if percentage < 0 or percentage > 100:
    print('Please enter a number between 0 and 100')

elif 0 <= percentage < 40: # <=  carefully defines the exact range (or limits) for each grade
    print('Fail')
#elif percentage < 50: works, but it doesn't clearly show where each range starts and end
elif 40 <= percentage < 50:
    print('Pass')

elif 50 <= percentage < 60:
    print('Merit 1')

elif 60 <= percentage < 70:
    print('Merit 2')

else:
    print('Distinction')

# 40 <= percentage < 50 which means: The percentage must be at least 40 (including 40)
# The percentage must be less than 50 (but not 50)
# It ensures that numbers like 40.0, 50.0, 60.0 are correctly included in their respective categories


# Python only rounds numbers if you use functions like: 
# round(percentage) → Rounds to the nearest whole number.
# int(percentage) → Removes decimals (rounds down)
