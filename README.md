# data533_lab2

## Package Topic Selection

This repository contains the lab 2 submission for Liza Wood and Levannia Lildhar. 

The package written is titled `myfitness`
    - This package provides some basic tools to analyze the health data in a csv file downloaded from Apple Health. These tools could be used to analyze and compare the data from multiple people.
    
`healthdata` 
- contains two modules
    1. `data` - contains the name, age and gender of the person (the "superclass") and a method to read in the csv health data file using pandas
    2. `chart` - uses pygal to provide an interactive bar chart to the user

`summary`
- contains two modules 
    1. `table` - returns a summarized dataframe of average steps per month
    2. `maxmin`- contains functions to calculate the maximum and minimum number of steps
    
## Package Details

The package functions of `myfitness` are described below. The use of the package is also demonstrated in the test file included in this repositry

`healthdata`
This subpackage is meant to provide users a method of importing data as well as viewing the data interactively. 

Detailed descriptions  `data` module in the `healthdata` subpackage is shown below:  

| Module        | Description                                                            | Parameters        | Return                  |
| -------------  |:------------------------------------------------------------------:   | :----------------:|:-----------------------:|
| `__init__`     | Create an object of class Person() to be used in further analysis. This is the superclass | name, age, gender |An object of class Person|
| `display`      | Displays the name, age and gender of a Person() object                | Person() object   | Attributes name, age, and gender| 
| `healthdata`   | Create a object of class healthdata() this inherits from the superclass Person()| name, age, gender, csv file downloaded from Apple Health | Display of healthdata object attributes name, age, gender and dataframe containing healthdata() object file|

Detailed description of `chart` module in the `healthdata` subpackage is shown below:  

| Module        | Description                                                            | Parameters        | Return                  |
| -------------  |:------------------------------------------------------------------:   | :----------------:|:-----------------------:|
| `chart`     | Creates an interactive bar graph using pygal | columnX as list of strings, columnY as list of values, xlabel as string, ylabel as string |.svg file with xlabel, ylabel and title|




