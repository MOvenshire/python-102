# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab 7b__ Program 3 
# Date:         10/ 6/ 2020 
#
"""
import statistics
print("This program determines the median by sorting a list.")
gradeData=[79,99,73,49,67,62,52,99,57,58,	
           67,88,71,69,41,74,53,90,63,66,
           92,54,61,59,48,71,83,89,99,69,
           66,40,48,41,99,68,52,78,77,71,
           40,65,77,87,96,44,54,60,89,72,90]
test=gradeData

#Part A
#sort the data
test.sort()

#determine the median
for i in range(int(len(test)/2+0.5)):
    if (len(test)%2!=0):#execute process for ODD lists
        median=test[i]
    else:#execute process for EVEN lists
        add=test[i+1]+test[i-1]
        median=add/2

print("The median is",median,"when using a loop.")

#Part B
#initialize new list to start fake sorting
original=gradeData
original=[6,7,9,8,2,1,0,3]
fakeSort=[]

while (len(original)>0):
    #find the minimum value in orgininal list:
    minimum=original[0]
    for i in original:
        if(i<minimum):
            minimum=i        
    #append value to new list
    fakeSort.append(minimum)
    #delete element from original list
    original.remove(minimum) 
    #del original[original.index(minimum)]
print("\nThe sorted list would be",str(fakeSort))

#reverse the sorted list 
reverse=[]
for i in range(-1,-len(fakeSort)-1,-1):
   reverse.append(fakeSort[i])
print("\nThe reversed list would be", str(reverse))

#find median 
mid=len(fakeSort)/2
if len(fakeSort)%2==0:#even so average
    add=fakeSort[int(mid)]+fakeSort[int(mid-1)]
    median=add/2
else:#odd
    print("odd")
    median= fakeSort[int(mid-.5)]

print("\nThe median is",median,"based on the fake sorted list.")