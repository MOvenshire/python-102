# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab2b__ Program 3  
# Date:         9/ 2/ 2020 
#
"""
#z=1
z=0
x=1
z+=x
print(z)

#z=3
x+=1
z+=x
print(z)

#z=11
#reset values to add 10+1
y=10
x=1
z=0
z+=y
z+=x
print(z)

#z=28
z+=y
x+=1
x+=1
x+=1
x+=1
x+=1
x+=1
z+=x
print(z)

#z=123
#start with x=10 y=10 to multiply together and get 100
x=y
y*=x
z=0
z+=y
#add 20
z+=x
z+=x
#reset x and add 3
x=1
z+=x
z+=x
z+=x
print(z)

#z=10^32
x=y
y*=x
x=y
y*=x
x=y
y*=x
x=y
y*=x
z=0
z+=y
print(z)

#z=4321
#reset values then add 1 to z 
z=0
x=1
y=10
z+=1
#add 20 
z+=y
z+=y
x=y
#add 300 in increments of 100
y*=x
z+=y
z+=y
z+=y
#add 4000 in increments of 1000
y*=x
z+=y
z+=y
z+=y
z+=y
print(z)