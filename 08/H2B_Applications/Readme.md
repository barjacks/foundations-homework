# Documentation of H-2B Visa Programme

## Setting up the data

* The data is [here](https://www.foreignlaborcert.doleta.gov/performancedata.cfm).

* H-2B Program
The H-2B working visa is a nonimmigrant visa which allows foreign nationals to enter into the U.S. temporarily and engage in nonagricultural employment which is seasonal, intermittent, a peak load need, or a one-time occurrence.

* FY refers to the financial year, so Oct 1 - Sep 30. 

* The data is posted on a quartely basis since 2008. However, comparing the files as the data dictionaries have changed over the past years. I have collected the way the dictionaries have changed [here](https://docs.google.com/spreadsheets/d/1A_y5oTvbZcrLyymoc7SwhL4FhW_i3sI1IZAsOkfWZ9E/edit#gid=0). The year 2015 has by far the most data. In this initial excerise I will only be looking at the latest year. 

* Here is the [data dictionary of 2015](https://docs.google.com/document/d/1EXFgRnW5dPaiORLHiXC360xtEqxj5cOi97FH5LpAcLE/edit?usp=sharing).

## Questions
    1. How many requests did the Office of Foreign Labor Certification (OFLC) receive in 2015?
    2. How many jobs did that regard in total? How many full time positions?
    3. How many jobs did the ETA National Processing Center actually certify? 
    4. What was the average pay?
    5. Who earned the least? And where are these people working?
    6. What was the most common unit of pay (daily, weekly, monthly)?
    7. Work our total pay amount payed to H-2B laborers?
    8. Were there any foreign companies hiring foreign workers in the US? If yes, work out averages by nation.
    9. Most common job title. Graph this.
    10. Which US state had the largest need? Make a graph of this.
    11. Which industries had the largest need? 
    12. Which companies had the largest need? Compare acceptance/denials of each company.
    
    ***BONUS*** Looking into [Silver Bay Seafoods](http://www.silverbayseafoods.com/about.html) and [UK International Soccer Campus](http://www.uksocca.com/). 
    
## Problems

* Can Pandas deal with messy data? Is there an efficient way for Pandas to clean the data? Merge "Landscape Laborer" with "LANDSCAPE LABORER" etc.? See question ten.
* This .fillna(0.0) is magic. I found it [here](http://stackoverflow.com/questions/21291259/convert-floats-to-ints-in-pandas)
df['NAIC_CODE'] = df['NAIC_CODE'].fillna(0.0).astype(int)
But it turns out, it only works for my original file, changing floats into int. In the file I am imported, it changes objects into floats. Why?

    
    