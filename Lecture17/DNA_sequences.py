#!/usr/bin/python3

import re
import os

os.system("cp /localdisk/data/BPSM/Lecture17/long_dna.txt .")

dna = open("long_dna.txt").read()
len(dna)

# split the dna into pieces
print("\n".join(re.findall('.{1,60}', dna)))

BpsmI = "A[ATCG]TAAT"

count = 0
frag_num = 1
for match in re.finditer(BpsmI, dna):
    a = match.start()
    b = match.end()
    if count == 0:
        length = a - count + 3
        print(f"length of the fragment No.{frag_num} is {length}")
        count = b
        frag_num += 1
    else:
        length = a - count + 6
        print(f"length of the fragment No.{frag_num} is {length}")
        count = b
        frag_num += 1

length = len(dna)- b + 2
print(f"length of the fragment No.{frag_num} is {length}")


#what fragment lengths will get if digest the sequence with a novel restriction enzyme, with ANT*AAT as it's site
re.split(r"[ANT].[AAT]", dna.read().strip())