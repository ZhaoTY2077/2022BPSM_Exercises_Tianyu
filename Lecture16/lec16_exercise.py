#!/usr/bin/python3

import logging, sys, re, numpy as np
import pandas as pd

pd.Series(['a','b','c','d'])

df = pd.read_csv('eukaryotes.txt', sep = '\t', na_values = ["-"])


# Q1
fungi = df[(df['Size (Mb)'] > 100) & (df['Group'] == 'Fungi')]
result = fungi.apply(lambda x: x['#Organism/Name'].split()[1] , axis = 1)
list(result)

# Q2
df = pd.read_csv("eukaryotes.txt", sep = '\t', na_values = ["-"])
df["Group"].value_counts()
df.groupby("Group")["WGS"].count()
# value_counts will count all the values in each group while counts will return the number of each group.

# Q3
Heli = df[df.apply(lambda x: x["#Organism/Name"].split(" ")[0] == "Heliconius", axis = 1)]
resultq3 = Heli.apply(lambda x: x["#Organism/Name"].split(" ")[1:], axis = 1)
Heli[ ['#Organism/Name', 'Scaffolds'] ]


# Q4
centernums = df.groupby("Group")["Center"].value_counts()
resultq4 = centernums["Plants"]

# Q5
df["ratio"] = df["Proteins"]/df["Genes"]
morethan = df[df.apply(lambda x: x["ratio"] >= 1.10 , axis = 1)]
resultq5 = list(morethan.apply(lambda x: x["#Organism/Name"].split(" ")[0] , axis = 1))
