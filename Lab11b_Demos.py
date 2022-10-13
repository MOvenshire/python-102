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
# Assignment:   Lab 11b Demonstration
# Date:         11/03/2020
#

import Lab11b_Functions as lab


#4 test cases for function a and remaining volume 
#length: 10 width: 20 height: 5 radius: 4
    #volume left: 748.67

#length: 10 width: 20 height: 5 radius: 15
    #volume left: 0

#length: 10 width: 20 height: 5 radius: 7
    #volume left: 365.15

#length: 16 width: 20 height: 5 radius: 8
    #volume left: 594.69
         

#demo a 
print(lab.function_a1(10,20,3,4))
print(lab.function_a2(10,20,5,4))
print(lab.function_a2(10,20,5,15))
print(lab.function_a2(10,20,5,7))
print(lab.function_a2(16,20,5,8))


#demo b
print()
n=["fact1","fact2","fact3"]
pc=[300,200,400]
ac=[40,100,100]
print("The least profitable factory is",lab.function_b(n,ac,pc))

#demo c
print() 
lab.function_c("Ms. Reveille IX","College Station","TX","12345","123 Kyle Street")
#with second line for street adress
lab.function_c("Ms. Reveille IX","College Station","TX","12345","123 Kyle Street","Apartment 1")

#demo d
print()
#note function d does not return or print anything
fileName=input("Please enter the .csv you want to open: ")
lab.function_d(fileName)

#demo e
print()
testList=[23,4,5,6,2,-10]
minNum,maxNum,avg=lab.function_e(testList)
print("The minimum value is",minNum)
print("The maximum value is",maxNum)
print("The mean value is",avg)

#demo f
print()
timeList = [0, 2,  4,  6,  8,  10]
distList = [0, 10, 16, 29, 40, 52]
velList = lab.function_f(timeList, distList)

print("The velocities are",velList)
