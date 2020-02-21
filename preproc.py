import os
import cv2

path = r'C:\Users\sondors\Desktop\change'

#!/usr/bin/env python
from glob import glob                                                           
import cv2 
pngs = glob('./*.jpeg')

for j in pngs:
    img = cv2.imread(j)
    
    cv2.imwrite(j[:-3] + 'jpg', img)






'''for name in os.listdir(path):
    print(name)
    image = cv2.imread(os.path.join(path, name))
    # name_split = os.path.split(name)[0]
    os.remove(os.path.join(path, name))
    cv2.imwrite(path, image)'''

'''from PIL import Image
from os import listdir
from os.path import splitext

target_directory = path
target = '.jpg'

for file in listdir(target_directory):
    filename, extension = splitext(file)
    try:
        if extension not in ['.py', target]:
            im = Image.open(filename + extension)
            im.save(filename + target)
    except OSError:
        print('Cannot convert %s' % file)'''