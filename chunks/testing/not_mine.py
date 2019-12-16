import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import os

def draw_circle(event, x, y, flags, param):
    l = []
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
        p = (x, y)
        l.append(p)
        print(l)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
img = cv2.imread(r'C:/Users/sondors/Desktop/not_prepared/1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.resizeWindow('image', 600, 600)

cv2.setMouseCallback('image', draw_circle)

while 1:
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

rows, cols, channels = img.shape
pts1 = np.float32(l)
pts2 = np.float32([[0, 0], [200, 0], [200, 100], [0, 100]])

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (200, 100), cv2.INTER_LINEAR)

h1 = math.sqrt((abs(pts1[1][0] - pts1[0][0])) ** 2 + (abs(pts1[1][1] - pts1[0][1])) ** 2)
h2 = math.sqrt((abs(pts1[3][0] - pts1[2][0])) ** 2 + (abs(pts1[3][1] - pts1[2][1])) ** 2)
v1 = math.sqrt((abs(pts1[3][0] - pts1[0][0])) ** 2 + (abs(pts1[3][1] - pts1[0][1])) ** 2)
v2 = math.sqrt((abs(pts1[2][0] - pts1[1][0])) ** 2 + (abs(pts1[2][1] - pts1[1][1])) ** 2)
max_h = int(max(h1, h2))
max_v = int(max(v1, v2))


dst = cv2.resize(dst, (max_h, max_v))
plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()