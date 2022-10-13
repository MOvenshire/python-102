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
# Assignment:   Lab 10b Activity 2
# Date:         10/27/2020
#

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

#a. create line graph of avg temperature and pressure over period of time 
#x-axis date
#y-axis1 measurements for temperature
#y-axis2 measurements for avg pressure
figure1=plt.figure(FIGURE1)
avgTemp=[]
avgPres=[]
date=[]
count=0
for day in dataList:
    avgTemp.append(int(day[2]))
    avgPres.append(float(day[11]))
    date.append(count)
    count+=1

start1=min(avgTemp)
end1=max(avgTemp)

start2=min(avgPres)
end2=max(avgPres)

leftAxis=figure1.add_subplot(1,1,1)
rightAxis=leftAxis.twinx()

leftAxis.plot(date,avgTemp,label="Avg Temperature",color='b')
rightAxis.plot(date,avgPres,label="Avg Pressure",color='r')

plt.title('Average Temperature and Pressure for a Date Range')
leftAxis.set_xlabel('Date')
leftAxis.set_ylabel('Temperature')
rightAxis.set_ylabel('Pressure')
figure1.legend(loc='best')


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

print(precip.count(0.0))

#remove 0.0 to get rid of 820 count distortion
while 0.0 in precip:
    precip.remove(0.0)
        
#graph and set x axis ticks
plt.hist(precip,np.arange(0.01,9,.01),color='b',rwidth=10)
leftAxis2.xaxis.set_ticks(np.arange(0,9,1))


#c. scatterplot of relationships between avg temperature and avg dew point
#x-axis average temperature
#y-axis average dew point
figure3=plt.figure(FIGURE3)

avgTemp2=[]
avgDewPoint=[]
date=[]
count=0
for day in dataList:
    avgTemp2.append(int(day[2]))
    avgDewPoint.append(float(day[5]))

graph1 =figure3.add_subplot(1,1,1)
graph1.scatter(avgTemp2,avgDewPoint,s=5,color='black')
graph1.set_xlabel('Average Temperature')
graph1.set_ylabel('Average Dew Point')
graph1.set_title("Average Dew Point vs Average Temperature")

#d. create bar chart with 1 bar per month showing avg temp along wit error bars indicating the high and low each month
#Create empty lists for each of the months
jan = []
feb = []
march = []
apr = []
may = []
june = []
july = []
aug = []
sept = []
octo = []
nov = []
dec = []

for a in range(len(dataList)):
    dataList[a][0] = dataList[a][0].split('/') #Separate the date so that the numbers can be properly evaluated
    name = a
for num in range(1, 13):
    
    ## For each month:
        #Go through the data list and create individual lists for each month
        #Create three individual lists, 1 for each year
        #Use list indexing to sort each month, based on then number of days in each month.

    if num == 1:
        for x in range(len(dataList)):
            if int(dataList[x][0][0]) == num:
                jan.append(int(dataList[x][2]))
        jan1 = jan[:31]
        jan2 = jan[31:62]
        jan3 = jan[62:]
    if num == 2:
        for x in range(len(dataList)):
            if int(dataList[x][0][0]) == num:
                feb.append(int(dataList[x][2]))
        feb1 = feb[:28]
        feb2 = feb[28:56]
        feb3 = feb[56:]
    if num == 3:
        for x in range(len(dataList)):
            if int(dataList[x][0][0]) == num:
                march.append(int(dataList[x][2]))
        march1 = march[:31]
        march2 = march[31:62]
        march3 = march[62:]
    if num == 4:
        for x in range(len(dataList)):
            if int(dataList[x][0][0]) == num:
                apr.append(int(dataList[x][2]))
        apr1 = apr[:30]
        apr2 = apr[30:60]
        apr3 = apr[60:]
    if num == 5:
        for x in range(len(dataList)):
            if int(dataList[x][0][0]) == num:
                may.append(int(dataList[x][2]))
        may1 = may[:31]
        may2 = may[31:62]
        may3 = may[62:]
    if num == 6:
        for x in range(len(dataList)):
            if int(dataList[x][0][0]) == num:
                june.append(int(dataList[x][2]))
        june1 = june[:30]
        june2 = june[30:60]
        june3 = june[60:]
    if num == 7:
        for x in range(len(dataList)):
            if int(dataList[x][0][0]) == num:
                july.append(int(dataList[x][2]))
        july1 = july[:31]
        july2 = july[31:62]
        july3 = july[62:]
    if num == 8:
        for x in range(len(dataList)):
            if int(dataList[x][0][0]) == num:
                aug.append(int(dataList[x][2]))
        aug1 = aug[:31]
        aug2 = aug[31:62]
        aug3 = aug[62:]
    if num == 9:
        for x in range(len(dataList)):
            if int(dataList[x][0][0]) == num:
                sept.append(int(dataList[x][2]))
        sept1 = sept[:30]
        sept2 = sept[30:60]
        sept3 = sept[60:]
    if num == 10:
        for x in range(len(dataList)):
            if int(dataList[x][0][0]) == num:
                octo.append(int(dataList[x][2]))
        octo1 = octo[:31]
        octo2 = octo[31:62]
        octo3 = octo[62:]
    if num == 11:
        for x in range(len(dataList)):
            if int(dataList[x][0][0]) == num:
                nov.append(int(dataList[x][2]))
        nov1 = nov[:30]
        nov2 = nov[30:60]
        nov3 = nov[60:]
    if num == 12:
        for x in range(len(dataList)):
            if int(dataList[x][0][0]) == num:
                dec.append(int(dataList[x][2]))
        dec1 = dec[:31]
        dec2 = dec[31:62]
        dec3 = dec[62:]

