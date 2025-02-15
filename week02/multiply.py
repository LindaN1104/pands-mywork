# Programme that outputs what 111*555 is
# Exercise per Lab 2.2
# Topic 2 as part of 24-25: 4122--Programming and Scripting
# Author Linda Nikolajeva

111 * 555
num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))

mul = num1 * num2

print("Multiplication of {} and {} is {}".format(num1,num2,mul))

#slightly adapted code from https://youtu.be/y2TnP6JsIKk
# line 7 tells it what num1 is and what to say
# line 8 does the same but for the second number
# line 10 tells the computer mul is line 7 multiplied by line 8
# line 12 tells the computer how to say the answer
