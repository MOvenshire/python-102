# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab 4b__ Program 3 
# Date:         9/ 17/ 2020  
#
"""
print("This program will read a number of days from the keyboard and report the total number of widgets produced from the initial testing phase to the day entered.")

#read input and convert to an integer from a string
dayIn=int(float(input("Please enter a number of days between 0 and 100: ")))
day=dayIn
#create variable for widgets
widgets=0

if 0<day>100:
    print("Sorry that is not an appropriate input")
else:
    #write progam for days 0-10
     if day<=10:
         widgets+=10*day
     #days 11 to 60     
     if 11<day<=60:
         #add 100 for first 10 days
         widgets+=100
         widgets+=40*(day-10)
     #days 60 t0 100
     if 60<day:
         #add 2100 for first 60 days
         widgets+=2100
         day-=60
         widgets+=(day*(39+(40-day))/2)
         

print("The machine will have produced",str(int(widgets)),"widgets after",dayIn,"days.")

