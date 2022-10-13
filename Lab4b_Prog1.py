# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab 4b__ Program 1 
# Date:         9/ 16/ 2020  
#
"""
print("This program will take 3 user input numbers and report the largest value with conditionals.")

#create variables, get user input, and convert to a number 
num1= float(input("Please enter a number: "))
num2= float(input("Please enter a number: "))
num3= float(input("Please enter a number: "))

maxNum=0
#find the largest number
if num1>num2:
    maxNum=num1
else:
    maxNum=num2
if maxNum<num3:
    maxNum=num3

print("The maximum input value is", maxNum)

