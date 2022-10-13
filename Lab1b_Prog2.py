
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab1b Program 2 
# Date:         25/8/2020  
#
"""
from math import *

#Problem 1 
print("\nThis shows the evaluation of sin(x)/x")
print("The x values input will inclde 1,0.1,0.01,0.001,...,0.00000001")
print ("My guess is the function approaches 1.")

print(sin(pow(10,(0)))/pow(10,(0)))
print(sin(pow(10,(-1)))/pow(10,(-1)))
print(sin(pow(10,(-2)))/pow(10,(-2)))
print(sin(pow(10,(-3)))/pow(10,(-3)))
print(sin(pow(10,(-4)))/pow(10,(-4)))
print(sin(pow(10,(-5)))/pow(10,(-5)))
print(sin(pow(10,(-6)))/pow(10,(-6)))
print(sin(pow(10,(-7)))/pow(10,(-7)))

print()

#Problem 2 
print("This shows the evaluation of (1-cos(x)/x^2)")
print("The x values input will inclde 1,0.1,0.01,0.001,...,0.00000001")
print ("My guess is the function approaches 1/2.")

print((1-cos(pow(10,(0))))/pow(10,(0))**2)
print((1-cos(pow(10,(-1))))/pow(10,(-1))**2)
print((1-cos(pow(10,(-2))))/pow(10,(-2))**2)
print((1-cos(pow(10,(-3))))/pow(10,(-3))**2)
print((1-cos(pow(10,(-4))))/pow(10,(-4))**2)
print((1-cos(pow(10,(-5))))/pow(10,(-5))**2)
print((1-cos(pow(10,(-6))))/pow(10,(-6))**2)
print((1-cos(pow(10,(-7))))/pow(10,(-7))**2)

print()


#Problem 3 
print("This shows the evaluation of ((1+1/x)**x")
print("The x values input will inclde 1,10,100,1000,...,10000000")
print ("My guess is the function approaches 1000000.")

print((1+1/pow(10,(0)))**pow(10,(0)))
print((1+1/pow(10,(1)))**pow(10,(1)))
print((1+1/pow(10,(2)))**pow(10,(2)))
print((1+1/pow(10,(3)))**pow(10,(3)))
print((1+1/pow(10,(4)))**pow(10,(4)))
print((1+1/pow(10,(5)))**pow(10,(5)))
print((1+1/pow(10,(6)))**pow(10,(6)))
print((1+1/pow(10,(7)))**pow(10,(7)))


# I remembered L'Hopitals for others 
# However, I couldn't think of this so my guess was very off
