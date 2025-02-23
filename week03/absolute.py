# Lab 3.2 Fun with Numbers
# Author Linda Nikolajeva
# Programme that that takes in number and give its absolute value (ie -4 or 4 would both output 4)
# The abs() function returns the absolute value of the specified number
# https://www.w3schools.com/python/ref_func_abs.asp
# The Python abs() function return the absolute value. 
# The absolute value of any number is always positive, it removes the negative sign of a number in Python. 
# Example: Input: -29. Output: 29
# https://www.google.ie/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwim86vyxNmLAxVjZ0EAHRLyE1sQFnoECBYQAw&url=https%3A%2F%2Fwww.geeksforgeeks.org%2Fabs-in-python%2F%23%3A~%3Atext%3DThe%2520Python%2520abs()%2520function%2COutput%253A%252029&usg=AOvVaw2REyd-ZJwta8DEyNvUNzwZ&opi=89978449

# In the question, number is ambiguous but the
# output implies that we should be dealing with floats
# So I am casting the input to a float ... example of the type of comments Andrew wants

#... for my own reference... float variable = is a function or reusable code in the Python programming language 
# that converts values into floating point numbers
# Floating point numbers are decimal values or fractional numbers like 133.5

number = float(input("Enter a number:"))
absoluteValue = abs(number)
print('The absolute value of {} is {}'.format(number, absoluteValue))