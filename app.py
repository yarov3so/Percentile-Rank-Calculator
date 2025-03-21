#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import pandas as pd
import math
import streamlit as st

st.title("Percentile Rank Calculator")

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
    
st.markdown("Calculates the percentile rank of all values in a data set. Supports suppressed value ranges. Finds values corresponding to a given percentile rank.")


# st.text("Enter all the data values in increasing order, separated by commas. For suppressed entries, enter how many there are in each group between two underscores: \" _ { number of suppressed entries in the group } _ \" . Note that the values within each group of suppressed entries are assumed to be strictly between the two values that the group is sandwiched between.")
data=st.text_input("Enter all the data values in increasing order, separated by commas. For suppressed entries, enter how many there are in each group between two underscores: \" \_ { number of suppressed entries in the group } \_ \" . Note that the values within each group of suppressed entries are assumed to be strictly between the two values that the group is sandwiched between.")


if data=="":
    st.stop()
    
data=comprehend(data)

while True:
    data_check=[]
    for el in data:
        if el!=None:
            data_check.append(el)
    if sorted(data_check)!=data_check:
        data=st.text_input(("You did not enter your values in increasing order! Check the order and try again."))
        if data=="":
            st.stop()
        data=comprehend(data)
    else:
        break
        
st.text(f"Your data set has a total of {len(data)} entries, of which {len(data)-data.count(None)} are made explicit.")
output="The explicitly stated entries have values: "+", ".join([str(num) for num in sorted([int(el) if int(el)==el else el for el in set(data)-{None}])])
st.text(f"{output}")

df=pd.DataFrame(columns=["Value","Percentile Rank"])

for entry in set(data)-{None}:
    df.loc[len(df)]=[entry,math.ceil(100*(data.index(entry) + 0.5*data.count(entry))/len(data))]

df["Percentile Rank"]=df["Percentile Rank"].astype(int)
df=df.sort_values(by='Value', ascending=True).reset_index(drop=True)

if set([float(int(el)) for el in set(data)-{None}])==set(data)-{None}:
    df["Value"]=df["Value"].astype(int)

st.dataframe(df,hide_index=True)
st.text("")

st.markdown("##### Find values corresponding to a given percentile rank")

pr=st.text_input("Enter the required percentile rank: ")

if pr=="":
    st.text("")
    st.markdown("""*Crafted by yarov3so*   
<a href="https://www.buymeacoffee.com/yarov3so" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="width: 9em; height: auto; padding-top: 0.7em; padding-bottom: 1em" ></a>  
See my other [Math Help Tools](https://mathh3lptools.streamlit.app)""",unsafe_allow_html=True)
    st.stop()
    
pr=int(pr)

if pr in list(df["Percentile Rank"]):
    st.text(f"The following values have percentile rank equal to {pr}: " + ", ".join(df[df["Percentile Rank"]==pr]["Value"].astype(str).tolist())+" .")
else:
    st.text("There are no values in the data set with the specified percentile rank.") 

smallest_value=min(df[df["Percentile Rank"]>=pr]["Value"])
pr_smallest_value=min(df[df["Percentile Rank"]>=pr]["Percentile Rank"])

st.text(f"The smallest value having a percentile rank of at least {pr} is {smallest_value}. This value has percentile rank equal to {pr_smallest_value}.")

st.text("")
st.markdown("""*Crafted by yarov3so*   
<a href="https://www.buymeacoffee.com/yarov3so" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="width: 9em; height: auto; padding-top: 0.7em; padding-bottom: 1em" ></a>  
See my other [Math Help Tools](https://mathh3lptools.streamlit.app)""",unsafe_allow_html=True)
