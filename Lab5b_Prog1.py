# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab 5b__ Program 1 
# Date:         9/ 22/2020  
#
"""
print("This program uses the Collatz conjecture to produce a sequence of numbers.")

#ask the user for a number
numIn=int(input("Please enter a positive integer: "))

#rename the user variable so it is not overwritten in the loop 
num=numIn
#create to count the number of iterations
count=0

#create an empty string to hold the sequence of numbers
sequence=str(int(num))

while num!=1:
    #use if statements to determine which part of the collatz conjecture to use
    #even
    if num%2==0:
        num/=2
        sequence+=", "+str(int(num))
    #odd
    else:
        num=3*num+1
        sequence+=", "+str(int(num))
    count+=1

print("\nUser input:",numIn)
print("Sequence",sequence)
print("Number of iterations:", count)


