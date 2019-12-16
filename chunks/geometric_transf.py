import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg


img = cv2.imread('image1.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[574,755],[728,755],[728,789],[574,789]])
pts2 = np.float32([[0,0],[154,0],[154,34],[0,34]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(154,34))

cv2.imwrite('dst.jpg', dst)
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

