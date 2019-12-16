
from matplotlib import pyplot as plt
import cv2
import numpy as np

img = cv2.imread('alien.jpg',0)

'''#####
# Добавляем белый отступ для дальнейшего нахождения контура
# Вертикальный отступ
img = np.vstack((img, np.full((1, np.shape(img)[1]), 255, dtype=np.uint8) ))
img = np.vstack((img, np.full((1, np.shape(img)[1]), 255, dtype=np.uint8) ))
img = np.vstack((img, np.full((1, np.shape(img)[1]), 255, dtype=np.uint8) ))
img = np.vstack((img, np.full((1, np.shape(img)[1]), 255, dtype=np.uint8) ))
img = np.vstack((img, np.full((1, np.shape(img)[1]), 255, dtype=np.uint8) ))
img = np.vstack((img, np.full((1, np.shape(img)[1]), 255, dtype=np.uint8) ))
img = np.vstack((img, np.full((1, np.shape(img)[1]), 255, dtype=np.uint8) ))
img = np.vstack((img, np.full((1, np.shape(img)[1]), 255, dtype=np.uint8) ))
img = np.vstack((img, np.full((1, np.shape(img)[1]), 255, dtype=np.uint8) ))
img = np.vstack((img, np.full((1, np.shape(img)[1]), 255, dtype=np.uint8) ))
img = np.vstack((img, np.full((1, np.shape(img)[1]), 255, dtype=np.uint8) ))
img = np.vstack((img, np.full((1, np.shape(img)[1]), 255, dtype=np.uint8) ))
img = np.vstack((img, np.full((1, np.shape(img)[1]), 255, dtype=np.uint8) ))
img = np.vstack((img, np.full((1, np.shape(img)[1]), 255, dtype=np.uint8) ))
img = np.vstack((img, np.full((1, np.shape(img)[1]), 255, dtype=np.uint8) ))

img = np.vstack((np.full((1, np.shape(img)[1]), 255, dtype=np.uint8), img ))
img = np.vstack((np.full((1, np.shape(img)[1]), 255, dtype=np.uint8), img ))
img = np.vstack((np.full((1, np.shape(img)[1]), 255, dtype=np.uint8), img ))
img = np.vstack((np.full((1, np.shape(img)[1]), 255, dtype=np.uint8), img ))
img = np.vstack((np.full((1, np.shape(img)[1]), 255, dtype=np.uint8), img ))
img = np.vstack((np.full((1, np.shape(img)[1]), 255, dtype=np.uint8), img ))
img = np.vstack((np.full((1, np.shape(img)[1]), 255, dtype=np.uint8), img ))
img = np.vstack((np.full((1, np.shape(img)[1]), 255, dtype=np.uint8), img ))
img = np.vstack((np.full((1, np.shape(img)[1]), 255, dtype=np.uint8), img ))
img = np.vstack((np.full((1, np.shape(img)[1]), 255, dtype=np.uint8), img ))
img = np.vstack((np.full((1, np.shape(img)[1]), 255, dtype=np.uint8), img ))
img = np.vstack((np.full((1, np.shape(img)[1]), 255, dtype=np.uint8), img ))
img = np.vstack((np.full((1, np.shape(img)[1]), 255, dtype=np.uint8), img ))

print(np.shape(img)[0], np.shape(img)[1])

# Горизонтальный отступ

img = np.hstack((img, np.full((np.shape(img)[0], 1), 255, dtype=np.uint8) ))
img = np.hstack((img, np.full((np.shape(img)[0], 1), 255, dtype=np.uint8) ))
img = np.hstack((img, np.full((np.shape(img)[0], 1), 255, dtype=np.uint8) ))
img = np.hstack((img, np.full((np.shape(img)[0], 1), 255, dtype=np.uint8) ))
img = np.hstack((img, np.full((np.shape(img)[0], 1), 255, dtype=np.uint8) ))
img = np.hstack((img, np.full((np.shape(img)[0], 1), 255, dtype=np.uint8) ))
img = np.hstack((img, np.full((np.shape(img)[0], 1), 255, dtype=np.uint8) ))
img = np.hstack((img, np.full((np.shape(img)[0], 1), 255, dtype=np.uint8) ))
img = np.hstack((img, np.full((np.shape(img)[0], 1), 255, dtype=np.uint8) ))
img = np.hstack((img, np.full((np.shape(img)[0], 1), 255, dtype=np.uint8) ))

img = np.hstack((np.full((np.shape(img)[0], 1), 255, dtype=np.uint8), img ))
img = np.hstack((np.full((np.shape(img)[0], 1), 255, dtype=np.uint8), img ))
img = np.hstack((np.full((np.shape(img)[0], 1), 255, dtype=np.uint8), img ))
img = np.hstack((np.full((np.shape(img)[0], 1), 255, dtype=np.uint8), img ))
img = np.hstack((np.full((np.shape(img)[0], 1), 255, dtype=np.uint8), img ))
img = np.hstack((np.full((np.shape(img)[0], 1), 255, dtype=np.uint8), img ))
img = np.hstack((np.full((np.shape(img)[0], 1), 255, dtype=np.uint8), img ))
img = np.hstack((np.full((np.shape(img)[0], 1), 255, dtype=np.uint8), img ))
img = np.hstack((np.full((np.shape(img)[0], 1), 255, dtype=np.uint8), img ))
img = np.hstack((np.full((np.shape(img)[0], 1), 255, dtype=np.uint8), img ))
img = np.hstack((np.full((np.shape(img)[0], 1), 255, dtype=np.uint8), img ))
img = np.hstack((np.full((np.shape(img)[0], 1), 255, dtype=np.uint8), img ))
img = np.hstack((np.full((np.shape(img)[0], 1), 255, dtype=np.uint8), img ))
img = np.hstack((np.full((np.shape(img)[0], 1), 255, dtype=np.uint8), img ))
img = np.hstack((np.full((np.shape(img)[0], 1), 255, dtype=np.uint8), img ))
img = np.hstack((np.full((np.shape(img)[0], 1), 255, dtype=np.uint8), img ))
img = np.hstack((np.full((np.shape(img)[0], 1), 255, dtype=np.uint8), img ))
img = np.hstack((np.full((np.shape(img)[0], 1), 255, dtype=np.uint8), img ))
img = np.hstack((np.full((np.shape(img)[0], 1), 255, dtype=np.uint8), img ))
img = np.hstack((np.full((np.shape(img)[0], 1), 255, dtype=np.uint8), img ))


print(np.shape(img)[0], np.shape(img)[1])
####'''

#ret,thresh = cv2.threshold(img,127,255,0)

ret,thresh = cv2.threshold(img,221,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(cnt)
print(M)

epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)

x,y,w,h = cv2.boundingRect(cnt)
y = cv2.rectangle(thresh,(x,y),(x+w,y+h),(0,255,0),2)

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
x = cv2.drawContours(thresh,[box],0,(0,0,255),2)


plt.imshow(y, cmap = 'gray')
plt.show()