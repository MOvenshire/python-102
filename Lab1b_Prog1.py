
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab #1b Program 1
# Date:         25/8/2020  
#
"""
#An interesting fact about me is that I have never broken a bone. 

#Example
"""
#calculate/print area of rectangle of length 5 in. and height 3 in
print("Area of rectangle is", 5*3,"in^2")
print()
"""
from math import *
#C Ohm'S Law
a=5 #current (ampmeres)
r=20#resistance (ohms)
#Wikipedia says a=v/r so v=a*r
print("The voltage across the conductor will be ",a*r,"volts.\n")

#D Kinetic Energy
#KE=.5*m*v^2
print("The kinetic energy of an object with mass 100kg and velocity 21m/s ",1/2*100*21**2, " Joules.\n")

#E Reynolds Number(Re)
#Re=(flow speed*characteristic linear dimension)/kinematic viscosity
print("The Reynold's Number is ",(100*2.5)/1.2, "\n")


#F Arps equation
#rate on day 21= initial rate/ (1+hyperbolic constant*initial decline rate* # days)^(1/constant)
print("The production of a well is ",100/(1+0.8*2*20)**(1/0.8)," barrels per day.\n")

#G Mohr-Coulomb Failure Criterion
#shear stress= normal stress*tan(angle of Ff(rad))+cohesion
#convert degree to radians
rad=35*pi/180
print("The shear stress is ",20*tan(rad)+2 ," lbf/in^2.\n")