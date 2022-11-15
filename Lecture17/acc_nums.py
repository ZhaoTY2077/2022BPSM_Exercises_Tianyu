#!/usr/bin/python3
import re
import os

acc_nums = "xkn59438, yhdck2, eihd39d9, chdsye847, hedle3455, xjhd53e, 45da, de37dp".split(', ')

output = []

for acc_num in acc_nums:
    # contain the number "5"
    if re.search(r"5", acc_num):
        output.append('contain the number 5: ' + acc_num)
    # contain the letter d or e
    if re.search(r"[de]", acc_num):
        output.append("contain letter d or e: " + acc_num)
    # contain the letter d and e in that order
    if re.search(r"de", acc_num):
        output.append("contain the letter de in order: " + acc_num)
    # contain the letter d and e in that order and allow any thing between them
    if re.search(r"d.*e", acc_num):
        output.append("contain the letter d...e in order: " + acc_num)
    # contain the letter d and in that order with a sindle letter between them
    if re.search(r"d[a-zA-Z{1}]e", acc_num):
        output.append("contain the letter de with a letter between them: " + acc_num)
    # contain the letter d and e in any order
    if re.search(r"d", acc_num) and re.search(r"e", acc_num):
        output.append("contain both d and e in any order: " + acc_num)
    # start with x or y
    if re.search(r"^[xy]", acc_num):
        output.append("start with x or y: " + acc_num)
    # start with x or y and end with e
    if re.search(r"^[xy].+e$", acc_num):
        output.append("start with x or y and end with e: " + acc_num)
    # contains any 3 numbers in any order:
    if len(re.findall(r"\d", acc_num)) == 3:
    # if re.search(r"\d{3}", acc_num):
        output.append("contains 3 numbers in any order: " + acc_num)

    # contain 3 different numbers
    if len(set(re.findall(r"\d", acc_num))) == 3:
        output.append("contains 3 different numbers: " + acc_num)
    # contain three or more numbers in a row
    if re.search(r"\d{3,}", acc_num):
        output.append("contains 3 or more numbers in a row: " + acc_num)
    # end with d followed by either a, r or p
    if re.search(r"d[arp]$", acc_num):
        output.append("end with d followed by either a, r or p: " + acc_num)
output.sort()

for i in output:
    print(i)
