# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab 4b__ Program 4 
# Date:         9/ 17/ 2020  
#
"""
print("This program solves a quadratic equation when the user inputs coefficients.")

from math import *

#get coefficients
a=int(input("Please enter the coefficient for the x^2 part as a whole number: "))
b=int(input("Please enter the coefficient for the x part as a whole number: "))
c=int(input("Please enter the coefficient for the constant part as a whole number: "))
print()
#find the discriminant
d=b**2-(4*a*c)

#special cases where coefficients are equal to 0 
if a==0 and b!=0:
    print("This is a linear equation.")
    solution= -c/b
    print("The solution would be", str(solution))
elif a==b==0:
    print("No equation to solve.")    


#check if result is imaginary
elif d<0:
    
    x1=str(-b/(2*a))+"+{:.2f}i".format((sqrt(abs(d)))/(2*a))
    x2=str(-b/(2*a))+"-{:.2f}i".format((sqrt(abs(d)))/(2*a))
    print("There are two complex roots: ")
    print("x1 =",x1)
    print("x2 =",x2)
#check if result is real values
else:
    quadPos=(-b+sqrt(d))/(2*a)
    quadNeg=(-b-sqrt(d))/(2*a)
    x1="{:.2f}".format(quadNeg)
    x2="{:.2f}".format(quadPos)
    print("There are two complex roots: ")
    print("x1 =",x1)
    print("x2 =",x2)    