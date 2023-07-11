#Name: Gabe Maturo
#Class: IS678 Data Analytics in Cybersecurity
#Date: 2/15/23
#Program Description: This code will generate a random data frame that will be used to provide
#                     a graph of the contingency table

import numpy as np #import the numbers/computing functions 
import pandas as pd #importing pandas to read data into the pandas dataframe

#creating dataframe and naming it random_df
#using the random function from the numpy library to generate random integers between 1-10
#these integers will then fill the dataframe which has size 1000 rows by 2 columns
#I chose size 1000 to give a large enough sample size for the graph
random_df = pd.DataFrame(np.random.randint(0, 10, size=(1000, 2)))

#Renaming the columns as 'Risk' and 'Reliability'
random_df.columns = ["Risk","Reliability"]

#printing the list to ensure that the data frame has been generated correctly
print(random_df)

#Output should be in the form of:
#    Risk  Reliability
#0       7            2
#1       3            5
#2       2            4
#3       4            8
#4       8            8
#..    ...          ...
#995     6            4
#996     8            6
#997     9            5
#998     7            6
#999     9            8

#Obviously output will be different each time it is run since the numbers are random


import matplotlib.pyplot as plt #import plot functions

# compute contingency table for Risk/Reliability factors which 
# produces a matrix of counts of rows that have attributes at
# each (x, y) location
# need cm for basic colors
# need arange to modify axes display
from matplotlib import cm #color map
from numpy import arange #Return evenly spaced values within a given interval

# graphical view of contingency table 
xtab = pd.crosstab(random_df['Risk'], random_df['Reliability'])
plt.pcolor(xtab,cmap=cm.Greens) #use green color map
#define dimensions of the different sections of the horizontal index on the chart
plt.yticks(arange(0.5,len(xtab.index), 1),xtab.index)
#define dimensions of the different sections of the vertical index on the chart
plt.xticks(arange(0.5,len(xtab.columns), 1),xtab.columns)
plt.colorbar() #add colorbar to the chart
plt.title("Risk ~ Reliability")

#Output should be graph similar to the one in Figure 3-9 
#This graph uses random generated data

