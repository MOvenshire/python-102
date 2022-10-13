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
# Assignment:   Lab 11 Activity 1
# Date:         11/03/2020
#

#Test Cases
'''
	y = 3x^3 - 6x^2 + 5x + 1												roots = -.165 # Typical
	y = 13x^5 - 7x^4 + 1.5x^3 - 25x^2 + 0x + 0 		roots = 0 and 1.416 
	y = 0x^4 - 3x^2 + 0x + 10											roots = -1.826 and 1.826
'''

#create functions
def evalPoly(coefList,x):
    sum = 0
    j=len(coefList)-1
    for i in range(len(coefList)):
        sum += (float(coefList[i]) * (x ** j))
        j-=1
    return sum #value of polynomial evaluated at x

def polyStr(coefList):
    '''This funciton takes a list of coefficients and prints the polynomial.'''
    pStr=""
    j=len(coefList)-1
    for i in range(len(coefList)-2):
        pStr+="("+str(coefList[i])+")x^"+str(j)+" + "
        j-=1
    pStr=pStr+"("+coefList[-1]+")"
    
    return pStr #string of the polynomial if the powers are in ascending order


#main code
print("Using the bisection method to find a single root of P(x) on interval (a,b)")

#ask user for coefficients separated by commas
coef=input("Please enter the coefficients of P(x) separated by commas:")
#make the coeficients into a list of strings
cList=coef.split(",")


#get the interval to find the root 
interval=input("Please enter the interval a,b such that a is less than b:")
#set input as a list then set a and b as numbers
interval_split=interval.split(",")
a=float(interval_split[0])
b=float(interval_split[1])

print("P(x)="+polyStr(cList))
print("Interval (a,b) = ("+str(a) +", "+ str(b)+")")

## Bisecting the interval & finding f_c and f_a
c = (a + b) / 2
#evaluate function at end points and root 
f_a = evalPoly(cList, a)

f_c = evalPoly(cList, c)

print("\nThe loop iterates until the size of the interval decreases below 1.0e-0.6 or the absolute value of the function decreases below 1.0e-08 or both. \n")

# f_c = solve polynomial here for c
print("-"*100)
#print the header
print("{:<8s}{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}{:<15s}\n".format("iter","a","b","c","f_a","f_c","|b - a|"),end="")
num_iter = 1
while abs(b - a) > (1 * (10 ** -6)) and abs(f_c) > (1 * (10 ** -8)):
  print("{:4d}   {:.8f}   {:.8f}   {:.8f}    {:.8f}     {:.8f}    {:.8f}".format(num_iter,a,b,c,f_a,f_c,abs(b - a),end=""))
  num_iter += 1
  if f_a * f_c > 0:
     a = c
  elif f_a * f_c < 0:
     b = c
  elif f_a * f_c == 0:
  ## Root is C
    print(1)
  
  f_a = evalPoly(cList, a)
  c = (a + b) / 2
  f_c = evalPoly(cList, c)

#print the last iteration that is smaller than the tolerance
print("{:4d}   {:.8f}   {:.8f}   {:.8f}    {:.8f}     {:.8f}    {:.8f}".format(num_iter,a,b,c,f_a,f_c,abs(b - a),end=""))

#print summary of findings 
print()
print('-'*100)
print('The root is: {:.8f}'.format(c))
print('P(root) = {:.8f}'.format(f_c))
print('The number of iterations is', num_iter)