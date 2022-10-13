# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab 3b__ Program 2 
# Date:         9/ 12/ 2020  
#
"""
print("This program takes 3D location point inputs and prints the angle between the vectors.")
from math import *
#create and assign vaaribales based on user input

#3d position of an observer (xObs,yObs, zObs)
print("Observer Location ")
xObs=int(input("Please enter the x position of the Observer: "))
yObs=int(input("Please enter the y position of the Observer: "))
zObs=int(input("Please enter the z position of the Observer: "))

#3d position of the first observed point (x1,y1,z1)
print("\nPoint 1 Location")
x1=int(input("Please enter the x position of the first point: "))
y1=int(input("Please enter the y position of the first point: "))
z1=int(input("Please enter the z position of the first point: "))

#3d position of the second observed point (x2,y2,z2)
print("\nPoint 2 Location")
x2=int(input("Please enter the x position of the second point: "))
y2=int(input("Please enter the y position of the second point: "))
z2=int(input("Please enter the z position of the second point: "))

#create and assign vectors from the observer 
#Observer to point 1
xVector1=x1-xObs
yVector1=y1-yObs
zVector1=z1-zObs

#Observer to point 2
xVector2=x2-xObs
yVector2=y2-yObs
zVector2=z2-zObs

#use arccos to calculate the angle between 2 vectors 
#magnitude of vector 1
v1magnitude=sqrt(xVector1**2+yVector1**2+zVector1**2)

#magnitude of vector 2
v2magnitude=sqrt(xVector2**2+yVector2**2+zVector2**2)

#dot product
dot=xVector1*xVector2+yVector1*yVector2+zVector1*zVector2

#put it together to find angle
angleRad=acos(dot/(v1magnitude*v2magnitude))
angleDegree=angleRad*180/pi

print("Observer location is x=",xObs,"y=",yObs,"z=",zObs)
print(" Point 1 location is x=",x1,"y=",y1,"z=",z1)
print(" Point 2 location is x=",x2,"y=",y2,"z=",z2)
print("\nThe angle between the points is","{:.3f}".format(angleDegree),"degrees.")