# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab 3b__ Program 1 d  
# Date:         9/10/2020  
#
"""
print("This program calculates the production of a well after a given number of days for a given initial production rate, initial decline rate, and hyperbolic constant.")
#Arps equation
#rate on day 21= initial rate/ (1+hyperbolic constant*initial decline rate* # days)^(1/constant)
rate0=float(input("Please enter the initial production rate (barrels/day): "))
declRate0=float(input("Please enter the initial decline rate (barrels/day): "))
days=int(float(input("Please enter the number of days: ")))
HYPERBOLIC=float(input("Please enter the hyperbolic constant: ")) 

production=rate0/(1+HYPERBOLIC*declRate0*days)**(1/HYPERBOLIC)
print("Production of a well =",production,"barrels per day.")

