# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab 5b__ Program 2 
# Date:         9/ 22/ 2020 
#
"""
print("This progam will take user input measurements and print some statistical data.")
#create a variable to keep track of the number of inputs
count=0

#ask for the first measurement
measurement= float(input("Please enter a measurement:"))

#use the first value to create minimum and maximum variables
minimum=measurement
maximum=measurement

#create the sum variabl=0 so I can add measurements to it inside the loop 
totalSum=0

#create a loop that will continue asking for measurements until a negative value is entered
while measurement>0:
    #increase the count and sum variables
    count+=1
    totalSum+=measurement
    #test to redefine minimum and maximum if the measurement is less than 
    #or greater than the last min/max respectively 
    if measurement<minimum:
        minimum=measurement
        
    if measurement>maximum:
        maximum=measurement
    #prompt the user again to restart the loop 
    measurement=float(input("Please enter a measurement:"))
    
    
#print output and floats to 3 decimal places 
print()
print("Number of measurements:{:>5s}".format(str(count)))
print("Average:{:19s}{:.3f}".format(" ",totalSum/count))
print("Maximum:{:19s}{:.3f}".format(" ",maximum))
print("Minimum:{:19s}{:.3f}".format(" ",minimum))