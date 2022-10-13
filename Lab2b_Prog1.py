# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab2b__ Program 1 
# Date:         9/ 3/ 2020  
#
"""

#An interesting fact about me is that I have never broken a bone. 

from math import *
#C Ohm'S Law
current=5 #(ampmeres)
resistance=20 #(ohms)
#Wikipedia says current=voltage/resistance so voltage=current*resistance
print("The voltage across the conductor will be ",current*resistance,"volts.\n")

#D Kinetic Energy
#KE=.5*m*v^2 (Joules)
mass=100#kg
velocity=21#m/s
print("The kinetic energy of an object with mass 100kg and velocity 21m/s ",1/2*mass*velocity**2, " Joules.\n")

#E Reynolds Number(Re)
#Re=(flow speed*characteristic linear dimension)/kinematic viscosity
velocity=100#m/s
kVisc= 1.2# kinematic viscosity (m^2)/s
LIN_DIMENSION= 2.5#characteristic linear dimension m
print("The Reynold's Number is ",(velocity*LIN_DIMENSION)/kVisc, "\n")


#F Arps equation
#rate on day 21= initial rate/ (1+hyperbolic constant*initial decline rate* # days)^(1/constant)
rate0=100#initial rate (barrels/day)
HYPERBOLIC=0.8# hyperbolic constant 
declRate0=2#initial decline rate (barrels/day)
days=20

print("The production of a well is ",rate0/(1+HYPERBOLIC*declRate0*days)**(1/HYPERBOLIC)," barrels per day.\n")

#G Mohr-Coulomb Failure Criterion
#shear stress= normal stress*tan(angle of Ff in radians)+cohesion
#convert degree to radians
rad=35*pi/180 #angle of force of friction in radians
normStress=20 #normal stress (lbf/in^2)
cohesion= 2#lbf/in^2

print("The shear stress is ",normStress*tan(rad)+cohesion ,"lbf/in^2.\n")
