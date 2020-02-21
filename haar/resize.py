from matplotlib import pyplot as plt
import cv2

img = cv2.imread('2.jpg',0)

plt.imshow(img, cmap = 'gray')
plt.show()

img = cv2.resize(img, (72, 24))
plt.imshow(img, cmap = 'gray')
plt.show()