#Find the average of each month by getting the sum of the temperatures for the month and dividing by the total number of days in the month, then add it to the list        
tempAvg = [(sum(jan1) / 31), (sum(feb1) / 28), (sum(march1) / 31), (sum(apr1) / 30), (sum(may1) / 31), (sum(june1) / 30), (sum(july1) / 31), (sum(aug1) / 31), (sum(sept1) / 30), (sum(octo1) / 31), (sum(nov1) / 30), (sum(dec1) / 31), (sum(jan2) / 31), (sum(feb2) / 28), (sum(march2) / 31), (sum(apr2) / 30), (sum(may2) / 31), (sum(june2) / 30), (sum(july2) / 31), (sum(aug2) / 31), (sum(sept2) / 30), (sum(octo2) / 31), (sum(nov2) / 30), (sum(dec2) / 31), (sum(jan3) / 31), (sum(feb3) / 28), (sum(march3) / 31), (sum(apr3) / 30), (sum(may3) / 31), (sum(june3) / 30), (sum(july3) / 31), (sum(aug3) / 31), (sum(sept3) / 30), (sum(octo3) / 31), (sum(nov3) / 30), (sum(dec3) / 31)]

month = ['1', '2', '3', '4', '5', '6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36']
#Find the minimum and maximum values in each list
errormin = [min(jan1), min(feb1), min(march1), min(apr1), min(may1), min(june1), min(july1), min(aug1), min(sept1), min(octo1), min(nov1), min(dec1), min(jan2), min(feb2), min(march2), min(apr2), min(may2), min(june2), min(july2), min(aug2), min(sept2), min(octo2), min(nov2), min(dec2), min(jan3), min(feb3), min(march3), min(apr3), min(may3), min(june3), min(july3), min(aug3), min(sept3), min(octo3), min(nov3), min(dec3)]
errormax1 = [max(jan1), max(feb1), max(march1), max(apr1), max(may1), max(june1), max(july1), max(aug1), max(sept1), max(octo1), max(nov1), max(dec1), max(jan2), max(feb2), max(march2), max(apr2), max(may2), max(june2), max(july2), max(aug2), max(sept2), max(octo2), max(nov2), max(dec2), max(jan3), max(feb3), max(march3), max(apr3), max(may3), max(june3), max(july3), max(aug3), max(sept3), max(octo3), max(nov3), max(dec3)]
errormax = []
count = 0

#Create a max for the error bar
for num in errormax1:
    errormax.append(errormax1[count] - errormin[count]) #Add to the list for the error bar
    count += 1
FIGURE4 = 4
figure4=plt.figure(FIGURE4)

bar = figure4.add_subplot(1,1,1)
bar.bar(month, tempAvg, yerr = [errormin, errormax])

bar.set_xlabel('Average Temperature')
bar.set_ylabel('Average Dew Point')
bar.set_title("Average Temperature by Month")
bar.xaxis.set_ticks(np.arange(1,37,2))