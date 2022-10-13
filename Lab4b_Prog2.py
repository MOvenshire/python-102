# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab 4b__ Program 2 
# Date:         9/ 16/ 2020 
#
"""
print("This program will calculate the Reynolds number for pipe flow and report whether the flow is laminar, in transition, or turbulent. ")
 
#create variables and assign with user input

#characteristic velocity of the flow meters/second
velocity=float(input("Please enter the characteristic velocity of the flow in m/s: "))

#pipe diameter meters
diameter= float(input("Please enter the diameter in meters: "))

#fluid kinematic viscosity meters squared/ second
visc=float(input("Please enter the fluid kinematic viscosity in m^2/s: "))

#calulate reynolds number
reynolds=(velocity*diameter)/visc
print("\nThe Reynolds number is {:.2f}".format(reynolds))
print("Therefore the fluid flow is",end=" ")

#figure out if flow is laminar, in transition or turbulent
if reynolds < 2300:
    print("laminar.")
elif reynolds > 2900:
    print("turbulent.")
else:
    print("in transition.")