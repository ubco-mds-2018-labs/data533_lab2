# data533_lab2

## Package Topic Selection

This repository contains the lab 2 submission for Liza Wood and Levannia Lildhar. 

The package written is titled `myfitness`
    - This package provides some basic tools to analyze the health data in a csv file downloaded from Apple Health. These tools could be used to analyze and compare the data from multiple people.
    
`view` 
- contains two modules
    1. `healthdata` - contains the name, age and gender of the person (the "superclass") and a method to read in the csv health data file using pandas
    2. `chart` - uses pygal to provide an interactive bar chart to the user

`summary`
- contains two modules 
    1. `table` - returns a summarized dataframe of average steps per month
    2. `minmax`- contains functions to calculate the minimum and maximum number of steps
