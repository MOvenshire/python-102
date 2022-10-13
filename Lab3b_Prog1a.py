# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab 3b__ Program 1 a  
# Date:         9/10/2020  
#
"""
print("This program calculates voltage with Ohm's Law.")
from math import *
# Ohm'S Law ask the user for values as floats to ensure most accurate calculations
current=float(input("Please enter the current (ampmeres)): "))
resistance=float(input("Please enter the resistance (ohms): "))

#Wikipedia says current=voltage/resistance so voltage=current*resistance
voltage=current*resistance
print("Voltage across the conductor =",voltage,"volts.")

