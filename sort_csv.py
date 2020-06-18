# -*- coding: utf-8-sig -*-
import Levenshtein as lv
import glob
import os
import re
import csv

file3reader = csv.reader(open('/home/sonders/Recognizer/server/not_api/russian_surnames.csv'), delimiter=",")
FILENAME = "/home/sonders/Recognizer/server/not_api/sorted_surnames.csv"

sorted_list = []

for ID,name_csv,Sex,PeoplesCount,WhenPeoplesCount,Source in file3reader:
    
        line = [ID,name_csv,Sex,int(PeoplesCount),WhenPeoplesCount,Source]
        sorted_list.append(line)
        
newlist = sorted(sorted_list, key=lambda x: x[3], reverse=True)    

#print(sorted_list)
with open(FILENAME, "a", newline="") as file:
    writer = csv.writer(file)

    writer.writerows(newlist)