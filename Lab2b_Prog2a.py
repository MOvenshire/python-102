# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab2b__ Program 2a
# Date:         9/ 3/ 2020 
#
"""
#given 3d points corresponding numbers
time1=13#seconds
xpos1=1#meters
ypos1=3#meters
zpos1=7#meters

time2=84
xpos2=23
ypos2=-5
zpos2=10

time3=50
print("Time of interest =",time3,"seconds")
#use given information above to find the coordinates for time =50
#pos3=pos1+(time-time1)*((pos2-pos1)/(time2-time1))

#linear interpolation for x value dependent on time
xpos3=xpos1+(time3-time1)*((xpos2-xpos1)/(time2-time1))
print("x value =",xpos3,"m")

#linear interpolation for y value dependent on time
ypos3=ypos1+(time3-time1)*((ypos2-ypos1)/(time2-time1))
print("y value =",ypos3,"m")

#linear interpolation for z value dependent on time
zpos3=zpos1+(time3-time1)*((zpos2-zpos1)/(time2-time1))
print("z value =",zpos3,"m")
