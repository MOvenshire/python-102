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
# Assignment:   Lab 11b Functions
# Date:         11/03/2020
#

from math import pi

#function a
#write function that find the volume remaining with given dimensions
#part 1: write a function assuming the hole has a radius less than the smaller of the 2 values 
def function_a1(length, width, height, radius):
    '''This function takes the length, width, and height of a rectangle. 
    Then it takes the radius of a drill bit and calculates the remaining volume 
    after drilling the hole. This program assumes that the radius is smaller than 
    the smallest side of the rectangle'''
    minSide=min(length/2,width/2)
    if radius<minSide:
        volBox=length*width*height
        volCyl=height*pi*radius**2
        return volBox-volCyl
	
#part 2: write a function that accounts for larger radii        
def function_a2(length,width,height,radius):
    '''This function takes the length, width, and height of a rectangle. 
    Then it takes the radius of a drill bit and calculates the remaining 
    volume after drilling the hole even if the diameter is greater than one 
    of the side lengths.'''
    d=radius*2
    shorter=min(length,width)
    longer=max(length,width)
    #basically same as function_a1
    if d<=shorter:
        vol=length*width*height-height*pi*radius**2
    #test if the diameter is bigger than the largest side of the rectangle
    elif d>longer:
        vol=0
    #test for more difficult sections and approximate with squares
    elif d>shorter and d<longer:
        small_square=(shorter)**2 # make a square inside circle
        area_circle=pi*radius**2 # Circle area
        shaded_area_sec=(area_circle-small_square)/4 # gets bit of circle outside the square
        rectangle_area=(width)*(length) # Calculates rectangle area
        rectangle_area_cut=rectangle_area-small_square-2*shaded_area_sec # Calculate rectangle area minus cut
        vol=rectangle_area_cut*height # calculate vol
    else:
        small_square_s=(shorter)**2
        small_square_l=(longer)**2
        area_circle = pi*radius**2
        shaded_area_sec_s=(area_circle-small_square_s)/4
        shaded_area_sec_l=(area_circle-small_square_l)/4
        rectangle_area=(width)*(length) # Calculates rectangle area
        rectangle_area_cut=rectangle_area-small_square-2*shaded_area_sec_s-2*shaded_area_sec_l # Calculate rectangle area minus cut
        vol=rectangle_area_cut*height # calculate vol
    return vol
         
#function b
def function_b(names,annualCost,prodCost):
    '''This function  takes 3 parallel lists with the names, 
    operation costs, and value of products. Then it will return 
    the name of the least profitable factory.'''
    
    #create a list for the net profitability of all the factories with a loop and subtraction
    net=[]
    for i in range(len(names)):
        net.append(prodCost[i]-annualCost[i])
    index=net.index(min(net))
    #find the name of the least profitable 
    return names[index]
    
#function c
def function_c(name,city,state,zCode,street1,street2=""):
    '''This function takes parameters for name, city, state, 
    zipcode, and a street address and prints an address label.'''
    print(name)
    print(street1)
    if street2!="":
        print(street2)
    print(city+","+state,zCode)

#function d
def function_d(name):
    '''This function will take the name of a file with a .csv 
    extension and write an equivalent .tsv file.'''
    #open files 
    c=open(name+".csv")
    t=open(name+".tsv","w")
    #read the whole file into 1 string
    stringC=c.read()
    stringT=""
    #write file with same name but \t instead of ,
    while "," in stringC:
        index=stringC.index(",")
        stringT+= stringC[:index]+"\t"
        stringC=stringC[index+1:]
    t.write(stringT)

    #close files 
    c.close()
    t.close()
    
#function e
def function_e(liste):
    '''This function takes a parameter of a list and returns the 
    minimum, maximum, and mean values as a tuple.'''
    minimum = min(liste)
    maximum = max(liste)
    mean = 0
    for num in liste:
        mean += float(num)
    mean = mean / len(liste)
    return minimum, maximum, mean

#function f
def function_f(timeL, dist):
  '''This function takes paramaters of lists for time and distance 
  and returns the velocity between consecutive measurements.'''
  vel_list = []
  for n in range(len(timeL)-1):
    #subtract final-initial for distance over time from slope formula
    newT = timeL[n + 1] - timeL[n]
    newD = dist[n + 1] - dist[n]
    newvel = newD / newT
    vel_list.append(newvel)
  return vel_list