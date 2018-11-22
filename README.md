# data533_lab2

## Package Topic Selection

This repository contains the lab 2 submission for Liza Wood and Levannia Lildhar. 

The package written is titled `myfitness`
    - This package will read a csv downloaded from Apple Health and perform the analyses described in the subpackages below. 
    
`read` 
- will read in the csv file using pandas

`summary`
- contains four modules 
    1. `table` - will return a summarized dataframe by year and month
    2. `min`- will return the month and year with the minimum number of steps 
    3. `mean`- will give the mean of the steps returned by the `table` module
    4. `max`- will return the year and month with the max number of steps 

`display`
- will display the dataframe using pygal to provide an interactive graph to the user
