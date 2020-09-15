import glob
import os
import re
import csv


#filename,file_size,file_attributes,region_count,region_id,region_shape_attributes,region_attributes
#"{""text"":""Дата выдачи""}"
file1reader = csv.reader(open('data1.csv', encoding='utf-8'), delimiter=",")
#useless_str = ['РОССИЙСКАЯ ФЕДЕРАЦИЯ','Р О С С И Й С К А Я Ф Е Д Е Р А Ц И Я','Паспорт выдан','Дата выдачи','Код подразделения','Личный код','Личная подпись', 'Дата рождения','Место рождения', 'Отчество', 'Фамилия', 'Имя','Пол']
#x = re.sub('[ !№@#$,()абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ]', '', i)

useless_str = ['РОССИЙСКАЯФЕДЕРАЦИЯ','Паспортвыдан','Датавыдачи','Кодподразделения','Личныйкод','Личнаяподпись','Датарождения','Месторождения','Отчество','Фамилия','Имя','Пол']

l = open("data_new.txt",'w', encoding="utf-8")
{"text":"Фамилия"}
dist_issue = []
possible_Issue_Place = []
search_next = True
while search_next: 
    for filename,file_size,file_attributes,region_count,region_id,region_shape_attributes,region_attributes in file1reader:
        if  re.sub('[ }{text":]', '',region_attributes) not in useless_str:
            l.write(filename + ';' + region_shape_attributes + ';' +region_attributes +'\n')
            
        else:
            search_next = False    
