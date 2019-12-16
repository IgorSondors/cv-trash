

'''
# Импортируем необходимые модули
import cv2, os
import numpy as np
from PIL import Image

# Для детектирования лиц используем каскады Хаара
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

path = 'Igor1.jpg'

def get_images(path):

    gray = Image.open(path).convert('L')
    image = np.array(gray, 'uint8')

    faces = faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    cv2.waitKey(27)
    cv2.imshow("", image)


get_images(path)

'''


import cv2

imagePath = 'shut.jpg'
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
gray,
scaleFactor=1.3,
minNeighbors=3,
minSize=(30, 30)
)
print("[INFO] Found {0} Faces!".format(len(faces)))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    while True:
        cv2.imshow("", image)
        if cv2.waitKey(1) == 27:
            break




















