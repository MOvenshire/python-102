
print("Howdy!")

# Open Data file
pData=open("ThermoData_P_5_10_15_MPa_win.csv", 'r')

dataList=[]
for line in pData:
    splitData=line.split(",")
    dataList.append(splitData)
#print(dataList)

pres=input("Please enter a pressure of 5, 10 or 15 (MPa) When you are done entering values, enter -1:  ")

# User input
while int(pres) != -1:
    if pres=="5":
        #data=data5
        cols=0
        temp2=260  
    elif pres == '10':
        #data=data10
        cols= 4
        temp2=300
    else:
        cols=8
        temp2=340

    question= "Please enter temperature in °C: 0 <= T <= "+str(temp2)+": "
    temp=float(input(question))
    ## There are 22 individual lists inside of our big list
    ## We start at row 5, or index 4... OR WE COULD DELETE THE FIRST FEW ROWS
    dataList[0:4] = []
    #print(dataList)
    if temp <= 0.0 or temp >= float(temp2):
        print("That temperature is not in range.")
        break
        
    else:
        #find bracket temps
        higher=0
        lower=0
        for i in range(len(dataList)):
            if float(dataList[i][0])>=temp:
                higher= float(dataList[i][0])
                hIndex=i
                lower= float(dataList[i-1][0])
                break
            # Volume
            # Get values for interpolation for Volume
        volI = float((dataList[hIndex-1][1+cols]))
        volF = float(dataList[hIndex][1+cols])
    # Calculate Volume
        vol=volI+(temp-lower)*(volF-volI)/(higher-lower)
        
    # Internal Energy
    #get interpolation points based on brackets
        lowIE= float(dataList[hIndex-1][2+cols])
        highIE= float(dataList[hIndex][2+cols])
        intEnergy= float(dataList[hIndex-1][2+cols])+(temp-lower)*((highIE-lowIE)/(higher-lower))
            
    # Enthalpy
        lowEnth= float(dataList[hIndex-1][3+cols])
        highEnth= float(dataList[hIndex][3+cols])
        enth= float(dataList[hIndex-1][3+cols])+(temp-lower)*((highEnth-lowEnth)/(higher-lower))
    
    # Entropy 
        lowEntr= float(dataList[hIndex-1][4+cols])
        highEntr= float(dataList[hIndex][4+cols])
        entr= float(dataList[hIndex-1][4+cols])+(temp-lower)*((highEntr-lowEntr)/(higher-lower))
    
    # Output **Just a suggestion but it might be easier to use the brackets and string formatting tools to round the values
        print()    
        print("The specific volume, v, at T =",temp,"°C is {:.8f} m^3/kg.".format(vol)) 
        print("The specific internal energy, u, at T = ",temp,"°C is {:.2f} kJ/kg.".format( intEnergy))
        print("The specific enthalpy, h, at T =",temp,"°C is {:.2f} kJ/kg.".format(enth))
        print("The specific entropy, s, at T =",temp,"°C is {:.4} kJ/kg*K.".format(entr))
    
        pres=input("Please enter a pressure of 5, 10 or 15 (MPa) When you are done entering values, enter -1:  ")