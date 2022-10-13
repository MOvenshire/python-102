# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab 3b__ Program 1 c
# Date:         9/10/2020  
#
"""
from math import *
print("This program calculates the shear stress for a given normal stress that is applied to a material with a given cohesion and angle of internal friction.")
# Mohr-Coulomb Failure Criterion
#shear stress= normal stress*tan(angle of Ff in radians)+cohesion
angle= float(input("Please enter the angle of internal Friction (degrees): "))
#convert degree to radians
rad=angle*pi/180
normStress=float(input("Please enter the amount of normal stress (lbf/in^2): ")) 
cohesion= float(input("Plese enter the cohesion of the material (lbf/in^2)"))

shear=normStress*tan(rad)+cohesion
print("Shear stress =",shear,"lbf/in^2")

