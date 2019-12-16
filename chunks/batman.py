from matplotlib import pyplot as plt
import cv2
import numpy as np

# Загружаем изображение паспорта
img = cv2.imread('2.jpg',0)

# Вертикальный отступ
img = np.vstack((img, np.full((30, np.shape(img)[1]), 255, dtype=np.uint8) ))
img = np.vstack((np.full((30, np.shape(img)[1]), 255, dtype=np.uint8), img ))

# Горизонтальный отступ

img = np.hstack((img, np.full((np.shape(img)[0], 30), 255, dtype=np.uint8) ))
img = np.hstack((np.full((np.shape(img)[0], 30), 255, dtype=np.uint8), img ))
img1 = img
# Tresholding

edge = cv2.Canny(img,170,250)

print(np.shape(img)[0], np.shape(img)[1])

ret,thresh = cv2.threshold(img,255,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


# Делаем прелбразование Хаффа

#img = cv2.imread('dave.jpg')
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#edges = cv2.Canny(gray,50,150,apertureSize = 3)

lines = cv2.HoughLinesP(thresh,1,np.pi/180,100,minLineLength=100,maxLineGap=1000)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imwrite('houghlines5.jpg',edge)
img1 = cv2.imread('houghlines5.jpg')





# Вместо трешхолдинга используем Канни

thresh = edge

#print(img1)

# Находим координаты всех контуров
contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

# Делаем словарь {Площадь:Контур}

area_dict = {}
for c in contours:
  area = cv2.contourArea(c)
  area_dict[area] = c

# Ищем нужный контур

#print(len(area_dict))

k = list(area_dict.keys())
#print(k)
#print(max(k))

'''# Вместо ручного удаления добавим цикл для выбора контура (при уменьшении площади последующего контура более, чем в два раза, выбираем предыдущий)
choosing_contour = True
s = sorted(k)
print(sorted(s))
while choosing_contour:
    if s[len(s)-1]/s[len(s)-2] < 2:
        s.remove(max(s))
    else:
        choosing_contour = False
'''
'''print(sorted(s))
print(max(s))'''

# Удаляем самый большой контур
k.remove(max(k))
#print(max(k))

# Удаляем второй по величине контур
k.remove(max(k))

# Выбираем нужный контур для препроцессинга
my_area = max(k)
my_cnt = area_dict.get(my_area)

# Получаем 4 крайние точки контура
print(np.shape(my_cnt))
print(my_cnt)

#print(cv2.CHAIN_APPROX_SIMPLE(my_cnt))

'''epsilon = 0.1*cv2.arcLength(my_cnt,True)
approx = cv2.approxPolyDP(my_cnt,epsilon,True)
'''

'''# Рисуем горизонтальный контур
x,y,w,h = cv2.boundingRect(my_cnt)
y = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) # Для наглядности меняем thresh на img'''

# Рисуем контур, который может быть под углом
rect = cv2.minAreaRect(my_cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
z = cv2.drawContours(img1,[box],0,(0,0,255),10) # Для наглядности меняем thresh на img

# Получаем картинку, прошедшую препроцессинг
plt.imshow(z, cmap = 'gray')
plt.show()

# Рисуем все контура
rect = cv2.minAreaRect(my_cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
q = cv2.drawContours(img,contours,-1,(0,0,255),1) # Для наглядности меняем thresh на img

plt.imshow(q, cmap = 'gray')
plt.show()




'''
# Рисуем все контура по очереди
i = 0
for i in range(len(contours)):
    cnt = contours[i]
    area = cv2.contourArea(cnt)
    print(area)

    ###
    epsilon = 0.1*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)

    x,y,w,h = cv2.boundingRect(cnt)
    y = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    ###
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    z = cv2.drawContours(thresh,[box],0,(0,255,0),2)

    plt.imshow(z, cmap = 'gray')
    plt.show()'''
