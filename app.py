#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import pandas as pd
import math

print("\n")

def comprehend(mystring):
    mystring=mystring.replace(" ", "")
    data_list=mystring.split(",")
    data =[]
    for el in data_list:
        try:
            data.append(float(el))
        except: 
            for i in range(int(re.findall(r'\d+', el)[0])):
                data.append(None)
    return data

print("Percentile Rank Calculator by yarov3so\n")

data=comprehend(input("Enter all the data values in increasing order, separated by commas. For suppressed entries, enter how many there are in each group between two underscores: \"_{ number of suppressed entries in the group}_\". Note that the values within each group of suppressed entries are assumed to be strictly between the two values that the group is sandwiched between. \n\n") )

while True:
    data_check=[]
    for el in data:
        if el!=None:
            data_check.append(el)
    if sorted(data_check)!=data_check:
        print("\n")
        data=comprehend(input("You did not enter your values in increasing order! Check the order and try again. \n\n"))
    else:
        print("\n")
        break
    
print(f"Your data set has a total of {len(data)} entries, of which {len(data)-data.count(None)} are made explicit. \n")
print(f"The explicitly stated entries have values:",", ".join([str(num) for num in sorted([int(el) if int(el)==el else el for el in set(data)-{None}])]))

print("\n")

df=pd.DataFrame(columns=["Value","Percentile Rank"])

for entry in set(data)-{None}:
    df.loc[len(df)]=[entry,math.ceil(100*(data.index(entry) + 0.5*data.count(entry))/len(data))]

df["Percentile Rank"]=df["Percentile Rank"].astype(int)
df=df.sort_values(by='Value', ascending=True).reset_index(drop=True)

if set([float(int(el)) for el in set(data)-{None}])==set(data)-{None}:
    df["Value"]=df["Value"].astype(int)

print(df.to_string(index=False))
print("\n")
