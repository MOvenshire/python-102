# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab 7b__ Program 2 
# Date:         10/ 6/ 2020 
#
"""
print("This program practices lists and loops while completing vector computations.")
from math import *

#get 2 vectors from user and store in a list 
A=input("Please enter vector a (components separated by space): ")
B=input("Please enter vector b (components separated by space): ")

#set strings to be lists 
a=A.split()
b=B.split()

#magnitude of vector A
aMag=0
for i in a:
    aMag+=int(i)**2
aMag=sqrt(aMag)
print ("The magnitude of vector a is",str(aMag))

#magnitude of vector B
bMag=0
for i in b:
    bMag+=int(i)**2
bMag=sqrt(bMag)
print("The magnitude of vector b is",str(bMag))

#test for errors
if len(a)!=len(b):
    print("Error: The vectors cannot be added or subtracted because they are not the same length.")
else:
    add=[]
    subtract=[]
    print("works")
    for i in range(len(a)):
    #A+B vector addition
        add.append(int(a[i])+int(b[i]))
        
    #A-B vector subtraction
        subtract.append(int(a[i])-int(b[i]))
        
    print("The addition of vector A + vector B =",str(add))
    print("The subtraction of vector A - vector B =",str(subtract))
    
    #vector dot product 
    dot=0
    for i in add:
        dot+=i
    print("The dot product of vectors A and B is",dot)
    
