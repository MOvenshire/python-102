# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Marissa Ovenshire
# Section:      ENGR 102 - 220
# Team:         N/A
# Assignment:   Lab 7b__ Program 1 
# Date:         10/ 6/ 2020 
#
"""
print("This program translates a string to Pig Latin")

#get a word from user until user enters STOP
word=input("Please enter a word: ")

while word!="STOP":    
    #convert to pig latin - if vowel add yay
    w=word[0]
    if(w=="a"or w=="A" or w=="e" or w=="E" or w=="i" or w=="I" or w=="o" or w=="O" or w=="u" or w=="U" or w=="y" or w=="Y"):
        pig=word+"yay"
    #convert to pig latin -if consonant add first letter+ ay
    else:
        pig=word[1:]+word[0]+"ay"
    print(pig)
        
    #get new word
    word=input("Please enter a word: ")
    