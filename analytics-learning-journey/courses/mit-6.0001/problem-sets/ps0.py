# -*- coding: utf-8 -*-
"""
MIT 6.0001: Problem Set 0

Problem: Write a program that does the following in order:
1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”.
4. Prints out the log (base 2) of “x”.
"""

# import math library to use log
import math

#Greet the user
print("Today we'll be calculating the power of 2 numbers of your choosen, and also,")
print("calculating the log(base2) of the first number you choose. Let's begin!")


# Ask the user to enter a number X --> input
x = float(input("Please enter your first number: "))

# Ask the user to enter a number Y --> input
y = float(input("Please enter your second number: "))

# Print out number X riased to the power Y --> expression, statement
print(x, " to the power of ", y, " equals ", x**y)

# Print out the log (base 2) of X --> expression, statement
print("The log(base2) of ", x, " is equal to: ", math.log(x,2))