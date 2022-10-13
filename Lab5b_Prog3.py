# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab 5b__ Program 3 
# Date:         9/ 22/ 2020 
#
"""
print("This program takes a user input for 'x' and estimates the value of 1/(1-x) within a tolerance of 1E-6 with a Maclaurin series.")

#determine x from the user
x=float(input("Please enter a value between -1 and 1: "))

#create other numerical variables add set to 1 to start loop before redefinition
#summation set to 1 because that is the first term in the series 
add=1
summation=1

count=0

#check to see if -1<x<1 
if not(-1<x<1):
    print("ERROR: Sorry that value is not within the acceptable range.")

else:
    #estimate 1/(1-x) using a Maclaurin series within given tolerance
    while add>=1e-06:
        count+=1
        add=x**count
        summation+=add
        

    #print number of terms
    print("\nIt would take ",count,"terms to reach an estimate of", summation)
    
    #check results by computing 1/(1-x) and print calculated value
    calc=1/(1-x)
    print("The actual value of 1/(1-x) would be", calc)
    
    #calculate and print difference between estimate and directly calculated value 
    difference=summation-calc
    print("The difference between the estimated value and the actual calculated value is {:.4e}".format(difference))
