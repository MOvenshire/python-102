# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab 9b __ Activity 2
# Date:         10/ 20/ 2020  
#
"""
#ask the user for a file name for saving the data
name=input("Please enter a file name to save data: ")

#ask the user for the amount of the loan (P)
P=float(input("Please enter the amount of the loan: $"))
#ask the user for number of months (N) for repaying
N=float(input("Please enter the number of months over which the loan will be repaid: "))
#ask the user for annual interest rate (i)
i=float(input("Please enter the annual interest rate as a decimal ex.25% to 0.025: "))

#calculate monthly payment 
J=i/12
M=P*(J/(1-(1+J)**-N))

#open a csv file to write
fileName=name+".csv"
f=open(name+".csv",'w')

#create other variables for print
begin=P #beginning balance $
final=P #final balance $
accruedInterest=0

basic="{},${:.2f},${:.2f},${:.2f},${:.2f}\n"

#add header
f.write("Month,Beginning Balance,Monthly Interest,Accrued Interest,Final Balance\n")

#add the first line 
f.write("0,,,,$100000.00\n")

#create a loop to keep track of the months
for num in range(1,int(N)+1):
    #start new line 
    begin=final
    #find the monthly interest
    monthly=begin*J
    #add the monthly payment to the accrued interest
    accruedInterest+=monthly
    #subtract the monthly payment and add the monthly interest to find the final value
    final=final-M+monthly
    
    #add the variables to the csv file with the format created above
    f.write(basic.format(num,begin,monthly,accruedInterest,final))

#close the file
f.close()