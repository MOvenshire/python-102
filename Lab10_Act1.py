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
# Assignment:   Lab 10 Activity 1
# Date:         10/27/2020
#

import numpy as np
import matplotlib


print("As a team, we have gone through all required sections of the tutorial, and each team member understands the material.")

#create 4 matricies 
#A is 3 x 4
A=np.arange(12).reshape(3,4)
print(A)
#B is 4 x 2 
B=np.arange(8).reshape(4,2)
print(B)
#C is 2 x 3 
C=np.arange(6).reshape(2,3)
print(C)
#D is 3 x 1
D=np.arange(3).reshape(1,3)
print(D)
#E=ABC matrix multiplication
E=A @ B @ C
print(E)

#E=B@A@C
#What happens when computing E+BAC?
print("Multiplying the matricies B*A*C will not work because B does not have enough rows. ")

#Solve system of linear algebraic equations
u = [[50,75,10],[5,10,3],[90,100,50]]
p = [[500],[75],[1150]]
print(np.linalg.solve(u,p))


#Solve another system of linear algebraic equations
b = [[1,-2,-4],[2,-3,-6],[-3,6,15]]
v = [[7],[5],[0]]
print(np.linalg.solve(b,v))