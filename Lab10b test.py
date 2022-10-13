# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab__ Activity 
# Date:         / /  
#
"""
import numpy as np
import matplotlib.pyplot as plt


#open and read weather data
weather=open("WeatherDataWindows.csv")

dataList=[]
#make each line a list 
data=weather.readlines()
for line in data:
    dataList.append(line.split(","))
dataList.pop(0)

weather.close()

#note datalist[n][0]date
#columns are 0 Date,1Temp High,2 Temp Avg,3 Temp Low, 4 Dew Point High,
#5 Dew Point Avg,6 Dew Point Low,7 Humidity High,8 Humidity Avg,9 Humidity Low,
#10 Pressure High,11 Pressure Avg,12 Pressure Low,13 Precipitation (in.)

FIGURE1=1
FIGURE2=2
FIGURE3=3
FIGURE4=4
"""
#a. create line graph of avg temperature and pressure over period of time 
#x-axis date
#y-axis1 measurements for temperature
#y-axis2 measurements for avg pressure
figure1=plt.figure(FIGURE1)
avgTemp=[]
avgPres=[]
date=[]
count=0
#create lists with the number of days, avg temperature, and avg pressure
for day in dataList:
    avgTemp.append(int(day[2]))
    avgPres.append(float(day[11]))
    date.append(count)
    count+=1

#find max and min to set tick marks later
start1=min(avgTemp)
end1=max(avgTemp)

start2=min(avgPres)
end2=max(avgPres)

#assign left and right axes
leftAxis=figure1.add_subplot(1,1,1)
rightAxis=leftAxis.twinx()

#plot data from lists
leftAxis.plot(date,avgTemp,label="Average Temperature",color='r')
rightAxis.plot(date,avgPres,label="Average Pressure",color='b')

#set titles and legend location
plt.title('Average Temperature and Pressure for Date Range')
leftAxis.set_xlabel('Date')
leftAxis.set_ylabel('Temperature')
rightAxis.set_ylabel('Pressure')
figure1.legend(loc='lower left')

#set range for tick marks on x and y axes 
leftAxis.yaxis.set_ticks(np.arange(start1,end1,10))
rightAxis.yaxis.set_ticks(np.arange(start2,end2,.2))
leftAxis.xaxis.set_ticks(np.arange(0,count,200))

#b. create histogram of amounts of precipitation
#x-axis range of precipitation levels
#y-axis number of days that had precipitation in range
figure2=plt.figure(FIGURE2)
leftAxis2=figure2.add_subplot(1,1,1)

#set chart and axes titles
plt.title('Histogram of precipitation')
leftAxis2.set_ylabel('Number of days')
leftAxis2.set_xlabel('Precipitation, in.')

#count how many days have how much precipitation 
#create a list of all precipitation
precip=[]
precipStr=""
for day in dataList:
    precipStr+=(day[13])
    
#make the string into a sorted list without the \n
precip1=precipStr.split('\n')
precip1.sort()
precip1.pop(0)

#convert the sorted list to floats
for i in precip1:
    precip.append(float(i))

#remove 0.0 to get rid of 820 count distortion
while 0.0 in precip:
    precip.remove(0.0)
        
#graph and set x axis ticks
plt.hist(precip,np.arange(0.01,9,.01),color='b',rwidth=10)
leftAxis2.xaxis.set_ticks(np.arange(0,9,1))



#c. scatterplot of relationships between avg temperature and avg dew point
#x-axis average temperature
#y-axis average dew point
"""

#d. create bar chart with 1 bar per month showing avg temp along wit error bars indicating the high and low each month

