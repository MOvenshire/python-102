# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab 3b__ Program 1 b 
# Date:         9/10/2020  
#
"""
# Kinetic Energy
print("This program calculates energy given mass and velocity.")

#KE=.5*m*v^2 (Joules) values as floats to ensure most accurate calculations
mass=float(input("Please enter the mass (kg): "))
velocity=float(input("Please enter the velocity (m/s): "))
KE=1/2*mass*velocity**2

print("Kinetic Energy =",KE,"Joules")

