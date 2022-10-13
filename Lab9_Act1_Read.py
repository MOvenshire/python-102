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
# Assignment:   Lab 9 Activity 1 Read
# Date:         10/20/2020
#


#open ThermoData.txt to read
txtFile=open('ThermoData_P_5_10_MPa.txt')

#open ThermoData.csv to write
csvFile=open('ThermoData_P_5_10_MPa.csv','w')

#convert text file spaces to commas for csv
#loop through each line of the text file 
for line in txtFile:
    splitLine=line.split(" ")
    output=""
    for i in splitLine:
        if i!="":
            output+=i+","
    csvFile.write(output[:len(output)-1])
csvFile.close()
txtFile.close()

