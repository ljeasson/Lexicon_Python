# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 23:30:47 2017
@author: ljeas

Spirit Animal User ID: creativeBison
Date: 2/28/17
Challenge 2

Sources:
Data Science from Scratch: First Principles with Python
by Joel Grus

"How to print a dictionary line by line in Python?" - Stack Overflow
URL: http://stackoverflow.com/questions/15785719/how-to-print-a-dictionary-line-by-line-in-python

"""
#Imports
from __future__ import division
from collections import Counter
import matplotlib.pyplot as mplot
import csv

def sentiment(fileName):
    #Sentiment Values   
    Negative = 0    
    Weakly_Negative = 0
    Neutral = 0
    Weakly_Positive = 0
    Positive = 0
    
    #Read in speech data 
    speech = open(fileName, "r")
    speech = speech.read()
    speech = speech.split(" ") #Split the data by spaces (" ")
    
    #Adds words in speech to a list
    speech_words = []
    for index in range(0, len(speech)-1):
        if speech[index] != "?" or speech[index] != "." or speech[index] != "!":
            speech_words.append(speech[index].lower()) #Convert data to lowercase
    
    #Convert list to set (to get unique words)
    speech_words = set(speech_words)
    
    #Count number of times each word appears in data
    speech_count = Counter(speech_words)
            
    #Loop through your count of unique words (use dictionary or Counter from step 6)  
    for key1,value1 in speech_count.items(): 
        for key2,value2 in lexicon.items():
            if key1 == key2:
                try:
                    value2 = float(value2)
                except:
                    value2 = int(value2)
                if value2 >= -1.0 and value2 < -0.6:
                    Negative += value1
                elif value2 >= -0.6 and value2 < -0.2:
                    Weakly_Negative += value1
                elif value2 >= -0.2 and value2 <= 0.2:
                    Neutral += value1
                elif value2 > 0.2 and value2 <= 0.6:
                    Weakly_Positive += value1
                elif value2 > 0.6 and value2 <= 1.0:
                    Positive += value1
    
    #Get total number of unique words in speech            
    total = Negative + Weakly_Negative + Neutral + Weakly_Positive + Positive
           
    #Calculate percentage of words that are negative, weak negative, etc.
    xaxis = [1,2,3,4,5]
    yaxis = [Negative/total, Weakly_Negative/total, Neutral/total,\
             Weakly_Positive/total, Positive/total,]
    
    #Plot
    mplot.title("Sentiment Distribution for " + str(fileName))
    mplot.bar(xaxis, yaxis, color = "blue")
    mplot.show()
    print("DONE")
    
#============================================================================
    
#Open and read sentiment lexicon
reader = csv.reader(open("sent_lexicon.csv", "r"))

#Store lexicon in dictionary
lexicon = {}
for row in reader:
    k,v = row
    lexicon[k] = v  
               
#Axis Labels
mplot.xlabel("Sentiment")
mplot.ylabel("Percent of Words")

#Label tick marks on axes
xpos = [1,2,3,4,5]
sentiments = ["Negative","Weak\nNegative","Neutral\nStatement","Weak\nPositive","Positive"]
mplot.xticks(xpos, sentiments)

ypos = [0.00,0.05,0.10,0.15,0.20,0.25,0.30]
mplot.yticks(ypos)           

#Asks for file name
print("Enter the name of your file")
fileName = input()
sentiment(fileName)
             
   