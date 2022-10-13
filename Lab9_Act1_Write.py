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
# Assignment:   Lab 9 Activity 1 Write
# Date:         10/20/2020
#

# Get User Input for File Name
fileName = input('Enter name for text files --> ')

# Create file with user input and set to write
fileNew_txt = open(fileName + ".txt", "w")
fileNew_csv = open(fileName + ".csv", "w")
row = ""
formi = "{:>10}"
i = 0
temp = ""
temp2 = ""

# Loop until user says stop
while "-1" not in row:
  row = input('Enter the values for the next row seperated by |, enter -1 to stop inputting--> ')
  
  # Make input a list
  row = row.split("|")
  
  # Reset temp value
  temp = ""
  temp2 = ""

  
  # Check if exited this iteration
  if "-1" not in row:
      # Print names left justified
      temp += "{:<11}".format(row[0])
      temp2 += row[0]
      
      # Add other values right justified
      for j in range(1, len(row)):
          temp += formi.format(row[j])
          temp2 += ","+ row[j]
      # Print to file
      fileNew_csv.write(temp2+"\n")
      fileNew_txt.write(temp+"\n")
      i += 1

# Close Files
fileNew_csv.close()
fileNew_txt.close()