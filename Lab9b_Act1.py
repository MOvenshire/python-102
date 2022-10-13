# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab 9b__ Activity 1
# Date:         10/ 20/ 2020 
#
"""
#open Celsius.dat to read
celsius=open('Celsius.dat')
#open Fahrenheit.dat to write
fahrenheit=open('Fahrenheit.dat','w')

#loop through each line of celsius converting to fahrenheit 
#wtite the converted value and a new line to fahrenheit file
for line in celsius:
    convert=int(line)*9/5+32
    fahrenheit.write(str(convert)+"\n")

#close files 
celsius.close()
fahrenheit.close()
