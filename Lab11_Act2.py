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
# Assignment:   Lab 11 Activity 2
# Date:         11/03/2020
#

# Test cases
'''
	Typical case
    val=25 x=0.0010011
    Edge case
	val = 20 x=0.0009996
    Extrapolation case
	val = -10 x=0.00099675
'''
# Functions
def Interp(x0,x1,y1,y2,val):
	'''This function takes a beginning and ending Temp and Vol and a query value
	   and outputs the predicted Vol for that query value '''
	return y1 + (val - x0) * (y2 - y1) / (x1 - x0)

# Creating file and usable list
#name = input('Enter name for file --> ')
#dataFile = open(name + '.txt', 'r')
dataFile = open('Lab11-data-Act2.txt', 'r')
val = int(float(input('Enter a query value --> ')))
d = dataFile.readlines()
d = d[4:]
for i in range(len(d)):
    d[i] = d[i].split(' ')
    while '' in d[i]:
        d[i].remove('')
    for j in range(len(d[i])):
        d[i][j] = float(d[i][j])
d.sort()
print(d)


ans = 0
cnt = 0
l = len(d)
initial = (val // 20) * 20
if val >= 0 and val < 260:
    while d[cnt][0] != initial:
        cnt += 1
    ans = Interp(initial, initial + 20, d[cnt][1], d[cnt + 1][1], val)
elif val < 0:
    ans = d[0][1] + ((val - 0) / (20 - 0)) * (d[1][1] - d[0][1])
elif val >= 260:
    ans = d[l - 2][1] + ((val - 240) / (260 - 240)) * (d[l - 1][1] - d[l - 2][1])
print('The value for x =', val, 'is', ans)

