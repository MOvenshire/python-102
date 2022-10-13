# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# The team members listed below have actively contributed to this assignment.
#
# Name:         Victor Malbrel
#               Marissa Ovenshire
#               Rachel Bode
#               Matthew Ensmann
# Section:      ENGR 102-220
# Team:         Team 15
# Assignment:   Lab 10b Activity 1
# Date:         10/27/2020
#

#import numpy and matplot
import numpy as np
import matplotlib.pyplot as plt

#initialize the 2d point and 2x2 matrix 
v=np.zeros((2,1))
v[0][0]=1
M=np.array(([1.00583,-0.087156],[0.087156,1.00583]))

#use a loop to plot 200 points
for i in range(200):
    #the product of M*v
    vProd=M@v
    x=vProd[0][0]
    y=vProd[1][0]
    plt.scatter(x,y,s=20)
    v=vProd

#add axis and chart titles    
plt.title("Spiral")
plt.xlabel("x axis",fontsize=10)
plt.ylabel("y axis",fontsize=10)