# -*- coding: utf-8-sig -*-
import Levenshtein as lv
import glob
import os
import re
import csv



Name = 'ВЕА'

file3reader = csv.reader(open('/home/sonders/Recognizer/server/sorted_names.csv'), delimiter=",")
dist_names = []
possible_names = []
#possible_names_popularity = []
search_next = True
i = 10

while search_next and i <= 51529:
    for ID,name_csv,Sex,PeoplesCount,WhenPeoplesCount,Source in file3reader:
        print(i)
        if lv.distance(Name, name_csv.upper()) == 0 and int(PeoplesCount) >= 1000: # found it
            Name = name_csv.upper()
            search_next = False
            print(ID)
                        
        elif lv.distance(Name, name_csv.upper()) <= 4 and int(PeoplesCount) >= 200:
            
            i = i+1
            possible_names.append(name_csv.upper())
            #possible_names_popularity.append(int(PeoplesCount))
            dist_names.append(lv.distance(Name, name_csv.upper())) 
    
        else:
            i = i+1 
#print('possible names list', possible_names)
if search_next:
    #print('possible names list', possible_names) 
    min_dist = min(dist_names)
    #max_popularity = max(possible_names_popularity)

    if min_dist <= 2:
        min_dist_ind = dist_names.index(min_dist)
        name_correct = possible_names[min_dist_ind]
        Name = name_correct
        
    else:
        Name = Name

print(Name)