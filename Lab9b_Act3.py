# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab 9 b __ Activity 3
# Date:         10/ 20/ 2020 
#
"""

#open the file 
weather=open("WeatherDataWindows.csv")

dataList=[]
dataList2=[]
#make each line a list 
data=weather.readlines()
print(data)
for line in data:
    dataList.append(line.split(","))
dataList.pop(0)

#note datalist[n][0]date
#columns are 0 Date,1Temp High,2 Temp Avg,3 Temp Low, 4 Dew Point High,
#5 Dew Point Avg,6 Dew Point Low,7 Humidity High,8 Humidity Avg,9 Humidity Low,
#10 Pressure High,11 Pressure Avg,12 Pressure Low,13 Precipitation (in.)

#find the minimum temperature
low=dataList[0][3]
for day in dataList:
    if int(low)>int(day[3]):
        low=day[3]
print("The minimum temperature is",low,"degrees Fahrenheit. ")

print()
#find the maximum temperature
high=int(dataList[0][1])
for day in dataList:
    if int(high)<int(day[1]):
        high=day[1]
print("The maximum temperature is",high,"degrees Fahrenheit. ")

print()
#find average daily precipitation
count=0
add=0
for day in dataList:
    count+=1
    add+=float(day[13])
avg=add/count
print("The average daily precipitation is {:.3f} inches.".format(avg))

print()
#find how many days have an average humidity above 90
count=0
for day in dataList:
    if int(day[8])>90:
        count+=1
print("There were",count,"days where the average humidity was over 90%.")

print()
#find the maximum and minimum temperature for April 4 
for day in dataList:
    if '4/4' in day[0]:
        print("The maximum temperature for {} was {:.2f} degrees Fahrenheit".format(day[0],float(day[1])))
        print("The minimum temperature for {} was {:.2f} degrees Fahrenheit".format(day[0],float(day[3])))

print()
#find the average high pressure for October 2016
count=0
add=0
for day in dataList:
    if '10/'in day[0] and '/2016' in day[0] and (not "/10/20"in day[0]):
        add+=float(day[10])
        count+=1
    if('10/10/2016'in day[0]):
        add+=float(day[10])
        count+=1

avg=add/count
print("The average high pressure for Octoer 2016 was {:.2f}".format(avg))

#close the file
weather.close()
